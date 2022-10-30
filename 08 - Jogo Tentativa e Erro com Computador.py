from random import choice
from time import sleep
x = int(input('Tente acertar em qual número eu estou pensando de 1 a 5: '))
print('PROCESSANDO')
sleep(2)
if 0 < x < 6:
    escolhas = [1, 2, 3, 4, 5]
    numverd = int(choice(escolhas))
    if numverd == x:
        print('PARABÉNS, você acertou!!!')
    else:
        print('Dessa vez eu ganhei, eu havia escolhido o número {}.'.format(numverd))
else:
    print('Este número não pode ser escolhido, tente novamente.')
