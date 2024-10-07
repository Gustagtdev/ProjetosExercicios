'''
Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano.
Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista.
Depois, calcule a média anual das temperaturas e mostre todas as
temperaturas acima da média anual e em que mês elas ocorreram,
mostrando os meses por extenso (Janeiro, Fevereiro, etc.).
'''
temperaturas_mensais=[]
meses=['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro'
       ,'Novembro','Dezembro']

for i in range(0,12):
    temp= float(input(f'Digite a temperatura de {meses[i]}: '))
    temperaturas_mensais.append(temp)
    media_temp= sum(temperaturas_mensais) / len(temperaturas_mensais)
print(f'Temperaturas acima da média em:')
for i in range(0,12):
    if temperaturas_mensais[i]> media_temp:
        print(meses[i])