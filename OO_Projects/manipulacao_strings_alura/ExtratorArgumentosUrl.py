class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.urlEhValida(url):
            self.url = url

        else:
            raise LookupError('URL não é valida!')
    
    @staticmethod
    def urlEhValida(url):
        if url:
            return True
        else:
            return False

    def extraiArgumentos(self):

        buscaMoedaOrigem = "moedaorigem="
        buscaMoedaDestino = "moedadestino="

        indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find(buscaMoedaDestino) - 1

        indiceInicialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)
        indiceFinalMoedaDestino = self.url.find("valor") - 1

        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]
        moedaDestino = self.url[indiceInicialMoedaDestino:indiceFinalMoedaDestino]

        return moedaOrigem, moedaDestino

    def encontraIndiceInicial(self, moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada)
