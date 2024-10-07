'''
Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as).
Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:

Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco
(representados pelo número 6).
'''
def votacao():
    voto_c1=0
    voto_c2=0
    voto_c3=0
    voto_c4=0
    voto_nulo=0
    voto_branco=0
    try:
        for i in range(0,20+1):
            voto= int(input('Informe o seu voto: '))
            if voto==1:
                voto_c1+=1
            elif voto==2:
                voto_c2+=1
            elif voto==3:
                voto_c3+=1
            elif voto==4:
                voto_c4+=1
            elif voto==5:
                voto_nulo+=1
            elif voto==6:
                voto_branco+=1
            else:
                print('Por favor,insira um valor dentre as opções disponíveis')
    except ValueError:
        print('Insira um valor válido(número inteiro)')
    return{'candidato 1': voto_c1,
           'candidato 2': voto_c2,
           'candidato 3': voto_c3,
           'candidato 4': voto_c4,
           'votos nulos': voto_nulo,
           'votos em branco': voto_branco}
resultados= votacao()
try:
    print(f'Votos candidato 1: {resultados['candidato 1']}')
    print(f'Votos candidato 2: {resultados['candidato 2']}')
    print(f'Votos candidato 3: {resultados['candidato 3']}')
    print(f'Votos candidato 4: {resultados['candidato 4']}')
    print(f'Votos nulos: {resultados['votos nulos']}')
    print(f'Votos em branco: {resultados['votos em branco']}')
    print(f'Percentual de votos nulos: {(resultados['votos nulos'] / 20 * 100):.2f}%')
    print(f'Percentual de votos em branco: {(resultados['votos em branco'] / 20 * 100):.2f}%')

except KeyError:
    print(f'Percentual de votos em branco: {(resultados["votos em branco"] / 20 * 100):.2f}%')

