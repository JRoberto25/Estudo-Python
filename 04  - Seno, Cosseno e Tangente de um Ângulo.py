from math import sin, cos, tan, radians
ang = int(input('Digite um ângulo: '))
r = radians(ang)
print('O ângulo {}º tem seno: {:.2f}, cosseno: {:.2f} e tangente: {:.2f}'.format(ang, sin(r), cos(r), tan(r)))
