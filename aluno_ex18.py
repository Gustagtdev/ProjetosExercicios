'''
 Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas.
 Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a
 resposta foi igual ao gabarito.
 Cada questão vale um ponto e existem as alternativas A, B, C ou D.
 Gabarito da prova:
01 - D
02 - A
03 - C
04 - B
05 - A
06 - D
07 - C
08 - C
09 - A
10 - B
'''
gabarito={1: 'D',
    2: 'A',
    3: 'C',
    4: 'B',
    5: 'A',
    6: 'D',
    7: 'C',
    8: 'C',
    9: 'A',
    10: 'B'}

def verificar_resposta():
    nota=0
    try:
        for i in range(1,10+1):
            resposta= input(f'Digite a resposta da questão {i}: ').strip().upper()
            if resposta not in ['A','B','C','D']:
                print('Resposta inválida,digite apenas as respostas como A,B,C ou D ')
                return 
            if resposta==gabarito[i]:
                nota+=1
        print(f'Nota final: {nota}')
    except None:
        print('Fim do programa.')

verificar_resposta()

