from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, ListView

from .models import Venda
from .forms import VendaForm

class DashboardView(View):
    def get(self, request):
        data = {}
        data['quantidade_entregas'] = Venda.objects.quantidade_entregas()
        data['media_entregas'] =Venda.objects.media_entregas()
        data['venda_mensal_dinheiro'] =Venda.objects.venda_mensal_dinheiro()
        data['venda_mensal_cartao'] =Venda.objects.venda_mensal_cartao()
        data['soma_venda_dinheiro_cartao'] =Venda.objects.soma_venda_dinheiro_cartao()
        data['despesa_mensal'] =Venda.objects.despesa_mensal()
        data['compras_mensal'] =Venda.objects.compras_mensal()
        data['soma_despesa_total'] =Venda.objects.soma_despesa_total()
        data['soma_mensal_lucro_liquido'] =Venda.objects.soma_mensal_lucro_liquido()

        return render(request, 'core/dashboard.html', data)


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
    success_url = '/core/dashboard'


class VendaLista(ListView):
    model = Venda
