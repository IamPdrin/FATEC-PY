#3-)
#Lendo o numero inteiro menor que mil:
num1 = int(input('Digite um numero inteiro menor que mil: '))

#Veficando se o numero é realmente menor que mil:
if num1 >= 1000:
    print('O numero digitado não é menor que mil!')
    num1 = 0

#Veficando se o numero digitado possui centena:
elif num1 < 100:
    #Caso não possua, converta o numero digitado para string:
    num2 = str(num1)

    dezenas = num2[0]
    unidades = num2[1]

    # Exibindo a quantidade de dezenas e unidades:
    print('{} = {} dezenas(s), {} unidade(s)'.format(num1, dezenas, unidades))

#Caso não seja maior que mil e nem menor que cem:
else:
    #Convertendo o numero digitado para uma string:
    num2 = str(num1)

    #Selecionando os indices da string:
    # Primeiro numero (centena): 
    centenas = num2[0]
    # Segundo numero (dezena):
    dezenas = num2[1]
    # Terceiro numero (unidade):
    unidades = num2[2]

    # Exibindo a quantidade de centenas, dezenas e unidades:
    print('{} = {} centena(s), {} dezenas(s), {} unidade(s)'.format(num1, centenas, dezenas, unidades))

