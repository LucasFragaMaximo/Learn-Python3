nome = input('Digite seu nome completo: ').strip()
name = nome.split()

print(f'prazer em te conhecer {nome}')
print(f'Seu primeiro nome é {name[0]}')
print(f'Seu último nome é {name[len(name)-1]}')
