'''
Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos.
Os dados das vendas foram armazenados em um dicionário:

{'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

Escreva um código que calcule o total de vendas e o produto mais vendido.
'''
dados_vendas= {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

total_vendas= sum(dados_vendas.values())
produto_mais_vendido= max(dados_vendas,key= dados_vendas.get)

print(f'O total de vendas é de: {total_vendas}')
print(f'O produto mais vendido é o: {produto_mais_vendido}')



