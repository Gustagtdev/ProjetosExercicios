'''
Crie um programa que solicite dois valores numéricos à pessoa usuária
e imprima a multiplicação dos dois valores.
'''
lista=[]

for num in range(0,2):
    num= int(input('Digite um número: '))
    lista.append(num)
    resultado=lista[0]
    resultado*=num
print(f'A multiplicação dos valores na lista é: {resultado}')
