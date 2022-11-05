def voto(ano):
    idade = 2022 - ano
    if idade in range(18, 65):
        return f'Com {idade}, o voto é OBRIGATÓRIO!'
    elif idade < 16:
        return f'Com {idade}, o voto NÃO É OBRIGATÓRIO!'
    else:
        return f'Com {idade}, o voto é OPCIONAL!'


nasc = int(input('Digite sua data de nascimento: '))
print(voto(nasc))
