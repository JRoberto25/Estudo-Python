pessoas = dict()
listapessoas = list()
mulheres = list()
cont = media = 0
fim = ''
while True:
    pessoas['Nome'] = input('Nome: ')
    sexo = input('Sexo: [M/F]').lower()
    while sexo not in 'mf':
        print('Erro! Digite apenas M ou F!')
        sexo = input('Sexo: [M/F]').lower()
    if sexo in 'Ff':
        mulheres.append(pessoas.copy())
    pessoas['Sexo'] = sexo
    Idade = int(input('Idade: '))
    media += Idade
    pessoas['Idade'] = Idade
    cont += 1
    listapessoas.append(pessoas.copy())
    fim = input('Você quer continuar? [S/N] ').lower()
    while fim not in 'sn':
        print('Erro! Digite apenas S ou N')
        fim = input('Você quer continuar? [S/N] ').lower()
    if fim == 'n':
        break
media = media/cont
print(f'Ao todo {cont} pessoas foram cadastradas.')
print(f'A média de idade é de {media:5.2f}.')
print(f'As mulheres cadastradas foram: ', end='')
for m in mulheres:
    print(m['Nome'], end=' ')
print(f'\nAs pessoas com idade acima da média foram: ')
cont = 0
for n in listapessoas:
    if n['Idade'] > media:
        print(f'Nome: {n["Nome"]}; Sexo: {n["Sexo"]}; Idade: {n["Idade"]}')
