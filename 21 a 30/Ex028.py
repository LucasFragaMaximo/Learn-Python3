import random

num = random.randint(0, 5)
print('-=-'*19)
print('Em um número de 0 a 5...')
print('-=-'*19)
num2 = int(input('Advinhe o número que estou pensando: '))

if num2 == num:
    print('Parabéns você acertou!!')

else:
    print(f'Errou era {num}, tente novamente!!')
