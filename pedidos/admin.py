from django.contrib import admin
from .models import CadastroAcai, CadastroAcrescimos, Pedido

class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'dia',
        'nome_cliente',
        'telefone',
        'endereco',
        'acai_pedido',
        'acrescimo_pedido',
        'pagamento',
        'valor_pagar',
    )

    # def total(self, obj):
    #     return obj.get_total()
    #
    # total.short_description = 'Total'

    fieldsets = (
        ('Dados do Cliente', {'fields': ('nome_cliente', 'telefone', 'endereco')}),
        ('Dados do Pedido', {'fields': ('acai_pedido', 'acrescimo_pedido', 'pagamento', 'observacoes', 'valor_pagar')}),
    )

    readonly_fields = ('valor_pagar',)
    search_fields = ('id', 'nome_cliente')





admin.site.register(CadastroAcai)
admin.site.register(CadastroAcrescimos)
admin.site.register(Pedido, PedidoAdmin)
