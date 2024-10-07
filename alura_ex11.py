'''
2)Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e
calcule a porcentagem quanto ao total de compras.
'''

compras= [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
contador=0
for dado in compras:
    if dado >3000.0:
        contador+=1
total_compras= len(compras)
porcento_3mil= 100* (contador) / (total_compras)

print(f'{contador} compras foram acima de R$3mil reais: ')
print(f'Está é a porcentagem destas compras em relação ao todo: {porcento_3mil}%')
       
       

       
