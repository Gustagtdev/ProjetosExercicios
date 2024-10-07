'''
Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas.
A leitura deve ser encerrada ao ser enviado o valor -273°C.
'''
lista_temp=[]
while True:
    temp= float(input('Digite uma temperatura em °C (ou -273°C para encerrar): '))

    if temp== -273:
        break

    lista_temp.append(temp)
if lista_temp:
    media= sum(lista_temp) / len(lista_temp)
    print(f'A média das temperaturas é de: {media:.2f}°C')
else: 
    print('Nenhuma temperatura foi inserida!')

print('Programa encerrado!')

'''
Solução Alura:
# coletamos a temperatura
temperatura = float(input('Insira a temperatura em Celsius: '))

# inicializamos uma contadora e soma para a média
contadora = 0
soma = 0

# nosso código executa sempre até o valor de temperatura for igual a -273
while temperatura != -273:
    # a soma é dada com a adição da temperatura à variavel soma
    soma += temperatura
    # contamos a quantidade de valores coletados através da contadora
    contadora += 1
    # coletamos novamente a temperatura
    temperatura = float(input('Insira a temperatura em Celsius: '))

media = soma / contadora

print(f'A média das temperaturas é: {media}')
'''