from django.contrib.auth.models import User
from django.test import TestCase
from core.models import Venda
from core.forms import VendaForm


class VendaTestCase(TestCase):
#TODO: Falta o teste para somar dinheiro e cartão descontando 3% da venda do cartão

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
        """
        Teste para criar uma venda verificando se os dados não são None.
        """
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

    def test_sum_dinheiro_cartao(self):
        """
        Soma dinheiro com cartão
        """
        data = {
            "dia_da_venda": '2020-12-30',
            "quantidade_entregas": 10,
            "venda_dinheiro": 50,
            "venda_cartao": 30,
            "compras": 2,
            "despesas": 1,
        }

        venda = Venda.objects.create(
            dia_da_venda=data['dia_da_venda'],
            quantidade_entregas=data['quantidade_entregas'],
            venda_dinheiro=data['venda_dinheiro'],
            venda_cartao=data['venda_cartao'],
            compras=data['compras'],
            despesas=data['despesas'],
            venda_total_dia=data['venda_dinheiro'] + data['venda_cartao'],
        )

        total = venda.venda_total_dia

        self.assertEqual(total, 80)

    def test_sum_despesas(self):
        """
        Teste para somar as despesas
        """
        data = {
            "dia_da_venda": '2020-12-30',
            "quantidade_entregas": 10,
            "venda_dinheiro": 50,
            "venda_cartao": 30,
            "compras": 2,
            "despesas": 1,
        }

        venda = Venda.objects.create(
            dia_da_venda=data['dia_da_venda'],
            quantidade_entregas=data['quantidade_entregas'],
            venda_dinheiro=data['venda_dinheiro'],
            venda_cartao=data['venda_cartao'],
            compras=data['compras'],
            despesas=data['despesas'],
            venda_total_dia=data['venda_dinheiro'] + data['venda_cartao'],
            despesa_do_dia=data['compras'] + data['despesas'],
        )

        total = venda.despesa_do_dia

        self.assertEqual(total, 3)

    def test_sum_lucro_liquido(self):
        """
        Teste para retornar o valor liquido
        """
        data = {
            "dia_da_venda": '2020-12-30',
            "quantidade_entregas": 10,
            "venda_dinheiro": 50,
            "venda_cartao": 30,
            "compras": 2,
            "despesas": 1,


        }

        venda = Venda.objects.create(
            dia_da_venda=data['dia_da_venda'],
            quantidade_entregas=data['quantidade_entregas'],
            venda_dinheiro=data['venda_dinheiro'],
            venda_cartao=data['venda_cartao'],
            compras=data['compras'],
            despesas=data['despesas'],
            venda_total_dia=data['venda_dinheiro'] + data['venda_cartao'],
            despesa_do_dia=data['compras'] + data['despesas'],
            lucro_liquido_dia=((data['venda_dinheiro'] + data['venda_cartao']) -
                               data['compras'] + data['despesas']),
        )

        total = venda.lucro_liquido_dia
        self.assertEqual(total, 77)
