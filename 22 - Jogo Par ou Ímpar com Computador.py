from random import randint
from time import sleep
print('Vamos jogar!')
while True:
    computador = randint(1, 10)
    parimpar = str(input('Escolha entre par ou ímpar [P/I]: ').lower())
    if parimpar == 'i':
        break
    elif parimpar == 'p':
        break
    print('Acho que você não entendeu, escolha "P" para par e "I" para ímpar, tente novamente')
sleep(0.3)
escolha = int(input('Muito bem, agora escolha um número: '))
sleep(0.5)
vencedor = resultadoip = 'p'
vitorias = 0
while True:
    if escolha < 0:
        print('Ei, você está tentando trapacear!')
    elif escolha > 10:
        print('Ei, você não tem mais que 10 dedos, jogue limpo!')
    else:
        resultado = (escolha + computador) % 2
        if resultado == 0:
            vencedor = 'p'
            resultadoip = 'par'
        else:
            vencedor = 'i'
            resultadoip = 'ímpar'
    if vencedor == parimpar:
        print('3...')
        sleep(0.5)
        print('2...')
        sleep(0.5)
        print('1... Já!')
        sleep(0.5)
        print(f'Você escolheu {escolha} e o computador escolheu {computador}')
        print(f'Deu {resultadoip}! você ganhou dessa vez.')
    else:
        print('3...')
        sleep(0.5)
        print('2...')
        sleep(0.5)
        print('1... Já!')
        sleep(0.5)
        print(f'Você escolheu {escolha} e o computador escolheu {computador}\nDeu {resultadoip}! você perdeu.')
        print(f'Número de vitórias: {vitorias}')
        break
    vitorias += 1
    sleep(0.7)
    print('Vamos tentar novamente...')
    while True:
        computador = randint(1, 10)
        parimpar = str(input('Escolha entre par ou ímpar [P/I]: ').lower())
        if parimpar == 'i':
            break
        elif parimpar == 'p':
            break
        print('Acho que você não entendeu, escolha "P" para par e "I" para ímpar, tente novamente')
    sleep(0.3)
    escolha = int(input('Agora escolha o número: '))
    sleep(0.5)
