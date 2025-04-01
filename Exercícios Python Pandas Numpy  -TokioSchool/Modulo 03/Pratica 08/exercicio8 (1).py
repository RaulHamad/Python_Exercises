class Veiculo:
    
    def __init__(self,cor,rodas):
        self.cor = cor
        self.rodas = rodas
        
    def __str__(self):
        return f'Cor: {self.cor}\nRodas: {self.rodas}'
    @classmethod    
    def filtrar(cls,lista,nome_veiculo):
        lista_carros =[]
        for i in lista:
            if(type(i).__name__) == nome_veiculo:
                lista_carros.append(i)
        return lista_carros
    
    
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
    

carro1 = Carro("red",4,190,2000)
carro2 = Carro("green",4,160,1800)
carro3 = Carro("black",4,140,1400)
bicicleta1 = Bicicleta("green",2,"desportivo")
bicicleta2 = Bicicleta("pink",2,"urbano")
moto1 = Moto("blue",2,"urbano",150,600)
moto2 = Moto("gray",2,"desportivo",180,800)
moto3 = Moto("yellow",2,"urbano",220,1000)
camiao1 = Camiao("purple",4,90,3000,5)
camiao2 = Camiao("red",4,110,3500,8)

lista_veiculos = [carro1,carro2,carro3,bicicleta1,bicicleta2,moto1,moto2,moto3,camiao1,camiao2]

print("Filtrar Objetos do tipo Carro")
listaCarro = Veiculo.filtrar(lista_veiculos,"Carro")
contador = 1
for i in listaCarro:
    print(f'---Objeto {contador}---')
    print(i)
    contador +=1
    
print("Filtrar Objetos do tipo Moto e mostrar apenas sua cilindrada")
listaCarro = Veiculo.filtrar(lista_veiculos,"Moto")
contador = 1
for i in listaCarro:
    print(f'---Objeto {contador}---')
    print(i.cilindrada)
    contador +=1
contador = 1   
print("Filtrar Objetos do tipo Camiao e mostrar apenas sua carga")
listaCarro = Veiculo.filtrar(lista_veiculos,"Camiao")

for i in listaCarro:
    print(f'---Objeto {contador}---')
    print(i.carga)
    contador +=1


    
