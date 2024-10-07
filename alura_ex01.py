'''
1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
'''

num= int(input("Digite um número: "))
num2= int(input('Digite mais um número: '))
inicio= min(num,num2)
fim= max(num,num2)

print(f'Números entre {inicio} e {fim} são:')

for i in range(inicio,fim+1,1):
    print(i,end=' ')
print()
'''
Outra forma de resolver o problema

'''
'''
# Solicita dois números inteiros do usuário
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# Determina o menor e o maior número
inicio = min(num1, num2)
fim = max(num1, num2)

# Imprime todos os números inteiros entre os dois números dados
print(f"Números entre {inicio} e {fim}:")
for numero in range(inicio, fim + 1):
    print(numero, end=" ")

print()  # Imprime uma linha em branco no final
'''

