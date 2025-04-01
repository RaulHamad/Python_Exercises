frase = 'Curso em Video'
print(len(frase)) #conta a string
print(frase.count('o',1,15)) # conta quantas vezes aparece a letra 'o' no intervalo de 1 a 15
print(frase[1:15:2]) #printa frase pulando de 2 em 2 caracteres
print(frase.find('ide')) #encontrar a palavra 'ide' na frase
print(frase.find('ou')) # quando n encontra da o valor de -1
print('curso' in frase) # se exista a palavra dentro da frase
print(frase.upper()) # todos os caracteres maiusculos
print(frase.lower()) # todos os caracteres minusculos
print(frase.replace('Video', 'toto')) #trocar palavra 'video' por 'toto' na frase
print(frase.capitalize()) #pega toda frase e coloca apenas a primeira palavra com letra maiuscula
print(frase.title())# coloca todos as primeiras letras em maiusculo

frase = '     Curso em phyton  '
print(frase)
print(frase.strip()) #remove espaços do inicio e fim
print(frase.rstrip())
print(frase.lstrip())

print(frase.split()) # separa lista em array
frase = 'Curso em video'
print(frase)
print('-'.join(frase))
print(frase.split())


# para saber se o item digitado é numerico
n1 =input('Digite algo: ')
if n1.isnumeric(): #condição se a variavel str for um numero
    n1 = int(n1)
