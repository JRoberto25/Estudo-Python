m1 = float(input('Digite a medida de um lado do triângulo: '))
m2 = float(input('Digite a medida do outro lado do triângulo: '))
m3 = float(input('Digite a medida do outro lado do triângulo: '))

if m1 < m2 + m3 and m2 < m1 + m3 and m3 < m2 + m1:
    if m1 == m2 == m3:
        print('Essas medidas formam um triângulo equilátero.')
    elif m1 == m2 != m3 and m1 == m3 != m2 and m2 == m3 != m1:
        print('Essas medidas formam um triângulo isóceles.')
    elif m1 != m2 != m3:
        print('Essas medidas formam um triângulo escaleno.')
else:
    print('Essas medidas não podem formar um triângulo.')
