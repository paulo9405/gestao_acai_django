from django.contrib import admin
from.models import Venda

class VendaAdmin(admin.ModelAdmin):
    fields = (
        'dia_da_venda',
        'quantidade_entregas',
        'venda_dinheiro',
        'venda_cartao',
        ('compras', 'descricao_compras'), #campos na msm linha
        ('despesas', 'descricao_despesas'),
        'venda_total_dia',
        'despesa_do_dia',
        'lucro_liquido_dia',
        'venda_dinheiro_total',
        'venda_cartao_total',
    )

    readonly_fields = (
        'venda_total_dia',
        'despesa_do_dia',
        'lucro_liquido_dia',
        'venda_dinheiro_total',
        'venda_cartao_total',
    ) #apenas leitura




admin.site.register(Venda, VendaAdmin)
