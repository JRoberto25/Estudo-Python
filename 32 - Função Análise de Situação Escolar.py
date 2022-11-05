def notas(*num, sit=False):
    """Função para analisar a situação de vários alunos.
    :param num: notas dos alunos.
    :param sit: parâmetro opcional que mostra a situação dos alunos.
    :return: dicionário com dados das notas, a média e a situação(opcional)."""
    dados = dict()

    dados['Total'] = len(num)
    dados['Maior'] = max(num)
    dados['Menor'] = min(num)
    dados['Média'] = sum(num) / len(num)

    if sit is True:
        if dados['Média'] < 5:
            dados['Situação'] = 'Ruim'
        elif dados['Média'] > 7:
            dados['Situação'] = 'Boa'
        else:
            dados['Situação'] = 'Regular'

    return dados


detalhes = notas(3, 6.6, 9, sit=True)
print(detalhes)
