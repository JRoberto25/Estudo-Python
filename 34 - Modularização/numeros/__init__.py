def moeda(preco=0, moedabr='R$'):
    return f'{moedabr}{preco:.2f}'.replace('.', ',')


def metade(num, formato=True):
    n = num / 2
    if formato is False:
        return n
    else:
        return moeda(n)


def dobro(num, formato=True):
    n = num * 2
    if formato is False:
        return n
    else:
        return moeda(n)


def acre10p(num, formato=True):
    n = num * 1.1
    if formato is False:
        return n
    else:
        return moeda(n)
