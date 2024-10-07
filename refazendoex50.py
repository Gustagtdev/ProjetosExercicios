'''
Faça um programa que, ao inserir um número qualquer,
cria uma lista contendo todos os números primos entre 1 e o número digitado.
'''


lista_primos=[]
num= int(input('Digite um número: '))

for numero in range(2,num):
    primo=True

    for div in range(2,numero):
        if numero % div==0:
            primo= False
            break
    if primo:
        lista_primos.append(numero)
print(f'Lista de números primos: {lista_primos}')