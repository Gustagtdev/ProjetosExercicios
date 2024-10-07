'''
Calcule a porcentagem de um produto com 15% de desconto
'''

produto= int(input('Digite o valor do produto: '))

d= produto-(produto*15/100)

print(f'O produto com o valor original de {produto}\n'
    f'Na promoção de 15% de desconto, o valor será : {d}')