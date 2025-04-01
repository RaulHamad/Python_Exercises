#ler o primeiro termo e uma razao. mostrar os 10 primeiros termos dessa PA.

primeiro_termo = int(input('digite o primeiro termo: '))
razao = int(input('digite razao dessa PA: '))
n_termos = primeiro_termo - razao
for c in range(1,11):
    n_termos = n_termos + razao
    print(n_termos)