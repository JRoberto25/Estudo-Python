listajogadores = list()
listagols = list()
dadosjogador = {}
partidas = escolha = 0
continuar = 's'

while continuar not in 'Nn':
    dadosjogador['Nome'] = input('Nome do Jogador: ')
    partidas = int(input(f'Quantas partidas {dadosjogador["Nome"]} jogou? '))
    for x in range(1, partidas + 1):
        listagols.append(int(input(f'   Quantos gols na partida {x}: ')))
    dadosjogador['Gols'] = listagols.copy()
    dadosjogador['Total'] = sum(listagols)
    listagols.clear()
    continuar = input('Você quer continuar? [S/N]')
    listajogadores.append(dadosjogador.copy())


print('-='*25)
print('cód. ', end='')
for i in dadosjogador.keys():
    print(f'{i:<14} ', end='')
print()
print('-' * 50)
for k, v in enumerate(listajogadores):
    print(f'{k:>2}   ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*25)

while True:
    escolha = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    print('-=' * 25)
    if escolha == 999:
        break
    elif escolha >= len(listajogadores):
        print('-=' * 25)
        print(f'Jogador de código {escolha} não encontrado!')
        print('-=' * 25)
    else:
        print(f'Mostrando dados do Jogador {listajogadores[escolha]["Nome"]}:')
        for i, v in enumerate(listajogadores[escolha]['Gols']):
            print(f'No jogo {i + 1} ele fez {v} Gols')
        print('-=' * 25)
