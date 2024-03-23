class ContaBancaria:
    
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo = self.saldo + valor
        
        if valor > 1:
            print("Foram adicionados", valor, "reais à sua conta")
        elif valor == 0: 
            print("Não é possível efetuar um depósito no valor de 0 reais")
        else: 
            print("Foi adicionado", valor, "real à sua conta")
            

        
    def sacar(self, valor):
        
        if self.saldo >= 20:
            self.saldo = self.saldo - valor
            print("Sacando", valor, "reais da sua conta")
        else:
            print("Não foi possível: O saque possui valor mínimo de 20 reais!")
        
    def obter_saldo(self):
        return self.saldo
        
class ContaCorrente (ContaBancaria):
    def __init__(self, titular, saldo, limite_cheque_especial):
        ContaBancaria.__init__(self, titular, saldo)
        self.limite_cheque_especial = limite_cheque_especial
    
    def usar_cheque_especial (self, valorCheque):
        
        if self.obter_saldo() < 20 and valorCheque <= self.limite_cheque_especial:
            print(self.titular + ", você pode utilizar um Cheque Especial no valor de até", self.limite_cheque_especial)
            valorCheque = int(input("Digite o valor do seu Cheque: "))
            print("Emitindo Cheque Especial no valor de R$", valorCheque)
        else:
            print("Não foi possível, saque o valor da sua conta ou confira seu limite!")
    

c1 = ContaBancaria("Pedro", 2000)
c1.depositar(20)
c1.sacar(2020)
c1.sacar(20)
print(c1.obter_saldo())

c2 = ContaCorrente("Thiago", 20, 2000)
c2.depositar(0)
c2.sacar(20)
c2.usar_cheque_especial(2000)
print(c2.obter_saldo())