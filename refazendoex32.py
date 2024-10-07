'''
Um programa deve ser escrito para ler dois números e, em seguida,
perguntar à pessoa usuária qual operação ele deseja realizar.
O resultado da operação deve incluir informações sobre o número:
se é par ou ímpar, positivo ou negativo e inteiro ou decimal
'''
num1= float(input('Digite um número: '))
num2= float(input('Digite mais um número: '))

operacao= str(input(f'Qual operação deseja realizar com os números {num1} e {num2}(S/M/D): '))

if operacao.lower() and operacao.upper()== 'S':
    print(f'A soma dos números é de: {num1+num2}')
elif operacao.lower() and operacao.upper()== 'M':
    print(f'A multiplicação dos números é de: {num1*num2}')
elif operacao.lower() and operacao.upper()== 'D':
    print(f'A divisão dos números é de: {num1/num2:.2f}')
else: 
    print('Valor inválido!')
if num1 % 2==0:
    print(f'{num1} é par!')
else: 
    print(f'{num1} é ímpar!')
if num2 % 2==0:
    print(f'{num2} é par!')
else:
    print(f'{num2} é ímpar!')
if num1 % 1==0:
    print(f'{num1} é inteiro!')
else: 
    print(f'{num1} é decimal!')
if num2 % 1==0:
    print(f'{num2} é inteiro!')
else:
    print(f'{num2} é decimal!')
if num1>0:
    print(f'{num1} é positivo!')
else:
    print(f'{num1} é negativo!')
if num2>0:
    print(f'{num2} é positivo!')
else:
    print(f'{num2} é negativo!')