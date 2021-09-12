from django.contrib import admin
from .models import CadastroAcai, CadastroAcrescimos, Pedido


class CadastroAcaiAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tamanho', 'valor', 'id')
    search_fields = ('id', 'nome')


class CadastroAcrecimosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'id')
    search_fields = ('id', 'nome')


class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        'nome_cliente',
        'id',
        'dia',
        'telefone',
        'endereco',
        'pagamento',
        'total',
    )

    fieldsets = (
        ('Dados do Cliente', {'fields': ('nome_cliente', 'telefone', 'endereco')}),
        ('Dados do Pedido', {'fields': ('acai_pedido', 'acrescimo_pedido', 'pagamento', 'observacoes', 'valor_pagar')}),
    )

    readonly_fields = ('valor_pagar',)
    search_fields = ('id', 'nome_cliente',)
    autocomplete_fields = ('acai_pedido', 'acrescimo_pedido')


    def total(self, obj):
        return obj.get_total()

    total.short_description = 'Total'


admin.site.register(CadastroAcai, CadastroAcaiAdmin)
admin.site.register(CadastroAcrescimos, CadastroAcrecimosAdmin)
admin.site.register(Pedido, PedidoAdmin)
