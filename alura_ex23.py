'''
Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta.
A equipe fez a coleta de informações sobre o número de espécies de plantas e
animais em cada área dessa floresta e armazenou essas informações em um dicionário.
Nele, a chave descreve a área dos dados e os valores nas listas correspondem às espécies
de plantas e animais nas áreas, respectivamente.
{'Área Norte': [2819, 7236],
 'Área Leste': [1440, 9492],
 'Área Sul': [5969, 7496],
 'Área Oeste': [14446, 49688],
 'Área Centro': [22558, 45148]}
Escreva um código para calcular a média de espécies por área e identificar a área
com a maior diversidade biológica. Dica: use as funções built-in sum() e len().
 '''
#Minha solução:


''' 
Solução da Alura:

plantas={'Área Norte': [2819, 7236],
 'Área Leste': [1440, 9492],
 'Área Sul': [5969, 7496],
 'Área Oeste': [14446, 49688],
 'Área Centro': [22558, 45148]}
maior_area=0
soma_media=0
maior_soma=0

for area,especies in plantas.items():
    soma_especies= sum(especies)
    media= soma_especies/ len(especies)

    print(f'A área {area} tem a média de especies de: {media}')

    if soma_especies>maior_soma:
        maior_soma=soma_especies
        maior_area=area
    soma_media+=media

print(f'A area com maior diversidade biológica é a de: {area}')
'''
