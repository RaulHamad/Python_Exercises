#dentro do pacote utilidadescev que criamos no desafio 111, temo
#um modulo chamado dado. Crie um função chamada leiaDinheiro()
#que seja capaz de funcionar como a função input(), mas com uma
#validação de dados para aceitar paenas valores que sejam monetarios.
#def leiaDinheiro():

def leiaDinheiro():



    validação_dados = str(input('Digite um valor: ')).replace(',','.').strip()    
    txt = validação_dados.isalpha()
    
    while txt is True or validação_dados == '':    
        print(f'\033[0;31mERRO!!!"{validação_dados}" não é um numero\033[m')
        validação_dados = str(input('Digite um valor: ')).replace(',','.').strip()
        txt = validação_dados.isalpha()
    
    return float(validação_dados)