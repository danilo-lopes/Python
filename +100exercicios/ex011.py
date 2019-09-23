# Faça um programa que leia a altura e a largura de uma parede em metros
# Calcule a sua área e a quantidade de tintas necessária para pintá-la.
# Sabendo que cada litro de tinta, pinta uma área de 2m²

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

area = larg * alt
tinta = area / 2

print('Sua parede tem a dimensão de: {}x{} e sua área é de: {}m²'.format(larg, alt, area))
print('Para pintar essa parede você precisará de: {}l de tinta'.format(tinta))
