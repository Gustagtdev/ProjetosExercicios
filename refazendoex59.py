'''
Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta.
A equipe fez a coleta de informações sobre o número de espécies de plantas e animais em cada área
dessa floresta e armazenou essas informações em um dicionário. Nele, a chave descreve a área dos dados
e os valores nas listas correspondem às espécies de plantas e animais nas áreas, respectivamente.
{'Área Norte': [2819, 7236],
 'Área Leste': [1440, 9492],
 'Área Sul': [5969, 7496],
 'Área Oeste': [14446, 49688],
 'Área Centro': [22558, 45148]}
Escreva um código para calcular a média de espécies por área e identificar a área com a
maior diversidade biológica. Dica:
use as funções built-in sum() e len().
'''
dados={'Área Norte': [2819, 7236],
 'Área Leste': [1440, 9492],
 'Área Sul': [5969, 7496],
 'Área Oeste': [14446, 49688],
 'Área Centro': [22558, 45148]}

for area,especies in dados.items():
    soma_especies= sum(especies)
    media_especies= soma_especies/ len(especies)

    print(f'A área {area} possui uma média de: {media_especies} espécies')

maior_diversidade= max(dados,key=dados.get)

print(f'A área com a maior diversidade biológica é a: {maior_diversidade}')