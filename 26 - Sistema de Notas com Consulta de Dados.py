listatemporaria = list()
notasalunos = list()
numeroaluno = 0
while True:
    listatemporaria.append(input('Nome: '))
    listatemporaria.append(int(input('Nota 1: ')))
    listatemporaria.append(int(input('Nota 2: ')))
    listatemporaria.append(float((listatemporaria[1] + listatemporaria[2]) / 2))
    notasalunos.append(listatemporaria[:])
    listatemporaria.clear()
    escolha = input('Você quer continuar? [S/N] ')
    if escolha in 'Nn':
        break
        
print(f'{"Nº":<4} {"Aluno":<10} {"Média":>4}')
print('-'*20)
for i, n in enumerate(notasalunos):
    print(f'{i:<4}{notasalunos[i][0]:<10}{notasalunos[i][3]:>4}')

while True:
    numeroaluno = int(input('Mostrar notas de qual aluno(Nº)? (999 interrompe) '))
    if numeroaluno == 999:
        print('Finalizando...')
        print('Volte sempre!')
        break
    else:
        print(f'As notas do aluno {notasalunos[numeroaluno] [0]} foram '
              f'{notasalunos[numeroaluno] [1]} e {notasalunos[numeroaluno] [2]}')
