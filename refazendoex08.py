'''
Crie um programa que solicite dois valores numéricos
à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.
'''


lista= []

for n in range(0,2):
    n= int(input('Digite um número: '))
    lista.append(n)
    resultado=lista[0]
    resultado-=n
print(f'A subtração é: {resultado}')

