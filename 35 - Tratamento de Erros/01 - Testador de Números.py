def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro: Digite um número válido.')
            continue
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except:
            print('Erro: Digite um número inteiro válido.')
        else:
            return n


num = leiaint('Digite um número inteiro: ')
num2 = leiafloat('Digite um número real: ')
print(f'Os números digitados foram: {num} e {num2}')
