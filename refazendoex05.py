'''
Coleta e amostragem de dados
Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”.
Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e
imprima “Olá, [nome], você tem [idade] anos.”.
Crie um programa que solicite à pessoa usuária digitar seu nome, idade e
altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.
'''

pessoa= str(input('Digite o seu nome: '))
idade= int(input(f'Digite a sua idade {pessoa}: '))
altura= float(input(f'Digite a sua altura {pessoa}: '))

print(f'\nOlá {pessoa}, você tem {idade} anos e tem {altura}m de altura')