largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = float(largura * altura)
print('Sua parede tem a dimensão de {}x{} e sua área é {}m².'.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede você precisará de {}l de tinta.'.format(tinta))