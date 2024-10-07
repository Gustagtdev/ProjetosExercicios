'''
5) Faça um programa que, ao inserir um número qualquer,
cria uma lista contendo todos os números primos entre 1 e o número digitado.
'''



''''
def e_primo(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n % 2==0 or n %3==0:
        return False
    i=5
    while i *i <=n:
        if n % i==0 or n % (i+2)==0:
            return False
        i+=6
    return True
def lista_primos(limite):
    primos=[]
    for n in range(2,limite+1):
        if e_primo(n):
            primos.append(n)
    return primos
try:
    num= int(input('Digite um número: '))
    if num<1:
        print('Por favor insira um número maior ou igual a 1: ')
    else:
        primos= lista_primos(num)
        print(f'Números entre 1 e {num}: {primos}')
except ValueError:
    print('Número inválido, por favor digite um número inteiro: ')
'''
'''Solução da Alura
# Coletamos o números
numero = int(input('Digite um número inteiro: '))
# Lista para receber os números primos
lista_primos = []
# Laço que vai rodar por todos os números abaixo do número digitado
for num in range(2, numero):
  # Primo é uma bandeira, ela permite sabermos se o valor analisado é ou não primo
  primo = True 
  # Testamos se todos os números abaixo do especificado no primeiro laço podem
  # gerar uma divisão exata
  for teste_divisiveis in range(2, num):
    if num % teste_divisiveis == 0:
      # Caso seja divisivel por algum número entendemos que 
      # o num não é primo e finalizamos o laço interno com break
      primo = False
      break
  # A condição se torna o resultado booleno de primo: False, ignoramos o condicional
  # True, executamos o bloco do if
  if primo:
    lista_primos.append(num)
# Resultado
print(f'Lista de números primos: {lista_primos}')
'''
#Solução personalizada do problema(solução pessoal):

numero= int(input('Digite um número inteiro qualquer: '))

lista_primos= []

for num in range(2,numero):
    primo=True
    for div in range(2,num):
        if num % div==0:
            primo=False
            break
    if primo:
        lista_primos.append(num)

print(f'Lista de números primos: {lista_primos}')




