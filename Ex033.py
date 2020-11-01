num1 = float(input('Primeiro Número: '))
num2 = float(input('Segundo Número: '))
num3 = float(input('Terceiro Número: '))
#Menor
menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3
#Maior
maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3
print(f'O menor número foi {menor}.')
print(f'O maior número foi {maior}.')
