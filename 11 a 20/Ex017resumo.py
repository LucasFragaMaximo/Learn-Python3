from math import hypot
cat1 = float(input('Comprimento do cateto oposto: '))
cat2 = float(input('Comprimento do cateto adjacente: '))
hip = float(hypot(cat1, cat2))
print('A hipotenusa vai medir: {:.2f}'.format(hip))