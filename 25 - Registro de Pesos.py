pessoas = []
dados = []
nomesp = []
nomesl = []
escolha = 's'
cont = pesados = leves = 0
while escolha not in 'Nn':
    pessoas.append(input('Digite o nome de uma pessoa: '))
    pessoas.append(int(input('Digite o peso dela: ')))
    dados.append(pessoas[:])
    pessoas.clear()
    cont += 1
    escolha = input('Você quer continuar? [S/N]')
for n in range(len(dados)):
    if n == 0:
        pesados = leves = dados[n][1]
        nomesp.append(dados[n][0])
        nomesl.append(dados[n][0])
    else:
        if dados[n][1] > pesados:
            nomesp.clear()
            nomesp.append(dados[n][0])
            pesados = dados[n][1]
        elif dados[n][1] == pesados:
            nomesp.append(dados[n][0])
        if dados[n][1] < leves:
            nomesl.clear()
            nomesl.append(dados[n][0])
            leves = dados[n][1]
        elif dados[n][1] == leves:
            nomesl.append(dados[n][0])
print(f'Ao todo, foram cadastradas {cont} pessoas')

print(f'O maior peso foi {pesados} Kg. O peso foi de ', end='')
for i, m in enumerate(nomesp):
    if i < len(nomesp) - 1:
        print(nomesp[i], end=', ')
    else:
        print(nomesp[i], end='.')
print(f'\nO menor peso foi {leves} Kg. O peso foi de ', end='')
for i, m in enumerate(nomesl):
    if i < len(nomesl) - 1:
        print(nomesl[i], end=', ')
    else:
        print(nomesl[i], end='.')
