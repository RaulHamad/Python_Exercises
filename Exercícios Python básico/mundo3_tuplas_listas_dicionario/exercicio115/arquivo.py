def cria(arq):
    try:
        a= open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return ('error........')
    else:
        return ('Criado com sucesso...')
"""def inclui(nome): #def da opção incluir
    seuNome = str(input('Digite um nome: ')).strip().upper() # tira espaços, poe em uppercase
    seuNome= str(seuNome.ljust(20, '.')) #  seu nome justificado a esquerda com pontos de preenchimento até 20 caracteres
    idade = str(input('Digite a idade')).strip() # tira os espaços
    arquivo = open(nome, 'a+', encoding='utf-8') # encoding='utf-8' permite a leitura e gravação de Ç, á, etc..
    arquivo.write(seuNome)
    arquivo.write(idade)
    arquivo.write(' anos\n') # inclui a palavra anos e pula linha
    arquivo.close()"""