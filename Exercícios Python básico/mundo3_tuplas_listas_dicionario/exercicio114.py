import urllib.request
import urllib

n = str(input('insira o site: '))
try:
    site1 = urllib.request.urlopen('https://www.'+n+'/')
except:
    print('site nao acessivel')
else:
    print('abri o site')
