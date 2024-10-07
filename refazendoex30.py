'''
Escreva um programa que peça um número inteiro à pessoa usuária
e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.
'''
numero=int(input('Digite um número: '))

if numero %2 ==0:
    print('O número é par!')
else:
    print('O número é ímpar!')