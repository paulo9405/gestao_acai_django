from django.db import models
from django.db.models import Sum, F
from django.forms import FloatField


class CadastroAcai(models.Model):
    nome = models.CharField(max_length=50)
    tamanho = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.nome) + ' / ' + str(self.tamanho) + ' / R$ ' + str(self.valor)


class CadastroAcrescimos(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.nome) + '/  R$' + str(self.valor)


class Pedido(models.Model):
    PAG = (('Dinheiro', 'Dinheiro'), ('Cartão', 'Cartão'),)
    dia = models.DateTimeField(auto_now=True)
    nome_cliente = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True)
    endereco = models.CharField(max_length=200)
    acai_pedido = models.ManyToManyField(CadastroAcai)
    acrescimo_pedido = models.ManyToManyField(CadastroAcrescimos)
    pagamento = models.CharField(max_length=20, choices=PAG)
    observacoes = models.TextField(blank=True)

    valor_pagar = models.DecimalField(blank=True, default=0, max_digits=7, decimal_places=2)


    def get_total(self):
        tot_acai = 0
        tot_acre = 0
        for acai in self.acai_pedido.all():
            tot_acai += acai.valor
            tot_acre = 0
            for acre in self.acrescimo_pedido.all():
                tot_acre += acre.valor
        return tot_acai + tot_acre

    def __str__(self):
        return str(self.acai_pedido) + ' - ' + str(self.nome_cliente)
