import urllib.request

try:
    site = urllib.request.urlopen('https://g1.globo.com/')
except:
    print('O site não está acessível')
else:
    print('O G1 foi acessado com sucesso!')
