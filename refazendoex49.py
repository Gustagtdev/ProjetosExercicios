'''
Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.
'''

lista_num=[]

for i in range(1,5+1):
    numero= int(input(f'Digite o {i}° número: '))
    lista_num.append(numero)
print(f'Ordem inversa dos números:\n{lista_num[::-1]}')