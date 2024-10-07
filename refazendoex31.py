'''
Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.
'''
numero= float(input('Digite um número: '))

if numero % 1==0:
    print('O número é inteiro!')
else:
    print('O número é decimal!')