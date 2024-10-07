'''
Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o
número de bactérias por dia (em milhares) e pode ser observado a seguir:
[1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9].
Tendo esses valores, faça um código que gere uma lista contendo o percentual de
crescimento de bactérias por dia, comparando o número de bactérias em cada dia
com o número de bactérias do dia anterior. Dica: para calcular o percentual de
crescimento usamos a seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada).
'''
qt_bacterias= [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
porcentagem_lista= []
for i in range(1,len(qt_bacterias)):
    percentual_crescimento= 100* (qt_bacterias[i] - qt_bacterias[i-1]) / (qt_bacterias[i-1])
    porcentagem_lista.append(percentual_crescimento)
print(f'Percentual diário de crescimento das bactérias: {porcentagem_lista}')