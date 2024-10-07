'''
Crie um programa que solicite dois valores numéricos,
um numerador e um denominador e realize a divisão inteira entre os dois valores.
Deixe claro que o valor do denominador não pode ser 0.
'''
from math import trunc
numerador= float(input('Digite um numerador: '))

denominador= float(input('Digite um denominador: '))

while denominador==0:
    print('O denominador não pode ser zero!')
    denominador= float(input('Digite um denominador: '))

resultado= numerador//denominador
print(f'A divisão inteira é: {trunc(resultado)}')

