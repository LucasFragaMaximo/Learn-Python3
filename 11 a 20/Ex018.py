from math import cos, tan, sin, radians
ang = float(input('Digite o angulo que você deseja: '))
print('O ângulo de {} tem a SENO de {:.2f}'.format(ang, sin(radians(ang))))
print('O ângulo de {} tem a COSSENO de {:.2f}'.format(ang, cos(radians(ang))))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan(radians(ang))))