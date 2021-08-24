from django.db import models

class Venda(models.Model):
    dia = models.DateField()
    quantidade_entregas = models.IntegerField()
    venda_dinheiro = models.DecimalField(max_digits=5, decimal_places=2)
    venda_cartao = models.DecimalField(max_digits=5, decimal_places=2)
    compras = models.DecimalField(max_digits=5, decimal_places=2)
    descricao_compras = models.CharField(max_length=200, null=True, blank=True)
    despesas = models.DecimalField(max_digits=5, decimal_places=2)
    descricao_despesas = models.CharField(max_length=200, null=True, blank=True)

    venda_total_dia = models.DecimalField(blank=True, default=0, max_digits=5, decimal_places=2)
    despesa_do_dia = models.DecimalField(blank=True, default=0, max_digits=5, decimal_places=2)
    lucro_liquido = models.DecimalField(blank=True, default=0, max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.dia)

    def save(self, *args, **kwargs):
        self.venda_total_dia = (self.venda_dinheiro + self.venda_cartao)
        self.despesa_do_dia = (self.despesas + self.compras)
        self.lucro_liquido = (self.venda_total_dia - self.compras - self.despesas)

        return super(Venda, self).save(*args, **kwargs)

    def soma_mensal_dinheiro(self):
        pass

    def soma_mensal_cartao(self):
        pass # 3%

    def soma_mensal_dinheiro_cartao(self):
        pass

    def soma_despesa_total(self):
        pass

    def soma_mensal_liquido(self):
        pass


