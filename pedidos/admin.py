from django.contrib import admin
from .models import Acai, Acrescimo, Pedido
from .models import ItemDoPedidoAcai, ItemDoPedidoAcre


class ItemPedidoInLineAcai(admin.TabularInline):
    model = ItemDoPedidoAcai
    extra = 1


class ItemPedidoInLineAcre(admin.TabularInline):
    model = ItemDoPedidoAcre
    extra = 1


class AcaiAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tamanho', 'valor', 'id')
    search_fields = ('id', 'nome')


class AcrecimoAdmin(admin.ModelAdmin):
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
        'valor_pagar',
    )

    fieldsets = (
        ('Dados do Cliente', {'fields': ('nome_cliente', 'telefone', 'endereco')}),
        ('Dados do Pedido', {'fields': ('pagamento', 'observacoes', 'valor_pagar')}),
    )

    readonly_fields = ('valor_pagar',)
    search_fields = ('id', 'nome_cliente',)
    inlines = [ItemPedidoInLineAcai, ItemPedidoInLineAcre]

admin.site.register(Acai, AcaiAdmin)
admin.site.register(Acrescimo, AcrecimoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemDoPedidoAcai)
admin.site.register(ItemDoPedidoAcre)
