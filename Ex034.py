sal = float(input('Qual o salário do funcionário. R$'))
if sal > 1250:
    sal1 = sal + sal*10/100
else:
    sal1 = sal + sal*15/100

print(f'Quem ganhava R${sal} passará a ganhar R${sal1}.')