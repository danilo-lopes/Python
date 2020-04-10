import pytest
from src.app_leilao.usuario import Usuario
from src.app_leilao.leilao import Leilao
from src.app_leilao.lance import Lance
from src.app_leilao.excessao_leilao import LanceInvalido


@pytest.fixture
def joao():
    return Usuario('Joao', 500)


@pytest.fixture
def danilo():
    return Usuario('Danilo', 500)


@pytest.fixture
def pedro():
    return Usuario('Pedro', 500)


@pytest.fixture
def leilao():
    return Leilao('Xiaomi Mi10 Pro')


def test_deve_permitir_lance_em_ordem_crescente(pedro, danilo, joao, leilao):
    lance_pedro = Lance(pedro, 100)
    lance_danilo = Lance(danilo, 50)
    lance_joao = Lance(joao, 10)

    lancamentos_leilao = [lance_joao, lance_danilo, lance_pedro]

    [leilao.propoe(lance) for lance in lancamentos_leilao]

    menor_lance_esperado = 10
    maior_lance_esperado = 100

    assert menor_lance_esperado == leilao.menor_lance
    assert maior_lance_esperado == leilao.maior_lance


def test_nao_deve_permitir_lance_em_ordem_decrescente(joao, leilao):
    lance_joao = Lance(joao, 100)
    leilao.propoe(lance_joao)

    with pytest.raises(LanceInvalido):
        marinalva = Usuario('marinalva', 500)
        lance_marinalva = Lance(marinalva, 50)

        leilao.propoe(lance_marinalva)


def test_deve_permitir_unico_lance_de_um_usuario(leilao):
    josias = Usuario('Josias', 500)

    lance_josias = Lance(josias, 4000)

    leilao.propoe(lance_josias)

    menor_lance_esperado = 4000

    assert menor_lance_esperado == leilao.menor_lance


def test_deve_permitir_lances_caso_leilao_nao_tenha_lances(leilao):
    moises = Usuario('moises', 500)
    lance_moises = Lance(moises, 2000)

    leilao.propoe(lance_moises)

    quantidadeLances = len(leilao.lances)

    assert 1 == quantidadeLances


def test_deve_permitir_lance_caso_ultimo_usuario_seja_diferente(leilao):
    carol = Usuario('carol', 500)
    lance_carol = Lance(carol, 200)

    lance_joao = Lance(joao, 300)

    leilao.propoe(lance_carol)
    leilao.propoe(lance_joao)

    quantidadeLances = len(leilao.lances)

    assert 2 == quantidadeLances


def test_deve_nao_deve_permitir_lance_do_mesmo_usuario(joao, leilao):
    lance_joao = Lance(joao, 100)
    lance_200_joao = Lance(joao, 200)

    with pytest.raises(LanceInvalido):
        leilao.propoe(lance_joao)
        leilao.propoe(lance_200_joao)
