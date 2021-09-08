from django.db import models
from .managers import VendaManager


class Venda(models.Model):
    dia_da_venda = models.DateField()
    quantidade_entregas = models.IntegerField()
    venda_dinheiro = models.DecimalField(max_digits=7, decimal_places=2)
    venda_cartao = models.DecimalField(max_digits=7, decimal_places=2)
    compras = models.DecimalField(max_digits=7, decimal_places=2)
    descricao_compras = models.CharField(max_length=200, null=True, blank=True)
    despesas = models.DecimalField(max_digits=7, decimal_places=2)
    descricao_despesas = models.CharField(max_length=200, null=True, blank=True)

    venda_total_dia = models.DecimalField(blank=True, default=0, max_digits=7, decimal_places=2)
    despesa_do_dia = models.DecimalField(blank=True, default=0, max_digits=7, decimal_places=2)
    lucro_liquido_dia = models.DecimalField(blank=True, default=0, max_digits=7, decimal_places=2)

    objects = VendaManager()

    def __str__(self):
        return str(self.dia_da_venda)

    def save(self, *args, **kwargs):
        self.venda_total_dia = (self.venda_dinheiro + self.venda_cartao)
        self.despesa_do_dia = (self.despesas + self.compras)
        self.lucro_liquido_dia = (self.venda_total_dia - self.compras - self.despesas)

        return super(Venda, self).save(*args, **kwargs)


# class Colaborador(models.Model):
#     nome = models.CharField(max_length=200)
#     telefone = models.CharField(max_length=20)
#     endereço = models.CharField(max_length=200)
#     salario = models.DecimalField(max_digits=7, decimal_places=2)
#     descricao_salario = models.CharField(max_length=200, null=True, blank=True)
#
#     def __str__(self):
#         return self.nome

'''
class SalarioColaborador(models):
    pass
    #colaborador fk
    # dia
    # valor
    # choice (salario, vale)
'''