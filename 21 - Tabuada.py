cont = 0
while True:
    n = int(input('Você quer ver a tabuada de qual número? '))
    if n < 0:
        break
    while True:
        cont += 1
        print(f'{cont} x {n} = {(n * cont)}')
        if cont == 10:
            cont = 0
            break
print('O programa acabou, muito obrigado!')
