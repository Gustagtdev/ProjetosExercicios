'''
Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano.
Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista.
Depois, calcule a média anual das temperaturas e
mostre todas as temperaturas acima da média anual
e em que mês elas ocorreram,
mostrando os meses por extenso (Janeiro, Fevereiro, etc.).
'''

#Como eu faria:
'''Tarefas já resolvidas do programa:
-Coleta das temperaturas em 12 meses
-Cálculo da média anual
A fazer:
-Mostrar todas as temperaturas acima da média anual e em que eles elas ocorreram
-Mostrar os meses por extenso
'''
lista_temp = []
meses=['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro',
    'Outubro','Novembro','Dezembro']
for i in range(0,12):
    temp=float(input(f'Digite uma temperatura média do mês de {meses[i]}: '))
    lista_temp.append(temp)
    print(lista_temp)
    media= sum(lista_temp)/len(lista_temp)
    
print('\nTemperaturas acima da média: ')
for i in range(0,12):
    if lista_temp[i]> media:
        print(meses[i])

'''
Solução Alura
# Coletamos a lista de temperaturas
temperaturas_mensais = []
for i in range(0,12):
  temperaturas_mensais.append(float(input(f'Digite a média de temperatura do mês {i+1}: ')))
# Criamos uma lista auxiliar para os nomes dos meses
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
# Calculamos a média
media_anual = sum(temperaturas_mensais) / len(temperaturas_mensais)

#Resultado
print('Temperaturas acima da média em: ')
for i in range(0,12):
  # Verificamos todas as temperaturas de acordo com a média anual
  if temperaturas_mensais[i] > media_anual:
    # Como os índices dos meses correspondem às temperaturas,
    # podemos imprimir eles sob o mesmo índice
    print(meses[i])
'''