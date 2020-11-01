dis = float(input('Qual é a distancia da sua viagem? '))

print(f'Você está prestes a iniciar uma viagem de {dis} kilometros. ')

if dis <= 200:
    pay = dis * 0.50
    print(f'O valor total será R${pay}')
else:
    pay1 = dis * 0.45
    print(f'O valor total será R${pay1}')
