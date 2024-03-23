#2-)
#Lendo o numero de carros vendidos: 
numC = int(input('Digite o numero de carros vendidos: '))

#Lendo o valor total das vendas:
valorV = float(input('Digite o valor total de suas vendas: R$'))

#Lendo o salario fixo do funcionario: 
valorS = float(input('Digite o seu salario: R$'))

#Lendo o valor da comissao por carro:
valorC = float(input('Digite o valor da comissao por carro vendido: R$'))

#Realizando calculo do salario liquido final: 
total = valorS + (valorC * numC) + (valorV * 0.05); 

#Mostrando o salario liquido final: 
print('Salario final: R$ {:.2f}'.format(total))