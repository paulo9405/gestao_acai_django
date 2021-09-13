from django.db import models
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.db.models import Sum, F, FloatField, Max, Avg, Min, Count


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
    pagamento = models.CharField(max_length=20, choices=PAG)
    observacoes = models.TextField(blank=True)

    valor_pagar = models.DecimalField(blank=True, default=0, max_digits=7, decimal_places=2)

    def calcular_total(self):
        tot_acai = self.itemdopedidoacai_set.all().aggregate(
            tot_ped=Sum(F('quantidade') * F('acai__valor'), output_field=FloatField())
        )['tot_ped'] or 0

        tot_acre = self.itemdopedidoacre_set.all().aggregate(
            tot_ped=Sum(F('quantidade') * F('acrescimo__valor'), output_field=FloatField())
        )['tot_ped'] or 0

        soma = tot_acai + tot_acre
        self.valor_pagar = soma
        self.save()


class ItemDoPedidoAcai(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    acai = models.ForeignKey(CadastroAcai, on_delete=models.CASCADE)
    quantidade = models.FloatField()

    def __str__(self):
        return str(self.acai.nome)


class ItemDoPedidoAcre(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    acrescimo = models.ForeignKey(CadastroAcrescimos, on_delete=models.CASCADE)
    quantidade = models.FloatField()

    def __str__(self):
        return str(self.acrescimo.nome)


@receiver(post_save, sender=ItemDoPedidoAcai)
def update_vendas_total_acai(sender, instance, **kwargs):
    instance.pedido.calcular_total()


@receiver(post_save, sender=ItemDoPedidoAcre)
def update_vendas_total_acre(sender, instance, **kwargs):
    instance.pedido.calcular_total()


#@receiver(post_save, sender=ItemDoPedido)
# def update_vendas_total(sender, instance, **kwargs):
#     instance.valor_pagar = instance.calcular_total_acai()
#     instance.save()

# @receiver(post_save, sender=Venda)
# def update_vendas_total2(sender, instance, **kwargs):
#     instance.calcular_total()


