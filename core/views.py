from django.forms import model_to_dict
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Venda, Colaborador
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
from django.shortcuts import render
import csv
from django.contrib import messages





@method_decorator(login_required, name='dispatch')
class DashboardView(View):
    def get(self, request):
        data = {}
        data['quantidade_entregas'] = Venda.objects.quantidade_entregas()
        data['media_entregas'] = Venda.objects.media_entregas()
        data['venda_mensal_dinheiro'] = Venda.objects.venda_mensal_dinheiro()
        data['venda_mensal_cartao'] = Venda.objects.venda_mensal_cartao_desconto()
        data['soma_venda_dinheiro_cartao'] = Venda.objects.soma_venda_dinheiro_cartao()
        data['despesa_mensal'] = Venda.objects.despesa_mensal()
        data['compras_mensal'] = Venda.objects.compras_mensal()
        data['soma_despesa_total'] = Venda.objects.soma_despesa_total()
        data['soma_mensal_lucro_liquido'] = Venda.objects.soma_mensal_lucro_liquido()

        return render(request, 'core/dashboard.html', data)


@method_decorator(login_required, name='dispatch')
class VendaCreate(CreateView):
    model = Venda
    fields = [
        'dia_da_venda',
        'quantidade_entregas',
        'venda_dinheiro',
        'venda_cartao',
        'compras',
        'descricao_compras',
        'despesas',
        'descricao_despesas',
    ]
    success_url = reverse_lazy('core_venda_lista')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "✅ Venda criada com sucesso!")
        return response


@method_decorator(login_required, name='dispatch')
class VendaLista(ListView):
    model = Venda


@method_decorator(login_required, name='dispatch')
class ColaboradorCreate(CreateView):
    model = Colaborador
    fields = [
        'nome', 'telefone', 'endereco', 'salario', 'descricao_salario',
    ]
    success_url = '/core/colaborador_list'


@method_decorator(login_required, name='dispatch')
class ColaboradoresLista(ListView):
    model = Colaborador


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Vendas_pdf(View):
    def get(self, request):
        vendas = Venda.objects.all()
        params = {
            'vendas': vendas,
            'request': request,
        }
        return Render.render('core/vendas-pdf.html', params, 'vendas_pdf')

class Vendas_csv(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="vendas.csv"'

        vendas = Venda.objects.all()

        writer = csv.writer(response)
        writer.writerow([
            'Id',
            'Dia da venda',
            'Entregas',
            'Dinheiro',
            'Cartão',
            'Compras',
            'Despesas',
            'Total Despesa Do dia',
            'Venda dinheiro e cartão',
            'venda liquida'
        ])

        for venda in vendas:
            writer.writerow(
                [venda.id,
                 venda.dia_da_venda,
                 venda.quantidade_entregas,
                 venda.venda_dinheiro,
                 venda.venda_cartao,
                 venda.compras,
                 venda.despesas,
                 venda.venda_total_dia,
                 venda.despesa_do_dia,
                 venda.lucro_liquido_dia
                 ])

        return response


def api(request):
    lista_de_vendas = []
    vendas = Venda.objects.all()

    for venda in vendas:
        lista_de_vendas.append(model_to_dict(venda))

    return JsonResponse(lista_de_vendas, status=200, safe=False)
