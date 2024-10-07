'''
Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista.
Exemplo: [1,4,7,2,4].
'''
numero=[]

for i in range(0,5+1):
    n= int(input('Digite um número inteiro: '))
    numero.append(n)

print(f'A lista é: {numero}')

