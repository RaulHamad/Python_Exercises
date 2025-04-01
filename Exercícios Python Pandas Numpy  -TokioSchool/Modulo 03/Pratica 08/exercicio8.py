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
    

carro1 = Carro("red",4,90,2000)
bicicleta1 = Bicicleta("green",2,"desportivo")
moto1 = Moto("blue",2,"urbano",150,600)
camiao1 = Camiao("purple",4,90,3000,5)
print("-=-=-=Construtor=-=-=-=-")
print(carro1)
print(" ")
print("-=-=-=Construtor=-=-=-=-")
print(bicicleta1)
print(" ")
print("-=-=-=Construtor=-=-=-=-")
print(moto1)
print(" ")
print("-=-=-=Construtor=-=-=-=-")
print(camiao1)
print(" ")



lista_veiculos = [carro1,bicicleta1,moto1,camiao1]
def catalogar(tire = 0):
    # Listando tipo de objeto e seus atributos
    for i in lista_veiculos:
        print(type(i).__name__)
        print(i)
    cnt = 0
    print(" ")
    # Listando tipo de objeto pelo atributo 'rodas
    for i in lista_veiculos:
        if tire == 0:
            break
        if i.rodas == tire:
            print(type(i).__name__)
            print((i))
            cnt += 1
    if tire != 0:
        print(f'Encontrou-se {cnt} veiculos com {tire} rodas.')



catalogar(0)
catalogar(2)
catalogar(4)

    
