'''
Escreva um programa que peça uma data informando o dia, mês e ano e 
determine se ela é válida para uma análise.
'''
import datetime
def verificar_data(dia,mes,ano):
    try:
        datetime.datetime(day=dia,month=mes,year=ano)
        return True
    except ValueError:
        return False
try:
    dia=int(input('Digite o dia do seu nascimento(1-31): '))
    mes=int(input('Digite o mês de seu nascimento: '))
    ano= int(input('Digite o ano de seu nascimento: '))



    if verificar_data(dia,mes,ano):
        print(f'A data {dia}/{mes}/{ano} é válida!')
    else:
        print(f'A data {ano}/{mes}/{dia} é inválida!')
except ValueError:
    print('Entrada inválida.por favor digite apenas números inteiros ')

