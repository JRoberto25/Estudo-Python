n = e = int(input('Digite um número para calcular o fatorial: '))
f = 1
if n <= 0:
    print('Por favor, digite um número natural positivo')
else:
    while n > 1:
        f *= n
        n -= 1
print('O fatorial de {} é {}!'.format(e, f))
