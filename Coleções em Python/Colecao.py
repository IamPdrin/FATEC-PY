lista = []
soma = 0
i = 0

while i != 1:
    #Ler as notas (limite indefinido):
    nota = float(input('Digite a nota: '))
    
    #Verificando se o valor pode ser menor que zero ou maior que dez:
    if nota < 0 or nota > 10:
        print('\nNota nao compativel, iniciando execucao!\n')
        break
    else: 
        #Adicionando nota na lista:
        lista.append(nota) 


#Exiba todos os valores:
print("Todos os valores: ")
print(lista, '\n')
        
#Mostre a quantidade de valores que foram lidos:
print('Quantidade de valores lidos: ', len(lista), '\n')

#Exiba o maior e o menor valor:
lista.sort()
n = (len(lista) - 1)
print('Menor Valor:', lista[0], '\nMaior valor:', lista[n], '\n')

#Calcule e mostre a média dos valores:
for x in lista:
    soma = sum(lista)
media = soma/(len(lista))
print('Media: {:.2f} \n'.format(media))
        
#Calcule e mostre a quantidade de valores acima da média calculada:
j = 0
print('Valor(es) acima da media: ')
while j < len(lista):
    if lista[j] > media:
        print(lista[j])
        j = j + 1
    else:
        j = j + 1

#Altere todas as notas 5 para 6:
k = 0
while k < len(lista):
    if lista[k] == 5:
        lista[k] = 6.0
        k = k + 1
    else:
        k = k + 1


#Mostre todos os valores após as modificações:
print('\nLista apos modificacao:', lista, '\n')
    