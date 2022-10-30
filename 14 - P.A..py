print('Programa de Progressão Aritmética')
print('Informe o primeiro termo e a razão da PA que lhe retornarei os 10 primeiros números.')
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
d = pt + (10 - 1) * r
for c in range(pt, d + r, r):
    print('{}'.format(c), end=' -> ')
print('FIM')
