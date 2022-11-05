from time import sleep


def cont(ini, fim, raz):
    sleep(0.4)
    print(f'Números de {ini} a {fim} de {abs(raz)} em {abs(raz)}.')
    if fim > ini:
        if raz < 0:
            raz *= -1
        elif raz == 0:
            raz = 1

    elif fim < ini:
        if raz > 0:
            raz *= -1
            fim += raz
        elif raz == 0:
            raz = 1
        else:
            fim += raz

    sleep(1.4)
    for n in range(ini, fim + 1, raz):
        print(n, end=' ')
        sleep(0.4)
    print()


cont(1, 10, 1)
cont(10, 0, 2)
sleep(0.4)
print('Agora é sua vez de personalizar os números!')
sleep(1.4)
i = int(input('Digite o número inicial: '))
f = int(input('Digite o número final: '))
r = int(input('Digite a razão: '))
cont(i, f, r)
