'''
Crie um programa que solicite dois valores numéricos,
um numerador e um denominador, e retorne o resto da divisão entre os dois valores.
Deixe claro que o valor do denominador não pode ser 0.
'''
numerador= float(input('Digite um numerador: '))

denominador= float(input('Digite um denominador: '))

while denominador==0:
    print('O denominador não pode ser zero!')
    denominador= float(input('Digite um denominador: '))

resultado= numerador % denominador

print(f'O resto da divisão é: {resultado}')