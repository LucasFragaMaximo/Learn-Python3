cat1 = float(input('Comprimento do cateto oposto: '))
cat2 = float(input('Comprimento do cateto adjacente: '))
hip = (cat1 ** 2 + cat2 ** 2) ** 0.5
print('A hipotenusa vai medir: {:.2f}'.format(hip))
