nome = str(input('Qual seu nome?\n')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: ', nome.upper())
print('Seu nome em minúsculas é: ', nome.lower())
print('Seu nome ao todo tem: {} letras'.format(len(nome) - nome.count(' ')))

separado = nome.split()
print('Seu primeiro nome é {} e possui {} letras.'.format(separado[0], len(separado[0])))
