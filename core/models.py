from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string
from .managers import VendaManager
from django.db.models.signals import post_save
from django.dispatch import receiver


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

    class Meta:
        unique_together = ('dia_da_venda', )

    def __str__(self):
        return str(self.dia_da_venda)

    def save(self, *args, **kwargs):
        self.venda_cartao = self.venda_cartao - (self.venda_cartao * 3 / 100)
        self.venda_total_dia = (self.venda_dinheiro + self.venda_cartao)
        self.despesa_do_dia = (self.despesas + self.compras)
        self.lucro_liquido_dia = (self.venda_total_dia - self.compras - self.despesas)

        data = {'dia': self.dia_da_venda,
                'qtd_entregas': self.quantidade_entregas,
                'dinheiro': self.venda_dinheiro,
                'cartao': self.venda_cartao,
                'compras': self.compras,
                'despesas': self.despesas,
                'tot_despesas': self.despesa_do_dia,
                'bruto': self.venda_total_dia,
                'liquido': self.lucro_liquido_dia,
                }

        plain_text = render_to_string('core/emails/nova_venda.txt', data)
        html_email = render_to_string('core/emails/nova_venda.html', data)
        send_mail(
            'Nova venda cadastrada com sucesso',
            plain_text,
            'paulo.ricardo1137.pr@gmail.com',
            ['paulo.ricardo1137.pr@gmail.com'],
            html_message=html_email,
            fail_silently=False,
        )

        return super(Venda, self).save(*args, **kwargs)

    # @receiver(post_save)
    # def envia_email(sender, instance, **kwargs):
    #     data = {'dia': instance}
    #     plain_text = render_to_string('core/emails/nova_venda.txt', data)
    #     html_email = render_to_string('core/emails/nova_venda.html', data)
    #     send_mail(
    #         'Nova venda cadastrada com sucesso',
    #         plain_text,
    #         'paulo.ricardo1137.pr@gmail.com',
    #         ['paulo.ricardo1137.pr@gmail.com'],
    #         html_message=html_email,
    #         fail_silently=False,
    #     )


class Colaborador(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    salario = models.DecimalField(max_digits=7, decimal_places=2)
    descricao_salario = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ('nome', 'telefone')

    def __str__(self):
        return self.nome
