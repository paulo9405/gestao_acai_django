from django.db import models


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
    pagamento = models.CharField(max_length= 20, choices=PAG)
    acai_pedido = models.ForeignKey(CadastroAcai, on_delete=models.CASCADE)
    acrescimo_pedido = models.ForeignKey(CadastroAcrescimos, on_delete=models.CASCADE)

    valor_pagar = models.DecimalField(blank=True, default=0, max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.acai_pedido) + ' - ' + str(self.nome_cliente)
