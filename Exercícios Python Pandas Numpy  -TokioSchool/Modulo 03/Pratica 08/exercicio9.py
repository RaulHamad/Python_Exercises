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
    

class Bicicleta(Veiculo):
    
    def __init__(self,cor,rodas,tipo):
        super().__init__(cor,rodas)
        self.tipo = tipo
        
    def __str__(self):
        return f'Cor: {self.cor}\nRodas: {self.rodas}\nTipo:  {self.tipo}'   
        
class Moto(Bicicleta):
    
    def __init__(self, cor,rodas,tipo,velocidade,cilindrada):
        super().__init__(cor,rodas,tipo)
        self.velocidade = velocidade
        self.cilindrada = cilindrada
        
    def __str__(self):
        return f'Cor: {self.cor}\nRodas: {self.rodas}\nTipo:  {self.tipo}\nVelocidade: {self.velocidade}\nCilindrada: {self.cilindrada}'

class Camiao(Carro):
    
    def __init__(self,cor,rodas,velocidade,cilindrada,carga):
        super().__init__(cor,rodas,velocidade,cilindrada)
        self.carga = carga
        
    def __str__(self):
        return f'Cor: {self.cor}\nRodas: {self.rodas}\nCilindradas: {self.cilindrada}\nCarga: {self.carga}\nVelocidade: {self.velocidade}km/h'
    