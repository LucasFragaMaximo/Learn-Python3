print('C = celsius e F = fahrenheit e K = Kelvin')
temp = str(input('Informe qual temperatura: '))

if temp == 'C' or temp == 'c':
    cel = float(input('Informe a temperatura: '))
    fcel = (cel * 9/5)+ 32
    kcel = cel + 273.15
    print(f'São Fahrenheit {fcel:.2f}°F.')
    print('São Kelvins {:.2f}K.'.format(kcel))

elif temp == 'F' or temp == 'f':
    fah = float(input('Informe a temperatura: '))
    cfah = (fah - 32)* 5/9
    kfah = (fah - 32)* 5/9 + 273.15
    print('São Celsius {:.2f}°C.'.format(cfah))
    print('São Kelvins {:.2f}K.'.format(kfah))

elif temp == 'K' or temp == 'k':
    kel = float(input('Informe a temperatura: '))
    ckel = kel - 273.15
    fkel = (ckel - 273.15)* 9/5 + 32
    print('São Celsius {:.2f}°C.'.format(ckel))
    print('São Fahrenheit {:.2f}°F.'.format(fkel))