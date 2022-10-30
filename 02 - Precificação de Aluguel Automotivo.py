d = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos quilometros você andou com o carro? '))
v = d * 60 + km * 0.15
print('Você deverá pagar R${:.2f} pelo aluguel do carro.'.format(v))
