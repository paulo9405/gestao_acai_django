from django.contrib import admin
from .models import CadastroAcai, CadastroAcrescimos, Pedido

class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        'dia',
        'nome_cliente',
        'telefone',
        'endereco',
        'pagamento',
        'acai_pedido',
        'acrescimo_pedido',
        'valor_pagar',
    )


admin.site.register(CadastroAcai)
admin.site.register(CadastroAcrescimos)
admin.site.register(Pedido, PedidoAdmin)
