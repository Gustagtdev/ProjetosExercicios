#Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.
lista_num= []

for i in range(0,5+1):
    numero= int(input('Digite um número inteiro: '))
    lista_num.append(numero)
print(f'A ordem inversa dos números é de: {lista_num[::-1]}')
