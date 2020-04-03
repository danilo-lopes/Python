from src.app_leilao.leilao import Leilao
from src.app_leilao.lance import Lance
from src.app_leilao.excessao_leilao import LanceInvalido


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self._carteira = carteira

    def propoe_lance(self, leilao: Leilao, valor):
        if not self._valor_valido(valor):
            raise LanceInvalido('Não pode propor um lance maior do que o valor da carteira')

        lance = Lance(self, valor)
        leilao.propoe(lance)

        self._carteira -= valor

    def _valor_valido(self, valor):
        return valor <= self.carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self._carteira
