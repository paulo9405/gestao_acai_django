from django.db import models
from django.db.models import Sum, F, FloatField, Max, Avg, Min, Count


class VendaManager(models.Manager):
    def quantidade_entregas(self):
        return self.all().aggregate(
            Sum('quantidade_entregas'))['quantidade_entregas__sum']

    #TODO: formataar casas decimal
    def media_entregas(self):
        return self.all().aggregate(
            Avg('quantidade_entregas'))['quantidade_entregas__avg']

    def venda_mensal_dinheiro(self):
        return self.all().aggregate(
            tot_dinheiro=Sum(('venda_dinheiro'), output_field=FloatField())
        )['tot_dinheiro']

    # TODO: calculo para diminuir 3% do cartão
    def venda_mensal_cartao(self):
        return self.all().aggregate(
            tot_cartao=Sum(('venda_cartao'), output_field=FloatField())
        )['tot_cartao']

    def soma_venda_dinheiro_cartao(self):
        return self.all().aggregate(
            tot_d_c=Sum((F('venda_dinheiro') + F('venda_cartao')),
                        output_field=FloatField()))['tot_d_c']

    def despesa_mensal(self):
        return self.all().aggregate(
            tot_d_m=Sum(('despesas'), output_field=FloatField())
        )['tot_d_m']

    def compras_mensal(self):
        return self.all().aggregate(
            tot_compras=Sum(('compras'), output_field=FloatField())
        )['tot_compras']

    def soma_despesa_total(self):
        return self.all().aggregate(
            tot_desp=Sum((F('compras') + F('despesas')), output_field=FloatField())
        )['tot_desp']

    def soma_mensal_lucro_liquido(self):
        return self.all().aggregate(
            lucro=Sum(((F('venda_dinheiro') + F('venda_cartao')) - F('compras')
                       - F('despesas')), output_field=FloatField()))['lucro']
