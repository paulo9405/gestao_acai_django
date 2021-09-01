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
    )

    readonly_fields = (
        'venda_total_dia',
        'despesa_do_dia',
        'lucro_liquido_dia',
    )


admin.site.register(Venda, VendaAdmin)
