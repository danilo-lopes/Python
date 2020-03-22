from programa import Programa

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao
    
    @property
    def duracao(self):
        return self.__duracao

    # Representação Textual da Classe
    def __str__(self):
        return f'Nome {self.nome} - Ano {self.ano} - Duracao {self.__duracao} - Likes {self.likes}'
