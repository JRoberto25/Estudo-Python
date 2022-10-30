"""
co = float(input('Digite o valor do cateto oposto em cm: '))
ca = float(input('Digite o valor do cateto adjacente em cm: '))
h = ((co**2) + (ca**2))**(1/2)
print('A hipotenusa mede {:.2f}cm'.format(h))
"""
from math import hypot
co = float(input('Digite o valor do cateto oposto em cm: '))
ca = float(input('Digite o valor do cateto adjacente em cm: '))
print('A hipotenusa mede {:.2f}cm'.format(hypot(co, ca)))
