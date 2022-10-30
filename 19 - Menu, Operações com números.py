from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
sleep(0.5)
print('-' * 30)
sleep(0.5)
acao = 0
while acao != 5:
    acao = int(input('O que você quer fazer com esses números? \n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS VALORES\n[5] SAIR\n'))
    sleep(0.8)
    if acao == 1:
        s = n1 + n2
        print('A soma dos valores {} e {} é {}'.format(n1, n2, s))
    elif acao == 2:
        m = n1 * n2
        print('O produto de {} e {} é {}'.format(n1, n2, m))
    elif acao == 3:
        if n1 > n2:
            print('O valor {} é maior'.format(n1))
        elif n2 > n1:
            print('O valor {} é maior'.format(n2))
        else:
            print('Os valores são iguais')
    elif acao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif acao == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Valor inválido, tente novamente')
        sleep(0.3)
    sleep(0.5)
    print('-' * 30)
    sleep(0.5)

print('Obrigado, volte sempre!')