tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    n = int(input('Digite um número entre 0 e 10: '))
    if 0 <= n <= 10:
        break
print(f'Você digitou o número {tupla[n]}')
