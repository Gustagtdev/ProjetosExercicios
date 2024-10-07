'''
Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de
vendas anuais para ajudar a diretoria na tomada de decisão.
O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e
fazer um cálculo de variação percentual.
A partir do valor da variação, deve ser enviada às seguintes sugestões:

Para variação acima de 20%: bonificação para o time de vendas.
Para variação entre 2% e 20%: pequena bonificação para time de vendas.
Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
Para bonificações abaixo de -10%: corte de gastos.
'''

vendas_2022= float(input('Digite a quantidade de vendas no ano de 2022: '))
vendas_2023= float(input('Digite a quantidade de vendas no ano de 2023: '))

valor_percentual= 100*(vendas_2023-vendas_2022) / vendas_2022

if valor_percentual>20:
    print('Bonificação para o time de vendas! ')
elif 2<=valor_percentual<=20:
    print('Pequena bonificação para time de vendas')
elif -10<= valor_percentual<=2:
    print('Planejamento de políticas de incentivo às vendas')
elif valor_percentual<-10:
    print('Corte de gastos')
'''Solução Alura:
# Coletamos as vendas dos dois anos
venda_2022 = float(input('Informe a quantidade de vendas em 2022: '))
venda_2023 = float(input('Informe a quantidade de vendas em 2023: '))

# Calculamos a variação percentual entre as vendas dos anos de 2022 e 2023
var_percentual = 100 * (venda_2023 - venda_2022) / (venda_2022)

# Análise condicional da variação percentual para determinar a sugestão a ser enviada
if var_percentual > 20:
    print('Bonificação para o time de vendas.')
elif 2 <= var_percentual <= 20:
    print('Pequena bonificação para time de vendas.')
elif -10 <= var_percentual < 2:
    print('Planejamento de políticas de incentivo às vendas.')
else:
    print('Corte de gastos.')
'''