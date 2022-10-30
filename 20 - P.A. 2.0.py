primeiro = int(input('Vamos calcular uma P.A.\nDigite o primeiro número: '))
razao = int(input('Digite a razão: '))
vezes = 0
cont = 0
repeticao = 10
while vezes < repeticao:
    print('{} -> '.format(primeiro), end='')
    primeiro += razao
    vezes += 1
    if vezes == repeticao:
        print('Pausa')
        repeticao = int(input('Quantos termos você quer que sejam exibidos a mais? '))
        vezes = 0
    cont += 1
print('Ao todo, foram exibidos {} termos.'.format(cont))
