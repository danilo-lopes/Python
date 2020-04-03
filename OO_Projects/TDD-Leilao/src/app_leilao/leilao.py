from src.app_leilao.lance import Lance
from src.app_leilao.excessao_leilao import LanceInvalido


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    @property
    def lances(self):
        return self.__lances[:]

    def propoe(self, lance: Lance):
        if self._lance_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor

            self.__lances.append(lance)

    def _tem_lances(self):
        return self.__lances

    def _usuario_diferentes(self, lance: Lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido('O mesmo usuario não é permitido')

    def _valor_maior_lance_anterior(self, lance: Lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido('O valor do lance tem que ser maior do que o anterior')

    def _lance_valido(self, lance):
        return not self._tem_lances() or self._usuario_diferentes(lance) and self._valor_maior_lance_anterior(lance)
