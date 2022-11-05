from random import randint
valores = list()
for x in range(0, 5):
    valores.append(randint(0, 50))


def sorteio():
    print('Sorteando 5 valores:', end=' ')
    for n in range(0, 5):
        print(valores[n], end=' ')
    print('Pronto!')


def pares():
    par = 0
    sorteio()
    for v in valores:
        if v % 2 == 0:
            par += v
    print(f'Somando os valores pares {valores}, temos: {par}')


pares()
