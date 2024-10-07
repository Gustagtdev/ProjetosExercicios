'''
Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária.
Lembrando que o fatorial de um número inteiro é a multiplicação desse número por
todos os seus antecessores até o número 1.
Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.
'''
from math import factorial

numero= int(input('Digite um número: '))

fatorial_numero=factorial(numero)

print(f'O fatorial de {numero} é: {fatorial_numero}')