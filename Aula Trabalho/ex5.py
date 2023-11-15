#Lendo os 3 numeros inteiros:
num1 = int(input('Digite o 1° numero: '))
num2 = int(input('Digite o 2° numero: '))
num3 = int(input('Digite o 3° numero: '))

#Atribuindo o num1 às variáveis maior, medio e menor
maior = num1
medio = num1
menor = num1

#Verificando se num2 é maior que num1:
if num2 > maior:
    #Atualizando armazenamento da variável medio, para evitar erros de exibição:
    medio = maior
    #Caso seja, o num2 passa a ser o maior:
    maior = num2
#Verificando se num2 é menor que num1:
elif num2 < menor:
    medio = menor
    #Caso seja, o num2 passa a ser o menor:
    menor = num2
#Caso o num2 não seja menor nem maior, num2 é o medio:
else:
    medio = num2

#Verificando se num3 é maior que o maior (pode ser num1 ou num2):
if num3 > maior:
    medio = maior
    #Caso seja, o num3 passa a ser o maior:
    maior = num3
#Verificando se num3 é menor que o menor (pode ser num1 ou num2):
elif num3 < menor:
    medio = menor
    #Caso seja, o num3 passa a ser o menor
    menor = num3
#Caso o num3 não seja menor nem maior, num3 é o medio
else:
    medio = num3

#Exibindo valores em ordem decrescente:
print('\n1°:', menor)
print('2°:', medio)
print('3°:', maior)
