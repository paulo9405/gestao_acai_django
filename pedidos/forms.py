from django.forms import ModelForm
from .models import CadastroAcai


class CadastroAcaiForm(ModelForm):
    class Meta:
        model = CadastroAcai
        fields = (
            'nome',
            'tamanho',
            'valor',
        )