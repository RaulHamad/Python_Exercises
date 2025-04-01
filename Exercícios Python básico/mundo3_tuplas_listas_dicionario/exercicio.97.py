#faca um programa que tenha uma funcao chamada escreva(), que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavel.
#ex: escreva('Olá,Mundo!')
#saida: ~~~~~~~~~~~~~
#        Olá, Mundo!
#       ~~~~~~~~~~~~~


print('=' *20)
print('Exercicio 97')
print('=' *20)

def escreva(frase):
    print('~'* (len(frase)+4))
    print(f'  {frase}')
    print('~' * (len(frase)+4))

escreva('Raul é Lindo')
escreva('makunouchi')
escreva('nintendo switch lite')
