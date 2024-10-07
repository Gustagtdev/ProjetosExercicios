'''
 O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as)
 de 4 setores da empresa.Para isso, foram fornecidos os seguintes dados:
{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
Sabendo que cada setor tem 10 colaboradores(as),
construa um código que calcule a média de idade de cada setor,
a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.
'''

dados= {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

media_geral=0
media_setor=0

for setor,idade in dados.items():
    media_setor= sum(idade) / len(idade)
    print(f'A média de idade em cada setor é de: {media_setor}')
    media_geral+=media_setor/len(dados.keys())

acima_media=0

for setor,idade in dados.items():
    for id in idade:
        if id>media_geral:
            acima_media+=1

print(f'A idade média geral na empresa é de: {media_geral:.2f} anos')
print(f'A quantidade de pessoas com idade acima da média é de: {acima_media} pessoas')
'''
Solução do Alura:
# Especificamos os dados para um dicionário
dados = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
        'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
        'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
        'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
# Inicializamos a variável que irá somar todas as idades
total_idades = 0
# Percorremos os valores de chaves e elementos do dicionário
for setor, idades in dados.items():
  # Calculamos a média dividindo a soma das idades pela quantidade funcionários em cada setor
  media_idade = sum(idades) / len(idades)
  # Imprimimos
  print(f'O {setor} tem a média de {media_idade}')
  # Somamos as médias
  total_idades += sum(idades)
# A média total será dada pela total_idades dividida pela quantidade de pessoas totais (setores * funcionários por setor)
media_total = total_idades / (len(idades) * len(dados))
print(f'A média de idade geral é {media_total}')

# Inicializamos a variável que irá contar todas pessoas com idade acima da média
acima_media = 0
# Percorremos novamente os valores de chaves e elementos do dicionário
for setor, idades in dados.items():
  # Lemos os elementos (idades) dentro de cada lista de idades no dicionário
  for id in idades:
    # Verificamos se o valor da idade é superior à média total
    if id > media_total:
      # Caso o valor da idade seja superior à média, incrementamos mais um no contador
      acima_media += 1
# Resultado
print(f'{acima_media} pessoas estão acima da idade média geral')
'''


