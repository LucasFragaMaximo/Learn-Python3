preco = float(input('Qual é o preço do produto ?\n '))
por = preco*5/100
print('O produto no preço de {:.2f} com o desconto de 5% sai {:.2f}'.format(preco, preco-por))