sala = float(input('Qual é o salário do funcionário? R$ '))
aument = sala*15/100

print('Um funcionário que ganhava R${:.2f}, com o aumento de 15%, passa a receber R${:.2f}.'.format(sala, sala+aument))