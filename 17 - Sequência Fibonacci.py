n = int(input('Quantos números da sequência Fibonatti você quer ver? '))
cont = 0
f1 = 0
f2 = 1
f3 = 0
print('{} -> {} -> '.format(f1, f2), end='')
f3 = f1 + f2
while cont < n - 2:
    print('{} -> '.format(f3), end='')
    f1 = f3
    f3 = f1 + f2
    f2 = f1

    cont += 1
print('Fim')
