from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Venda, Colaborador
from django.urls import reverse_lazy


@method_decorator(login_required, name='dispatch')
class DashboardView(View):
    def get(self, request):
        data = {}
        data['quantidade_entregas'] = Venda.objects.quantidade_entregas()
        data['media_entregas'] =Venda.objects.media_entregas()
        data['venda_mensal_dinheiro'] =Venda.objects.venda_mensal_dinheiro()
        data['venda_mensal_cartao'] =Venda.objects.venda_mensal_cartao_desconto()
        data['soma_venda_dinheiro_cartao'] =Venda.objects.soma_venda_dinheiro_cartao()
        data['despesa_mensal'] =Venda.objects.despesa_mensal()
        data['compras_mensal'] =Venda.objects.compras_mensal()
        data['soma_despesa_total'] =Venda.objects.soma_despesa_total()
        data['soma_mensal_lucro_liquido'] =Venda.objects.soma_mensal_lucro_liquido()

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
    # success_url = reverse_lazy('dashboard')


@method_decorator(login_required, name='dispatch')
class VendaLista(ListView):
    model = Venda


@method_decorator(login_required, name='dispatch')
class ColaboradorCreate(CreateView):
    model = Colaborador
    fields = [
        'nome', 'telefone', 'endereço', 'salario', 'descricao_salario',
    ]
    success_url = '/core/colaborador_list'


@method_decorator(login_required, name='dispatch')
class ColaboradoresLista(ListView):
    model = Colaborador
