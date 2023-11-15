#4-)
import math

l1 = int(input('Digite o valor do 1° lado do triângulo: '))
l2 = int(input('Digite o valor do 2° lado do triângulo: '))
l3 = int(input('Digite o valor do 3° lado do triângulo: '))

#Verificando se os valores digitados podem formar um triângulo
#De acordo com a desigualdade triangular:
if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print('Esses valores podem formar um triângulo! ')
    
    #Calculo do semiperímetro: 
    s = (l1 + l2 + l3) / 2;
    #Fórmula de Herão: 
    area = math.sqrt(s * (s - l1) * (s - l2) * (s - l3))

    #Exibindo a area: 
    print('Area: {:.0f}'.format(area))
#Caso não seja possivel formar um triangulo com os valores digitados:
else:
    print('Esses valores não podem formar um triângulo!')