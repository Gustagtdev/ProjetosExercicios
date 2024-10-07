'''
Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência.
Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a
distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100].
Encerre a entrada de dados com um número negativo.
'''
def distribuirIdades():
    faixa1=0
    faixa2=0
    faixa3=0
    faixa4=0
    while True:
        idade= int(input('Digite uma idade ou um número negativo para encerrar o programa: '))
        if idade<0:
            break
        try:
            if 0<= idade<=25:
                faixa1+=1
            elif 26<=idade<=50:
                faixa2+=1
            elif 51<=idade<=75:
                faixa3+=1
            elif 76<=idade<=100:
                faixa4+=1
            else:
                print('Idade fora do intervalo[0-100]')
        except ValueError:
            print('Por favor insira um número válido!(número inteiro)')
    
    return{'0-25': faixa1,
        '26-50': faixa2,
        '51-75': faixa3,
        '76-100': faixa4}
distribuicao= distribuirIdades()

print('\n Distribuição de idades:')

for faixa,quantidade in distribuicao.items():
    print(f'Faixa: {faixa}: \n{quantidade} clientes')
