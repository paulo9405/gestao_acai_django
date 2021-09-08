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
