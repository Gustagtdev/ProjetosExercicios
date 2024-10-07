'''
Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.
'''
lista= []

for n in range(0,3):
    n= int(input('Digite um número: '))
    lista.append(n)
print(f'A soma é: {sum(lista)}')