from random import choice
from time import sleep
computador = int(choice([1, 2, 3, 4, 5]))
escolha = int(input('''Vamos jogar Pedra, Papel, Tesoura, Lagarto, Spock, escolha sua arma:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
[ 4 ] Lagarto
[ 5 ] Spock
'''))

if escolha == 1:
    sleep(0.5)
    print('Vamos lá!')
    sleep(1)
    print('Pedra...')
    sleep(0.5)
    print('Papel...')
    sleep(0.5)
    print('Tesoura...')
    sleep(0.5)
    print('Lagarto, Spock!')
    sleep(1)
    if computador == 1:
        print('Eu também escolhi Pedra, deu empate! :/')
    elif computador == 2:
        print('Eu escolhi Papel hehehe, o Papel embrulha a Pedra, eu venci! :D')
    elif computador == 3:
        print('Você deu sorte dessa vez, eu escolhi Tesoura, a Pedra quebra Tesoura, acho que você ganhou. :(')
    elif computador == 5:
        print('Eu escolhi Spock hehehe, o Spock vaporiza a Pedra, eu venci! :D')
    elif computador == 4:
        print('Você deu sorte dessa vez, eu escolhi Lagarto, a Pedra esmaga o Lagarto acho que você ganhou. :(')
elif escolha == 2:
    sleep(0.5)
    print('Vamos lá!')
    sleep(1)
    print('Pedra...')
    sleep(0.5)
    print('Papel...')
    sleep(0.5)
    print('Tesoura...')
    sleep(0.5)
    print('Lagarto, Spock!')
    sleep(1)
    if computador == 2:
        print('Eu também escolhi Papel, deu empate! :/')
    elif computador == 3:
        print('Eu escolhi Tesoura hehehe, Tesoura corta Papel, eu venci! :D')
    elif computador == 1:
        print('Você deu sorte dessa vez, eu escolhi Pedra, o Papel embrulha a Pedra, acho que você ganhou. :(')
    elif computador == 4:
        print('Eu escolhi Lagarto hehehe, o Lagarto come o Papel, eu venci! :D')
    elif computador == 1:
        print('Você deu sorte dessa vez, eu escolhi Spock, o Papel refuta o Spock, acho que você ganhou. :(')
elif escolha == 3:
    sleep(0.5)
    print('Vamos lá!')
    sleep(1)
    print('Pedra...')
    sleep(0.5)
    print('Papel...')
    sleep(0.5)
    print('Tesoura...')
    sleep(0.5)
    print('Lagarto, Spock!')
    sleep(1)
    if computador == 3:
        print('Eu também escolhi Tesoura, deu empate! :/')
    elif computador == 1:
        print('Eu escolhi Pedra hehehe, a Pedra quebra Tesoura, eu venci! :D')
    elif computador == 2:
        print('Você deu sorte dessa vez, eu escolhi Papel, a Tesoura corta o Papel, acho que você ganhou. :(')
    elif computador == 5:
        print('Eu escolhi Spock hehehe, o Spock quebra a Tesoura, eu venci! :D')
    elif computador == 4:
        print('Você deu sorte dessa vez, eu escolhi Lagarto, a Tesoura decapta o Lagarto, acho que você ganhou. :(')
elif escolha == 4:
    sleep(0.5)
    print('Vamos lá!')
    sleep(1)
    print('Pedra...')
    sleep(0.5)
    print('Papel...')
    sleep(0.5)
    print('Tesoura...')
    sleep(0.5)
    print('Lagarto, Spock!')
    sleep(1)
    if computador == 4:
        print('Eu também escolhi Lagarto, deu empate! :/')
    elif computador == 3:
        print('Eu escolhi Tesoura hehehe, a Tesoura decapta o Lagarto, eu venci! :D')
    elif computador == 2:
        print('Você deu sorte dessa vez, eu escolhi Papel, o Lagarto come o Papel, acho que você ganhou. :(')
    elif computador == 1:
        print('Eu escolhi Pedra hehehe, a Pedra esmaga o Lagarto, eu venci! :D')
    elif computador == 5:
        print('Você deu sorte dessa vez, eu escolhi Spock, o Lagarto envenena o Spock, acho que você ganhou. :(')
elif escolha == 5:
    sleep(0.5)
    print('Vamos lá!')
    sleep(1)
    print('Pedra...')
    sleep(0.5)
    print('Papel...')
    sleep(0.5)
    print('Tesoura...')
    sleep(0.5)
    print('Lagarto, Spock!')
    sleep(1)
    if computador == 5:
        print('Eu também escolhi Spock, deu empate! :/')
    elif computador == 4:
        print('Eu escolhi Lagarto hehehe, o Lagarto envenena o Spock, eu venci! :D')
    elif computador == 3:
        print('Você deu sorte dessa vez, eu escolhi Tesoura, o Spock quebra a Tesoura, acho que você ganhou. :(')
    elif computador == 2:
        print('Eu escolhi Papel hehehe, o Papel refuta o Spock, eu venci! :D')
    elif computador == 1:
        print('Você deu sorte dessa vez, eu escolhi Pedra, o Spock vaporiza a Pedra, acho que você ganhou. :(')
else:
    sleep(1)
    print('Ei, isso é trapaça, escolha Pedra(1), Papel(2), Tesoura(3), Lagarto(4) ou Spock(5)!')
