from django.contrib.auth.models import User
from django.test import TestCase
from core.models import Venda
from core.forms import VendaForm

class VendaTestCase(TestCase):

    def setUp(self):
        credentials = {
            'username': 'paulo',
            'password': 'paulo@12345'}
        self.user = User.objects.create_user(**credentials)

    def test_form_is_valid(self):
        """
        Teste para validar o fomulario
        """
        data_model = {
            "dia_da_venda": '2020-12-30',
            "quantidade_entregas": 10,
            "venda_dinheiro": 50,
            "venda_cartao": 30,
            "compras": 2,
            "despesas": 1
        }

        form = VendaForm(data=data_model)
        self.assertTrue(form.is_valid())

    def test_form_is_not_valid(self):
        """
        Teste para dar erro de formulario, prenchimento errado
        """
        data_model = {
            "dia_da_venda": '77/128/2020',
            "quantidade_entregas": 'sdfsdf',
            "venda_dinheiro": 'sufd',
            "venda_cartao": 'kgig',
            "compras": 'idfgnf',
            "despesas": 'iosdf'
        }

        form = VendaForm(data=data_model)
        self.assertFalse(form.is_valid())

    def test_form_field_empty(self):
        """
        Teste para dar erro de formulario com campo obrigatório vazio.
        """
        data_model = {
            "dia_da_venda": '',
            "quantidade_entregas": '',
            "venda_dinheiro": '',
            "venda_cartao": '',
            "compras": '',
            "despesas": ''
        }

        form = VendaForm(data=data_model)
        self.assertFalse(form.is_valid())


    def test_criar_venda(self):
        data = {
            "dia_da_venda": '2020-12-30',
            "quantidade_entregas": 10,
            "venda_dinheiro": 50,
            "venda_cartao": 30,
            "compras": 2,
            "despesas": 1
        }

        venda = Venda.objects.create(
            dia_da_venda=data['dia_da_venda'],
            quantidade_entregas=data['quantidade_entregas'],
            venda_dinheiro=data['venda_dinheiro'],
            venda_cartao=data['venda_cartao'],
            compras=data['compras'],
            despesas=data['despesas'],
        )

        self.assertIsNotNone(venda)

#TODO: testar somas do dinheiro e cartao
#TODO: testar somas do de despesa e compra
#TODO: testar soma liquida
'''
    def test_sum_dinheiro_cartao(self):
        data = {
            "dia_da_venda": '2020-12-30',
            "quantidade_entregas": 10,
            "venda_dinheiro": 50,
            "venda_cartao": 30,
            "compras": 2,
            "despesas": 1,

        }

        venda = Venda.objects.create(
            usuario_id=self.user.id,
            dia_da_venda=data['dia_da_venda'],
            quantidade_entregas=data['quantidade_entregas'],
            venda_dinheiro=data['venda_dinheiro'],
            venda_cartao=data['venda_cartao'],
            compras=data['compras'],
            despesas=data['despesas'],

        )

        data = VendaForm(self).data
        self.assertEqual(data["venda_total_dia"], 80)
'''

