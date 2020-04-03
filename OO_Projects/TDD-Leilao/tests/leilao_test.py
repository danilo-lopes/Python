from unittest import TestCase
from src.app_leilao.usuario import Usuario
from src.app_leilao.lance import Lance
from src.app_leilao.leilao import Leilao
from src.app_leilao.excessao_leilao import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):

        self.danilo = Usuario('Danilo', 500)
        self.joao = Usuario('Joao', 500)
        self.pedro = Usuario('Pedro', 500)

        self.lance_joao = Lance(self.joao, 2500)
        self.lance_danilo = Lance(self.danilo, 1500)
        self.lance_pedro = Lance(self.pedro, 100)

        self.leilao = Leilao('Xiaomi Mi10 Pro')

    def test_OrdemCrescente(self):

        lancamentos_leilao = [self.lance_pedro, self.lance_danilo, self.lance_joao]
        
        [self.leilao.propoe(lance) for lance in lancamentos_leilao]

        menor_lance_esperado = 100
        maior_lance_esperado = 2500

        self.assertEqual(menor_lance_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_lance_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_lance_em_ordem_decrescente(self):
        self.leilao.propoe(self.lance_joao)

        with self.assertRaises(LanceInvalido):
            marinalva = Usuario('marinalva', 500)
            lance_marinalva = Lance(marinalva, 50)

            self.leilao.propoe(lance_marinalva)

    def test_UnicoUsuario(self):
        josias = Usuario('Josias', 500)

        lance_josias = Lance(josias, 4000)

        self.leilao = Leilao('Iphone The Best 40')

        self.leilao.propoe(lance_josias)

        menor_lance_esperado = 4000

        self.assertEqual(menor_lance_esperado, self.leilao.menor_lance)

    def test_deve_permitir_lances_caso_leilao_nao_tenha_lances(self):
        moises = Usuario('moises', 500)
        lance_moises = Lance(moises, 2000)

        self.leilao.propoe(lance_moises)

        quantidadeLances = len(self.leilao.lances)

        self.assertEqual(1, quantidadeLances)

    def test_deve_permitir_lance_caso_ultimo_usuario_seja_diferente(self):
        carol = Usuario('carol', 500)
        lance_carol = Lance(carol, 200)

        self.leilao.propoe(lance_carol)
        self.leilao.propoe(self.lance_joao)

        quantidadeLances = len(self.leilao.lances)

        self.assertEqual(2, quantidadeLances)

    def test_deve_nao_deve_permitir_lance_do_mesmo_usuario(self):
        lance_200_joao = Lance(self.joao, 3000)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_joao)
            self.leilao.propoe(lance_200_joao)
