'''
Escreva um programa que peça uma data informando o dia,
mês e ano e determine se ela é válida para uma análise.
'''
import datetime
def verificar_data(dia,mes,ano):
    try:
        datetime.datetime(day=dia,month=mes,year=ano)
        return True
    except ValueError:
        return False
try:
    dia= int(input('Digite o dia do seu nascimento(1-31): '))
    mes= int(input('Digite o mês do seu nascimento(01-12): '))
    ano= int(input('Digite o ano do seu nascimento: '))
except ValueError:
    print('Insira um valor válido(número inteiro)')

data= verificar_data(dia,mes,ano)

if data:
    print(f'O formato da data {dia}/{mes}/{ano} é válido')
else:
    print(f'O formato da data {ano}/{mes}/{dia} é inválido')