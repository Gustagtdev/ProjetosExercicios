'''
Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos
e exiba o valor mais alto e mais baixo entre esses três anos.
'''
preco_carro=[]
anos=[]


for ano in range(1,3+1):
    preco= float(input(f'Digite o valor do carro no ano {ano}:R$ '))
    preco_carro.append(preco)
    anos.append(ano)
maior_valor= max(preco_carro)
menor_valor= min(preco_carro)
ano_maior_valor= anos[preco_carro.index(maior_valor)]
ano_menor_valor= anos[preco_carro.index(menor_valor)]
print(f'O preço mais alto foi no ano {ano_maior_valor} no valor de R${maior_valor}')
print(f'O preço mais baixo foi no ano {ano_menor_valor} no valor de R${menor_valor}')