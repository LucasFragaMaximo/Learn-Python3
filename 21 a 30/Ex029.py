vel = int(input('Qual é a velocidade atual do carro: '))

if vel <= 80:
    print('tudo certo diriga com cuidado')

elif vel > 80:
    print('MULTADO! Você exedeu o limite permitido de 80Km/h')
    print(f'Você deve pagar uma MULTA de {(vel-80) * 7}')

print('Tenha um bom dia! Dirija com segurança!')