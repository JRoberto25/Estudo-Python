from math import floor
print('{:=^40}'.format(' Lojas Roberto '))
valor = float(input('Digite o valor da compra: '))
metodo = int(input('''Selecione o método de pagamento:
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão
'''))

if metodo == 1:
    print('Com desconto de 10%, o valor total é de: R$', floor(valor * 0.9))
elif metodo ==2:
    print('Com desconto de 5%, o valor total é de: R$', floor(valor * 0.95))
elif metodo == 3:
    print('O valor sem juros é de: R$', valor)
elif metodo == 4:
    print('O valor total com juros de 20% é de: R$', floor(valor * 1.2))
else:
    print('Método invávido')
