
# Crie um pacote chamado utilidadescev que tenha dois modulos internos
#chamados moeda e dado. transfira todas as funções utilizadas nos desafios 107, 108, 109, 110
#para o primeiro pacote e mantenha tudo funcionando

import modulo_moeda.moeda



n = float(input('Digite o preço: R$ '))
print(modulo_moeda.moeda.resumo(n,20,25))



