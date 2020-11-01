print('-=-'*8)
print('Analizador de triângulos')
print('-=-'*8)
seg1 = float(input('Primeiro Segmento: '))
seg2 = float(input('Segundo Segmento: '))
seg3 = float(input('Terceiro Segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos acima PODEM FORMAR triangulos.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triangulos.')
