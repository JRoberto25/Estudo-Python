
num = int(input('Digite um número: '))
sn = int(input('''Selecione uma base para conversão:
1 : binário
2 : octal
3 : hexadecimal
'''))
if sn == 1:
    print('O número {} em binário é: {}.'.format(num, bin(num)[2:]))
elif sn == 2:
    print('O número {} em octal é: {}.'.format(num, oct(num)[2:]))
elif sn == 3:
    print('O número {} em hexadecimal é: {}.'.format(num, hex(num)[2:]))
else:
    print('Valor inválido, tente novamente!')
