'''
Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].
'''

lista_num=[]

for numero in range(1,5+1):
    numeros= int(input(f'Digite o {numero}° número: '))
    lista_num.append(numeros)

print(f'Números da lista:\n{lista_num}')