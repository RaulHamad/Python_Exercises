#refaze rexercicio 61, lendo primeiro termo,
#  a razao e mostrando os 10 primeiros termos usando while
#depois pergunta mais quantos numero o usuario quer ver
#so finaliza o programa quando o usuario digitar 0

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contador = 1
termos = 10
novos_numeros_de_termos = 1
n_termos = primeiro_termo - razao

while novos_numeros_de_termos != 0:
    termos += novos_numeros_de_termos
    while contador <= termos:
        n_termos += razao
        contador += 1
        print(n_termos)
    print('=-=' *10)
    print('Voce quer ver mais quantos termos??')
    novos_numeros_de_termos = int(input())
    print('=-=' *10)
    

print('GG com {} termos'.format(termos -1))


    
