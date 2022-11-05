def leiaDinheiro():
    valido = False

    while valido is False:
        entrada = str(input('Digite o valor: R$')).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'Erro! \"{entrada}\" não é um valor válido. Tente novamente.')
        else:
            valido = True
            return float(entrada)
