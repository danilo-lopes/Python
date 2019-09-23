# Em um proggrama, crie uma tupla para guardar os meses do ano


meses=('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio',
'Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')

data_nasc = input('Digite sua data de nascimento no formato DD-MM-AA: ')
indice = int(data_nasc[3:5])-1
resultado = meses[indice]

print('Você nasceu no mês de', resultado)
