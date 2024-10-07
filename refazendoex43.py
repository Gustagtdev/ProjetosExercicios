'''
Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança,
por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo.
Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
'''
'''Solução com uma função:
def e_primo():
        numero= int(input('Digite um número: '))

        primo=True
        if numero<=1:
            primo=False
        else:
            for num in range(2,numero):
                if numero % num==0:
                    primo=False
                    break
        if primo:
            print(f'O número {numero} é primo')
        else:
            print(f'O número {numero} não é primo')
resultado= e_primo()
resultado
'''
'''Solução simplificada:'''
numero= int(input('Digite um número: '))
primo=True
if numero<=1:
    primo=False
else:
    for num in range(2,numero):
        if numero % num==0:
            primo=False
            break
    if primo:
        print(f'O número {numero} é primo')
    else:
        print(f'O número {numero} não é primo')

'''Solução Alura:
# Solicitamos o número
num = int(input("Digite o número: "))

# Assumimos que o número é primo até que se prove o contrário
eh_primo = True

# Números abaixo de 2 não são primos
if num <= 1 :
  eh_primo = False
else:
    for i in range(2, num):
        # Se o número for divisível por qualquer número dentro deste intervalo,
        # ele não é primo, portanto, mudamos a variável 'eh_primo' para False e saímos do loop.
        if num % i == 0:
            eh_primo = False
            break
  
# Verifica se 'eh_primo' ainda é True, o que significa que o número passou pelo loop
# sem ser divisível por nenhum número além de 1 e ele mesmo.
if eh_primo:
    # Se for o caso, o número é primo.
    print(f'O número {num} é primo')
else:
    # Caso contrário, o número não é primo.
    print(f'O número {num} não é primo')
'''