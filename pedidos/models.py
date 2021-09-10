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
    acai_pedido = models.ForeignKey(CadastroAcai, on_delete=models.CASCADE)
    acrescimo_pedido = models.ForeignKey(CadastroAcrescimos, on_delete=models.CASCADE)
    pagamento = models.CharField(max_length=20, choices=PAG)
    observacoes = models.TextField(blank=True)

    valor_pagar = models.DecimalField(blank=True, default=0, max_digits=7, decimal_places=2)


    #TODO: criar funçõa de soma pedido mais acrescimo

    # def get_total(self):
    #     tot_acai = 0
    #     for acai in self.acai_pedido.all():
    #         tot_acai += acai.valor
    #
    #     return (tot_acai)

        # tot_acai = 0
        # tot_acre = 0
        # for acai in self.acai_pedido__:
        #     tot_acai += acai.valor
        #     for acre in self.acrescimo_pedido.all():
        #         tot_acre += acre.valor
        # return (tot_acre + tot_acai)



    def __str__(self):
        return str(self.acai_pedido) + ' - ' + str(self.nome_cliente)

    # def soma_venda_dinheiro_cartao(self):
    #     self.valor_pagar = Pedido.objects.aggregate(
    #         tot_d_c=Sum((F('acai_pedido__valor') + F('acrescimo_pedido__valor')),
    #                     output_field=FloatField()))['tot_d_c'] or 0
    #     self.save()
    #     return self.valor_pagar

    # def save(self, *args, **kwargs):
    #     self.valor_pagar = (self.acai_pedido__valor + self.acrescimo_pedido__valor)
    #     return super(Pedido, self).save(*args, **kwargs)

