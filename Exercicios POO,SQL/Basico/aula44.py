dici ={}


while True:
    
   apt = int(input('qual apt: '))
   if apt != -1:
      proprietario = input('nome do prop: ')
      dici.update({apt:proprietario})
   else:
      break
toto = dict(sorted(dici.items()))
print(toto)
for c in toto.items():
   print(c)