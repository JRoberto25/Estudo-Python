from random import randint
escolha = int(randint(1, 10))
print('Olá sou seu computador...')
print('Acabei de pensar em um número, tente adivinhá-lo! ')
acertou = False
cont = 0
while not acertou:
    cont += 1
    n = int(input('Diga seu {}º palpite: '.format(cont)))
    if escolha == n:
        acertou = True
        print('Você acertou e precisou de {} palpites para isso!'.format(cont))
    elif n > escolha:
        print('Menor... tente novamente!')
    elif n < escolha:
        print('Maior... tente novamente!')

