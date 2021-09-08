from django.test import TestCase
from .models import CadastroAcai, CadastroAcrescimos
from .forms import CadastroAcaiForm, CadastroAcrecimosForm


class CadastroAcaiTestCase(TestCase):

    def test_form_cad_acai_is_valid(self):
        """
        Teste para validar o fomulario de cadastro de açai é valido
        """
        data_model = {
            "nome": 'Açai Ninho',
            "tamanho": '300 ML',
            "valor": 11.00,
        }

        form = CadastroAcaiForm(data=data_model)
        self.assertTrue(form.is_valid())

    def test_form_cad_acai_is_not_valid(self):
        """
        Teste para dar erro de formulario, prenchimento errado
        """
        data_model = {
            "nome": 123,
            "tamanho": 456,
            "valor": 'letras',
        }

        form = CadastroAcaiForm(data=data_model)
        self.assertFalse(form.is_valid())

    def test_form_cad_acai_field_empty(self):
        """
        Teste para dar erro de formulario com campo obrigatório vazio.
        """
        data_model = {
            "nome": '',
            "tamanho": '',
            "valor": '',
        }

        form = CadastroAcaiForm(data=data_model)
        self.assertFalse(form.is_valid())

    def test_cadastrar_acai(self):
        """
        Teste para criar açai e verificando se os dados não são None.
        """
        data = {
            "nome": 'Açai Ninho',
            "tamanho": '300 ML',
            "valor": 11.00,
        }

        acai = CadastroAcai.objects.create(
            nome=data['nome'],
            tamanho=data['tamanho'],
            valor=data['valor'],
        )

        self.assertIsNotNone(acai)

class CadastroAcrescimosTestCase(TestCase):

    def test_form_cad_acre_is_valid(self):
        """
        Teste para validar o fomulario de cadastro de acrescimos é valido
        """
        data_model = {
            "nome": 'Chocolate',
            "valor": 2.00,
        }

        form = CadastroAcrecimosForm(data=data_model)
        self.assertTrue(form.is_valid())

    def test_form_cad_acre_is_not_valid(self):
        """
        Teste para dar erro de formulario, prenchimento errado
        """
        data_model = {
            "nome": 123,
            "valor": 'letras',
        }

        form = CadastroAcrecimosForm(data=data_model)
        self.assertFalse(form.is_valid())

    def test_form_cad_acre_field_empty(self):
        """
        Teste para dar erro de formulario com campo obrigatório vazio.
        """
        data_model = {
            "nome": '',
            "valor": '',
        }

        form = CadastroAcrecimosForm(data=data_model)
        self.assertFalse(form.is_valid())

    def test_cadastrar_acrescimo(self):
        """
        Teste para criar acrescimo e verificando se os dados não são None.
        """
        data = {
            "nome": 'Chocolate',
            "valor": 2,
        }

        acrescimo = CadastroAcrescimos.objects.create(
            nome=data['nome'],
            valor=data['valor'],
        )

        self.assertIsNotNone(acrescimo)
