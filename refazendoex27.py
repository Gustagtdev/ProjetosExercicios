'''
Escreva um programa que pergunte sobre o preço de três produtos
e indique qual é o produto mais barato para comprar.
'''
preco_produto=[]
barato=[]

for i in range(1,3+1):
    preco= float(input(f'Digiite o valor do produto {i}:R$'))
    preco_produto.append(preco)
    barato.append(i)

preco_mais_barato= min(preco_produto)

produto_id= barato[preco_produto.index(preco_mais_barato)]

print(f'O produto mais barato é o produto {produto_id} no valor de R${preco_mais_barato}')