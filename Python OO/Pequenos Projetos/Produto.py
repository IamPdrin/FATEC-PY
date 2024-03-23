#Criação da Classe Pai (Abstracao):
class Produto: 
    
    #Construtor da Classe Pai:
    def __init__(self, nome, preco, qtEstoque):
        self.nome = nome
        self.preco = preco
        self.qtEstoque = qtEstoque
    
    #Método que contém lista com todos os atributos dos objetos da classe pai:
    def informacoes(self):
        informacoes = [self.nome, self.preco, self.qtEstoque]
        print(informacoes)
    
    #Método vender: retira a quantidade passada no parâmetro do estoque do obj:
    def vender(self, qtVendida):
        self.qtEstoque = self.qtEstoque - qtVendida
        
        if self.qtEstoque > 0:
            print("Produto vendido!")
        else:
            print("Produto Esgotado!")
            self.qtEstoque = 0
            
        return self.qtEstoque
    

#Criação da Classe Filha (Herança):
class ProdutoImportado (Produto):
    
    #Construtor da classe filha (contém referência ao construtor da pai):
    def __init__(self, nome, preco, qtEstoque, pais_origem):
        Produto.__init__(self, nome, preco, qtEstoque)
        self.pais_origem = pais_origem
    
    #Método informações sendo sobrescrito (Polimorfismo):
    def informacoes(self):
        informacoes = [self.nome, self.preco, self.qtEstoque, self.pais_origem] 
        print(informacoes)
    
    
#Criação dos objetos e chamada de métodos:
produto1 = Produto("Perfume", 250, 100)
produto1.informacoes()
produto1.vender(2)
produto1.informacoes()

produto2 = ProdutoImportado("Perfume Importado", 1500, 25, "Irlanda")
produto2.informacoes()
produto2.vender(1)
produto2.informacoes()