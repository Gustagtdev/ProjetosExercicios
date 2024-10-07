'''
Para uma seleção de produtos alimentícios, precisamos separar o
conjunto de IDs dados por números inteiros sabendo que os produtos com ID par
são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs.
Depois, calcule e mostre a quantidade de produtos doces e amargos.
'''
dados= []
doces=0
amargos=0
for i in range(1,10+1):
    produto= int(input('Digite um ID: '))
    if produto % 2==0:
        doces+=1
    else:
        amargos+=1

print(f'Quantidade de produtos doces: {doces}')
print(f'Quantidade de produtos amargos: {amargos}')