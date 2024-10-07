'''
Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças.
A pesquisa foi feita e o votos computados podem ser observados abaixo:
Tabela de votos da marca
Design 1 - 1334 votos
Design 2 - 982 votos
Design 3 - 1751 votos
Design 4 - 210 votos
Design 5 - 1811 votos

Adapte os dados fornecidos para uma estrutura de dicionário.
A partir dele, informe o design vencedor e a porcentagem de votos recebidos.
'''
'''Minha solução:
votos_marca= {'Design 1':1334,
            '    Design 2':982,
                'Design 3':1751,
                'Design 4':210,
                'Design 5':1811}

mais_votado= max(votos_marca.values())
design_mais_votado= max(votos_marca.keys())
total_votos= sum(votos_marca.values())

porcentagem= 100* (mais_votado)/(total_votos)
porcentagem_arredondada= round(porcentagem,2)

print(f'O design mais votado foi o {design_mais_votado} com {porcentagem_arredondada}% dos votos totais')
'''
#Solução alternativa:
votos= {'Design 1':1334,
            'Design 2':982,
            'Design 3':1751,
            'Design 4':210,
            'Design 5':1811}

voto_vencedor=0
vencedor=''
total_votos=0

for chaves,valores in votos.items():
    total_votos+= valores
    if valores>voto_vencedor:
         voto_vencedor=valores
         vencedor=chaves

porcentagem_votos= 100*(voto_vencedor)/ (total_votos)

print(f'O design vencedor foi o: {chaves}')
print(f'Percentual de votos: {porcentagem_votos:.2f}%')
'''
# Dicionário de votos por design
votos = {'Design 1': 1334, 'Design 2': 982, 'Design 3': 1751, 'Design 4': 210, 'Design 5': 1811}

# Inicializamos as variáveis
total_votos = 0 # Irá somar todos os votos 
vencedor = '' # Irá armazenar o nome do design vencedor
voto_vencedor = 0 # Irá armazenar a quantidade vencedora de votos

# Percorremos os valores de chaves e elementos do dicionário
for design, voto_desing in votos.items():
  # Somamos o total de votos
  total_votos += voto_desing
  # Verificamos se o voto do atual desing (voto_desing) é maior que o valor armazenado em voto_vencedor
  # Cada vez que voto_desing superar o valor em voto_vencedor, 
  # a variável voto_vencedor vai ser igual à voto_desing, atribuindo um novo valor
  # De forma similar, o vencedor também é substituído pelo design
  if voto_desing > voto_vencedor:
    voto_vencedor = voto_desing
    vencedor = design
# Calculamos a porcentagem do design vencedor
porcentagem = 100 * (voto_vencedor) / (total_votos)

#Resultado
print(f'{vencedor} é o vencedor: ')
print(f'Porcentagem de votos: {porcentagem}%')
'''