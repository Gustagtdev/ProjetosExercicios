'''
Crie um programa que solicite dois valores numéricos,
um operador e uma potência, e realize a exponenciação entre esses dois valores.
'''

lista=[]

for num in range(0,2):
    num= int(input('Digite um número: '))
    lista.append(num)
    resultado=lista[0]
    resultado**= num
print(f'A exponenciação entre os valores da lista é: {resultado}')