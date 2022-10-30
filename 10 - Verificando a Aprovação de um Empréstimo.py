#O empréstimo só será aceito se 30% de sua renda mensal for maior que a parcela definida.
vc = int(input('Digite o valor da casa: '))
sc = int(input('Digite quanto você ganha: '))
an = int(input('Em quantos anos você quer pagar? '))
if (vc/(an * 12)) < (sc * 0.3):
    print('Seu empréstimo foi aprovado!')
else:
    print('Seu empréstimo não pode ser aprovado!')
