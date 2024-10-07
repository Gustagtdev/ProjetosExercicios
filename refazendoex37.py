'''
Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
'''
num1= int(input('Digite um número: '))
num2= int(input('Digite um 2° número: '))

for numero in range(num1,num2+1):
    print(numero)
