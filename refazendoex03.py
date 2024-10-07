'''
Imprima o dia do seu nascimento em formato dia mês ano.
Lembrando que os valores de dia e ano não podem estar entre aspas.
Supondo uma data de aniversário dia 28 de fevereiro de 2003,
o formato deve estar como no exemplo abaixo:
28 fevereiro 2003
'''
dia= int(input('Digite o dia do seu nascimento[1-31]: '))
mes= int(input('Digite o mês do seu nascimento: '))
ano=int(input('Digite o ano do seu nascimento: '))

print(f'Você nasceu em: {dia}/{mes}/{ano}')