'''
Com os mesmos dados da questão anterior, defina quantas compras foram realizadas
acima de 3000 reais e calcule a porcentagem quanto ao total de compras.

gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
'''
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
contador_acima_3000=0
for gasto in gastos:

    if gasto>3000:
        contador_acima_3000+=1

total_compras=len(gastos)

porcentagem= 100* (contador_acima_3000) / (total_compras)

print(f'Foram feitas {contador_acima_3000} compras acima de R$3000%')
print(f'Porcentagem das compras acima de R$3000: {porcentagem}')


