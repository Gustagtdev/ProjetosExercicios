'''
Faça um programa que tenha a seguinte lista contendo os valores de gastos de uma empresa de papel
[2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08].
Com esses valores, faça um programa que calcule a média de gastos.
Dica: use as funções built-in sum() e len().
'''
#Minha solução:
valores_gastos= [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

media_gastos= sum(valores_gastos)/ len(valores_gastos)

print(f'A média de gastos na empres é de: R${media_gastos}')

'''
Solução Alura:
# Dados de gastos
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

# Calculamos a média encontrando o valor total de gastos com sum
# e a quantidade total de compras realizadas com len
total_gastos = sum(gastos)
quantidade_compras = len(gastos)
media_gastos = total_gastos / quantidade_compras
# Resultado
print(f'A média de gastos é {media_gastos} reais.')
'''