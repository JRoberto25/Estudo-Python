import unidecode
frase = str.lower(input('Digite uma frase: ').strip())
frasepronta = unidecode.unidecode(frase)
letra = str(input('Digite a letra que queira buscar: ').strip())
num = frasepronta.count(letra)
print('A letra {} aparece {} vezes.'.format(letra, num))
