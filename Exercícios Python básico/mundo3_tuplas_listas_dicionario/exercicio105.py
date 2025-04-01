#faca um programa que tenha uma função notas()
# que pode receber varias notas de alunos e vai retornar
#um dicionario com as seguintes informações:
#quantidades de notas
#a maior nota
#a menor nota
#a media da turma
#a situação (opcional)

print('=' *20)
print('Exercicio 105')
print('=' *20)

def notas(*num,sit=False):
    """->Função que recebe varias notas
    Quantidade de notas : mostra o total de notas inseridas
    Maior nota: mostra maior nota entre todas 
    Menor nota: mostra a menor nota entre todas
    Média: gera a media entra as notas
    Situação: (opcional) se ficou com media acima de 7:
    situação boa, se nao : situação ruim"""
    cont = 0
    lista = list()
    dic = dict()
    for c in num:
        lista.append(c)
        cont += 1
    media = (sum(lista)/cont)
    maior_nota = max(lista)
    menor_nota = min(lista)
    dic["Quantidade de notas"] = cont
    dic["Maior nota"] = maior_nota
    dic["Menor nota"] = menor_nota
    dic["Média da turma"] = media
    if sit is True:
        if media >= 7:
            dic["Situação"] ='Boa'
        else:
            dic["Situação"] ='Ruim'
    
    return dic



resp= notas(10,5, 8, 7, 4, 9, 8,sit=True)
print(resp)
help(notas)

"""
def notas(*num,sit=False)
    r = dict()
    r["Total"] = len(num)
    r["Maior"] = max(num)
    r["Menor"] = min(num)
    r["Média"] = sum(num)/len(num)
"""