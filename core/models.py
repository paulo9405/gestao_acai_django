from django.db import models
from django.db.models import Aggregate, Sum, FloatField

class Venda(models.Model):
    dia_da_venda = models.DateField()
    quantidade_entregas = models.IntegerField()
    venda_dinheiro = models.DecimalField(max_digits=5, decimal_places=2)
    venda_cartao = models.DecimalField(max_digits=5, decimal_places=2)
    compras = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    descricao_compras = models.CharField(max_length=200, null=True, blank=True)
    despesas = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    descricao_despesas = models.CharField(max_length=200, null=True, blank=True)

    venda_total_dia = models.DecimalField(blank=True, default=0, max_digits=5, decimal_places=2)
    despesa_do_dia = models.DecimalField(blank=True, default=0, max_digits=5, decimal_places=2)
    lucro_liquido_dia = models.DecimalField(blank=True, default=0, max_digits=5, decimal_places=2)

    venda_dinheiro_total = models.DecimalField(blank=True, default=0, max_digits=5, decimal_places=2)
    venda_cartao_total = models.DecimalField(blank=True, default=0, max_digits=5, decimal_places=2)



    def __str__(self):
        return str(self.dia_da_venda)

    def save(self, *args, **kwargs):
        self.venda_total_dia = (self.venda_dinheiro + self.venda_cartao)
        self.despesa_do_dia = (self.despesas + self.compras)
        self.lucro_liquido_dia = (self.venda_total_dia - self.compras - self.despesas)
        #self.venda_dinheiro_total = (Venda.objects.all().aggregate(v_d=Sum('venda_dinheiro')))['v_d'] + self.venda_total_dia

        return super(Venda, self).save(*args, **kwargs)

    #vendas = Venda.objects.filter(data_venda=data_inicial, data_venda=data_final)
    # def soma_mensal_dinheiro(self):
    #     tot = self.venda_set.all().aggregate(ven_din=Sum('venda_dinheiro'))
    #     self.venda_dinheiro_total = tot
    #     self.save()

    # from core.models import Venda
    # from django.db.models import aggregate, Sum
    #
    # Venda.objects.all().aggregate(v_d=Sum('venda_dinheiro'))
    #
    # {'v_d': Decimal('151')}




    def soma_mensal_cartao(self):
        pass # 3%

    def soma_mensal_dinheiro_cartao_total(self):
        pass

    def soma_despesa_total(self):
        pass

    def soma_mensal_lucro_liquido(self):
        pass


