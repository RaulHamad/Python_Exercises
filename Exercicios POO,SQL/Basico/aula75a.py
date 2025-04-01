arq = open('texto2.txt')
text = arq.read()
i=1
for linha in text.splitlines():
    print(i, linha)
    i +=1

arq.close()