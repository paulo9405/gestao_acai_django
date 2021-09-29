from django.forms import ModelForm
from .models import Venda, Colaborador


class VendaForm(ModelForm):
    class Meta:
        model = Venda
        fields = (
            'dia_da_venda',
            'quantidade_entregas',
            'venda_dinheiro',
            'venda_cartao',
            'compras',
            'descricao_compras',
            'despesas',
            'descricao_despesas',
        )


class ColaboradorForm(ModelForm):
    class Meta:
        model = Colaborador
        fields = (
            'nome',
            'telefone',
            'endereco',
            'salario',
            'descricao_salario',
        )