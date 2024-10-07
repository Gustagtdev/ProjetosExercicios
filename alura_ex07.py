'''
Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança,
por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo.
Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
'''
def verificarNumeroPrimo(numero):
    if numero <= 1:
        return False

    for i in range(2,int(numero**0.5)+1):
        if numero % i == 0:
            return False
    return True

while True:
    try:
        num= int(input('Digite um número: '))
        if num>1:
            break
        else:
            print("Por favor,digite um número maior que 1")
    except:
        print('Por favor digite um número inteiro válido')

if verificarNumeroPrimo(num):
    print(f'O número {num} é primo!')
else:
    print(f'O número {num} não é primo!')