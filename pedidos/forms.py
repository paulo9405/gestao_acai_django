from django.forms import ModelForm
from .models import CadastroAcai, CadastroAcrescimos


class CadastroAcaiForm(ModelForm):
    class Meta:
        model = CadastroAcai
        fields = (
            'nome',
            'tamanho',
            'valor',
        )

class CadastroAcrecimosForm(ModelForm):
    class Meta:
        model = CadastroAcrescimos
        fields = (
            'nome',
            'valor',
        )
