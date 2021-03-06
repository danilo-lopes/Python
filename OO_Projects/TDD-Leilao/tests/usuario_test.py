import pytest
from src.app_leilao.usuario import Usuario
from src.app_leilao.leilao import Leilao
from src.app_leilao.excessao_leilao import LanceInvalido
from src.app_leilao.excessao_leilao import CarteiraInvalida


@pytest.fixture
def vinicius():
    return Usuario('Vinicius', 100)


@pytest.fixture
def pedro():
    return Usuario('Pedro', 100)


@pytest.fixture
def leilao():
    return Leilao('Celular')


def test_deve_subtrair_valor_carteira_usuario_em_lance(vinicius, leilao):
    vinicius.propoe_lance(leilao, 50.0)

    assert vinicius.carteira == 50.0


def test_deve_permitir_lance_valor_for_menor_que_valor_carteira(vinicius, leilao):
    vinicius.propoe_lance(leilao, 1.0)

    assert vinicius.carteira == 99.0


def test_deve_permitir_lance_valor_e_igual_valor_carteira(vinicius, leilao):
    vinicius.propoe_lance(leilao, 100)

    assert vinicius.carteira == 0


def test_nao_deve_permitir_lance_valor_maior_valor_carteira(vinicius, leilao):
    with pytest.raises(LanceInvalido):

        vinicius.propoe_lance(leilao, 200)


def test_nao_deve_permitir_usuario_iniciar_com_carteira_vazia():
    with pytest.raises(CarteiraInvalida):

        zezinho = Usuario('zezinho', 0)


def test_deve_permitir_usuario_visualizar_seus_lances(vinicius, leilao):
    vinicius.propoe_lance(leilao, 10)

    assert vinicius.meusLances(leilao)


def test_deve_garantir_que_lances_dados_do_usuario_sao_os_lances_dele(vinicius, pedro, leilao):
    vinicius.propoe_lance(leilao, 10)
    valorLanceVinicius = 10

    assert vinicius.meusLances(leilao) == valorLanceVinicius
