'''
Crie um programa que solicite dois valores numéricos, um numerador e um denominador,
e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0
'''
import math
numerador= float(input('Digite um numerador: '))

denominador= float(input('Digite um denominador: '))

try:
    if denominador==0:
        denominador= float(input('Digite um denominador que não seja zero: '))
    elif denominador!=0:
        print()
except ZeroDivisionError:
    print('Por favor digite um denominador maior que 0!')
resultado= (numerador)/(denominador)
print(f'O resultado da divisão é de: {math.trunc(resultado)}')