'''
Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as).
Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:

Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).
'''

def eleicao():
    candidato1=0
    candidato2=0
    candidato3=0
    candidato4=0
    votos_nulos=0
    votos_em_branco=0
    try:
        for i in range(1,20+1):
            votacao= int(input(f'Digite seu voto\n(1/2/3/4/5/6),eleitor {i}: '))

            if votacao== 1:
                candidato1+=1
            elif votacao== 2:
                candidato2+=1
            elif votacao== 3:
                candidato3+=1
            elif votacao== 4:
                candidato4+=1
            elif votacao== 5:
                votos_nulos+=1
            elif votacao== 6:
                votos_em_branco+=1
            else:
                print('Valor inválido,digite um valor dentro dos votos(1 a 6) ')
    except ValueError:
        print('Por favor,insira um valor válido(número inteiro): ')
    return{'candidato 1': candidato1,
           'candidato 2': candidato2,
           'candidato 3': candidato3,
           'candidato 4': candidato4,
           'votos nulos': votos_nulos,
           'votos em branco': votos_em_branco}
resultado= eleicao()


print(f'Candidato 1: {resultado['candidato 1']} votos')
print(f'Candidato 2: {resultado['candidato 2']} votos')
print(f'Candidato 3: {resultado['candidato 3']} votos')
print(f'Candidato 4: {resultado['candidato 4']} votos')
print(f'Votos nulos: {resultado['votos nulos']/20*100:.2f}%')
print(f'Votos em branco: {resultado['votos em branco']/20*100:.2f}%')

