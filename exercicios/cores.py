####Dicionario de cores em ingles

cores={'azul': 'blue', 'vermelho': 'red', 'preto': 'black', 'amarelo': 'yellow'}

cor=input('Digite o nome de uma cor em português para traducao em ingles: ').lower()
resultado=cores.get(cor,'Esta cor não se encontra no dicionario!')

print(resultado)
