from programa import Programa

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas

    @property
    def temporadas(self):
        return self.__temporadas

    @temporadas.setter
    def temporadas(self, novaTemporada):
        self.__temporadas += novaTemporada

    # Representação Textual da Classe
    def __str__(self):
        return f'Nome {self.nome} - Ano {self.ano} - Temporadas {self.__temporadas} - Likes {self.likes}'
