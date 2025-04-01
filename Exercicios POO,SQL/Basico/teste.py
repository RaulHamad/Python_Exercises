def primo(numero):
    qt = 0
    for n in range(1,numero):
        
        if numero % n == 0:
            qt += 1
            if qt > 1:
                return f'O numero {numero} não é primo'
            else:
                return f'O numero {numero} é primo'
