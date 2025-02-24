'''Um estabelecimento está vendendo combustíveis com descontos variados.
Para o etanol, se a quantidade comprada for até 15 litros,
o desconto será de 2% por litro.
Caso contrário, será de 4% por litro.
Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro.
Caso contrário, será de 5% por litro.
O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70.
Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível
(E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:

O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.
'''


'''Minha solução:
'''
opcao_escolhida= str(input('Qual tipo de combustível você deseja(D/E)?: ')).upper()
quantidade= float(input('Quantos litros deseja colocar?: '))

if opcao_escolhida=='E':
    preco_litro= 1.70
    
    if quantidade<=15:
        desconto= 0.02
    else:
        desconto=0.04
elif opcao_escolhida=='D':
    preco_litro= 2
    if quantidade<=15:
        desconto=0.03
    else:
        desconto=0.05
else:
    print('Entradas inválidas!')
    preco_litro=0
    desconto=0

valor_desconto= preco_litro*quantidade*desconto
valor_a_pagar= preco_litro*quantidade - valor_desconto

print(f'Total a pagar: {valor_a_pagar:.2f}')
'''
#Solução Alura:

# Coletamos a quantidade de litros e o tipo de combustível,
# já deixando o caractere em maiúsculo para facilitar nossa análise
quantidade_litros = float(input('Informe a quantidade de litros vendidos: '))
tipo_combustivel = input('Informe o tipo de combustível (E para etanol e D para diesel): ').upper()

#  Verificamos primeiro o tipo de combustível
if tipo_combustivel == 'E':
  # Taxamos o valor do preço em litros do etanol
  preco_litro = 1.70
  # De acordo com o valor da quantidade de litros, taxamos também o desconto
  if quantidade_litros <= 15:
    desconto = 0.02
  else:
    desconto = 0.04
elif tipo_combustivel == 'D':
  # Taxamos o valor do preço em litros do disel
  preco_litro = 2.00
  # De acordo com o valor da quantidade de litros, taxamos também o desconto
  if quantidade_litros <= 15:
    desconto = 0.03
  else:
    desconto = 0.05
# Caso ocorra um erro na especificação de tipo de combustível,
# consideramos entradas inválidas, e os preços são taxados em 0
else:
    print('Entradas inválidas!')
    preco_litro = 0
    desconto = 0

# Fazemos o cálculo do valor de desconto, seguido do cálculo do preço descontado
valor_desconto = preco_litro * quantidade_litros * desconto
valor_pago = preco_litro * quantidade_litros - valor_desconto

# Resultado
print(f'Valor a ser pago pelo cliente: R$ {valor_pago}')
'''

