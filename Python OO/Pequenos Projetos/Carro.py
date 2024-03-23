class Carro:
    
    def __init__(self, marca, modelo, ano, quilometragem):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem
    
    def informacoes (self):
        informacoes = [self.marca, self.modelo, self.ano, self.quilometragem]
        print(informacoes)
        
    def andar (self, distancia):
        
        if distancia < 1000: 
            self.quilometragem = 0
        elif distancia > 1000 and distancia < 2000:
            self.quilometragem = self.quilometragem + 1
            print("Você andou mais 1km")
        elif distancia > 2000 and distancia < 3000:
            self.quilometragem = self.quilometragem + 2
            print("Você andou mais 2km")
        elif distancia > 3000 and distancia < 4000:
            self.quilometragem = self.quilometragem + 3
            print("Você andou mais 3km")
        else:
            self.quilometragem = self.quilometragem + 4
            print("Você andou mais 4km")
            
        return self.quilometragem
    
class CarroEletrico (Carro):
    def __init__(self, marca, modelo, ano, quilometragem, autonomia):
        Carro.__init__(self, marca, modelo, ano, quilometragem)
        self.autonomia = autonomia
        
    def informacoes (self):
        informacoes = [self.marca, self.modelo, self.ano, self.quilometragem, self.autonomia]
        print(informacoes)
        
carro1 = Carro("Toyota", "Ethios", "2010", 50000)
carro1.informacoes()
carro1.andar(3000)
carro1.informacoes()

carro2 = CarroEletrico("Renault", "Kwid E-Tech", "2023", 0, 0)
carro2.informacoes()
carro2.andar(3000)
carro2.informacoes()