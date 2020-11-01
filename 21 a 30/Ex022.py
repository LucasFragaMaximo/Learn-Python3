nom = input('Digite seu nome completo: ')
nome = nom.strip()
pnome = nome.split()

print('Analisando o nome . . .')
print('Seu nome em maiúsculo é {}.'.format(nome.upper()))
print('Seu nome em minúsculo é {}.'.format(nome.lower()))
print('Seu nome tem {} letras no total.'.format(len(nome)))
print('Seu primeiro nome tem {} letras.'.format(len(pnome[0])))