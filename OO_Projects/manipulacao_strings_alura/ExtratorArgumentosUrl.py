# https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=700

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
        moedasAceitas = ["real", "dolar"]

        indiceInicialMoedaOrigem = self.encontraIndiceInicial("moedaorigem=")
        indiceFinalMoedaOrigem = self.url.find("&")

        indiceInicialMoedaDestino = self.encontraIndiceInicial("moedadestino=")
        indiceFinalMoedaDestino = self.url.find("&", indiceFinalMoedaOrigem + 1)

        indiceValorInicial = self.encontraIndiceInicial("valor=")

        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        if moedaOrigem not in moedasAceitas:
            raise LookupError(f"Valor {moedaOrigem} não é válido!")

        moedaDestino = self.url[indiceInicialMoedaDestino:indiceFinalMoedaDestino]

        if moedaDestino not in moedasAceitas:
            raise LookupError(f"Valor {moedaDestino} não é válido!")
        
        valor = self.url[indiceValorInicial:]

        return moedaOrigem, moedaDestino, valor

    def encontraIndiceInicial(self, moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada)
