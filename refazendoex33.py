'''
Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo.
O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo,
se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:

Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes.
'''
lado1= float(input('Digite o lado 1 do triângulo!: '))
lado2= float(input('Digite o lado 2 do triângulo!: '))
lado3= float(input('Digite o lado 3 do triângulo!: '))

if lado1==lado2!=lado3 or lado3==lado2!=lado1:
    print('O triângulo é isósceles! ')
elif lado1==lado2==lado3:
    print('O triângulo é equilátero! ')
elif lado1!=lado2!=lado3:
    print('O triângulo é escaleno! ')