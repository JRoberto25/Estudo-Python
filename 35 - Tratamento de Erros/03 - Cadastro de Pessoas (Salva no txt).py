def arquivoExiste(msg):
    try:
        a = open(msg, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(msg):
    try:
        a = open(msg, 'wt+')
        a.close()
    except:
        print('Houve um erro!')
    else:
        print(f'Arquivo {msg} criado!')


def lerArquivo(msg):
    try:
        a = open(msg, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<20}{dado[1]:>3} anos')
        a.close()


def adicionaPessoa(msg, nomepessoa = 'desconhecido', idadepessoa = 0):
    try:
        a = open(msg, 'at')
    except:
        print('Erro, tente novamente!')
    else:
        try:
            a.write(f'{nomepessoa};{idadepessoa}\n')
        except:
            print('Erro em adicionar dados')
        else:
            print(f'{nome} adicionado com sucesso')
            a.close()


from time import sleep

arq = 'teste.txt'
arquivoExiste(arq)

if arquivoExiste(arq) is False:
    criarArquivo(arq)

while True:
    print('-' * 30)
    print('MENU PRINCIPAL'.center(30))
    print('-' * 30)
    print('1 - Ver pessoas cadastradas.\n'
          '2 - Cadastrar nova pessoa.\n'
          '3 - Sair do sistema.')
    print('-' * 30)
    sleep(0.5)
    try:
        escolha = int(input(f'Sua opção: '))
        print('-' * 30)
    except:
       print('Erro! Digite um número válido!')
    else:
        sleep(0.5)
        if escolha == 1:
            print('-'*30)
            print('Pessoas Cadastradas')
            print('-' * 30)
            sleep(0.25)
            lerArquivo(arq)
            sleep(1)
        elif escolha == 2:
            sleep(0.5)
            print('-' * 30)
            print('Novo Cadastro'.center(30))
            print('-' * 30)
            nome = input('Digite o nome da pessoa: ')
            idade = int(input('Digite a idade: '))
            adicionaPessoa(arq, nome, idade)
        elif escolha == 3:
            sleep(0.2)
            print('-' * 30)
            print('Encerrando... Até logo!'.center(30))
            print('-' * 30)
            sleep(0.5)
            break
        else:
            sleep(0.5)
            print('Erro! Digite um número válido!')

