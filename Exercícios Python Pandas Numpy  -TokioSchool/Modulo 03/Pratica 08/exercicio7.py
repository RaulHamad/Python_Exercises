class Veiculo:
    
    def __init__(self,cor,rodas):
        self.cor = cor
        self.rodas = rodas
        
    def __str__(self):
        return f'Cor: {self.cor}\nRodas: {self.rodas}'
    
    
class Carro(Veiculo):
    
    def __init__(self,cor,rodas,velocidade,cilindrada):
        super().__init__(cor,rodas)
        self.velocidade = velocidade
        self.cilindrada = cilindrada
    
    def __str__(self):
        return f'Cor: {self.cor}\nRodas: {self.rodas}\nCilindrada: {self.cilindrada}\nVelocidade: {self.velocidade}'
    #fim exercicio7

carro1 = Carro("vermelho", 4,100,1000)
carro2 = Carro("azul", 2, 150, 2000)
carro3 = Carro("verde", 8, 200, 2500)
print(carro1)
print(" ")
print(carro2)
print(" ")
print(carro3)