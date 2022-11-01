num = []
pares = []
impares = []
fim = 's'
cont = 0
while fim != 'n':

    num.append(int(input('Digite um número: ')))
    fim = str(input('Você quer continuar?[S/N] ').lower())

    print(f'O número {num[cont]} foi adicionado na {cont + 1}º posição...')
    cont = cont + 1


for indice, valor in enumerate(num):
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(f'''A lista completa é {num}
A lista dos pares é {pares}
A lista dos ímpares é {impares}''')
