#filter aplica em uma função e retorna todos os elementos de valor TRUE

a= filter(None,[0,1,2,None,2>1,'olá'])
print(list(a))
b=filter(lambda x: x>3, [0,1,2,3,4,5,6])
print(list(b)) 
c = list(filter(lambda s: s>'a', 'python r0cks'))
print(c)
d = list(filter(lambda x: x%2, [1,2,3,4,5,6]))
print(d)

print('-='*30)
lista = [
    
    {"nome": 'Jose', "idade": 28},
    {"nome": 'Adriana', "idade": 39},
    {"nome": 'Pedro', "idade": 17},
    {"nome": 'Maria', "idade": 23},
    {"nome": 'Roberto', "idade": 15}
]

#menores de idade
menores = list(filter(lambda x : x['idade'] < 18, lista))
print(menores)
#retorna o nome das pessoas que tem mais de 5 letras no nome
nome_retorno = list(filter( lambda x : len(x['nome']) < 6, lista))
print(nome_retorno)

print('-='*30)
#retornar apenas os dados que estao acima da media
import statistics
dados = [1.2,3.4,1.7,4.5,3.2,2.3,5.6,2.4,1.6]
media = statistics.mean(dados)
acima = list(filter(lambda x : x > media, dados))
print(acima)