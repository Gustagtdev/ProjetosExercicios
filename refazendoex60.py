'''
O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as) de
4 setores da empresa. Para isso, foram fornecidos os seguintes dados:
{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
Sabendo que cada setor tem 10 colaboradores(as),
construa um código que calcule a média de idade de cada setor,
a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.
'''
setores = {
    'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
    'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
    'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
    'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
}
media_setores = {}
for setor, idades in setores.items():
    media_setores[setor] = sum(idades) / len(idades)

todas_as_idades = sum(idades for idades in setores.values())
total_de_pessoas = sum(len(idades) for idades in setores.values())
media_geral = todas_as_idades / total_de_pessoas

pessoas_acima_media = sum(1 for idades in setores.values() for idade in idades if idade > media_geral)

print("Média de idade de cada setor:")
for setor, media in media_setores.items():
    print(f"{setor}: {media:.2f}")

print(f"\nMédia de idade geral entre todos os setores: {media_geral:.2f}")
print(f"\nNúmero de pessoas acima da idade média geral: {pessoas_acima_media}")
