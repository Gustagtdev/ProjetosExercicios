'''
Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos.
Os dados das vendas foram armazenados em um dicionário:
{'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
Escreva um código que calcule o total de vendas e o produto mais vendido.
'''

vendas= {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

total_vendas= sum(vendas.values())
produto_mais_vendido= min(vendas.keys())
unidades= max(vendas.values())
print(f'O total de vendas foi de: R${total_vendas}')
print(f'O produto mais vendido foi o: {produto_mais_vendido} que vendeu {(unidades)} unidades ')
#Solução do Alura:

'''
# Dicionário de vendas
dados_vendas = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60, 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

# Inicializamos as variáveis
total_vendas = 0 # Irá somar todos as vendas
produto_mais_vendido = '' # Irá armazenar o nome do produto mais vendido
unidades_produto_mais_vendido = 0 # Irá armazenar a maior quantidade vendas

# Percorremos os valores de chaves e elementos do dicionário
for produto in dados_vendas.keys():
  # Somamos o total de vendas 
  total_vendas += dados_vendas[produto]
  # Verificamos se valor de venda atual desing (dados_vendas[produto]) é maior que o valor armazenado em unidades_produto_mais_vendido
  # Cada vez que dados_vendas[produto] superar o valor em unidades_produto_mais_vendido, 
  # a variável unidades_produto_mais_vendido vai ser igual à dados_vendas[produto], atribuindo um novo valor
  # De forma similar, produto_mais_vendido também é substituído pelo produto atual
  if dados_vendas[produto] > unidades_produto_mais_vendido:
    unidades_produto_mais_vendido = dados_vendas[produto]
    produto_mais_vendido = produto
# Resultados
print(f'Total de vendas é {total_vendas}')
print(f'{produto_mais_vendido} é o mais vendido')
'''