from time import sleep
c = ('\033[m',         #0, sem cores.
     '\033[0;30;41m',  #1, vermelho.
     '\033[0;30;42m',  #2, verde.
     '\033[0;30;43m',  #3, amarelo.
     '\033[0;30;44m',  #4, azul.
     '\033[0;30;45m',  #5, roxo.
     '\033[1;97;7m'    #6, branco.
)


def pyhelp(msg):
    titulo(f'Acessando manual do comando {fun}', 4)
    print(c[6])
    help(msg)
    print(c[0])
    sleep(2)


def titulo(msg, cor=0):
    print(c[cor])
    tam = len(msg)
    print('~' * (tam + 4))
    print(' ', msg)
    print('~' * (tam + 4))
    print(c[0])
    sleep(1)


while True:
    titulo('Sistema de ajuda PyHelp', 2)
    fun = input('Função ou Biblioteca (Digite "FIM" para sair)> ')
    if fun.upper() == "FIM":
        break
    pyhelp(fun)
titulo('Até logo', 1)


