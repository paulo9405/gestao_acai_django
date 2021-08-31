from django.shortcuts import render
from django.views import View
from .models import Venda
from django.db.models import Sum, F, FloatField, Max, Avg, Min, Count


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
