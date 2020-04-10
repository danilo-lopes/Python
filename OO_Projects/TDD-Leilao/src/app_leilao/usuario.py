from src.app_leilao.leilao import Leilao
from src.app_leilao.lance import Lance
from src.app_leilao.excessao_leilao import LanceInvalido
from src.app_leilao.excessao_leilao import CarteiraInvalida


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome

        if carteira <= 0:
            raise CarteiraInvalida('O usuario não pode iniciar com a sua carteira vazia')

        else:
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

    def meusLances(self, leilao: Leilao):
        lancesLeilao = leilao.lances

        for lance in lancesLeilao:
            if lance.usuario == self:
                return lance.valor
