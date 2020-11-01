fras = input('Digite uma frase: ').strip()
frase = fras.lower()
a = frase.count('a')
a1 = frase.find('a')+1
a2 = frase.rfind('a')+1
print('A letra A aparece {} vezes na frase.'.format(a))
print('A primeira letra A apareceu na posição {}'.format(a1))
print('A primeira letra A apareceu na posição {}'.format(a2))