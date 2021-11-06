from django.views import View
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Venda, Colaborador
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
from django.shortcuts import render



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
    #TODO: reverse lazy esta dando erro(Reverse for 'dashboard' not found. 'dashboard' is not a valid view function or pattern name), corrigir futuramenbte
    success_url = '/core/venda_list'
    #success_url = reverse_lazy('venda_list')


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
