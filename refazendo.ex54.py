'''
Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas.
Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se
a resposta foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.

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

'''Minha solução: '''
gabarito=['D','A','C','B','A','D','C','C','A','B']
respostas=[]
nota=0
for i in range(0,10):
    prova=str(input(f'Insira a resposta da questão {i+1}: ')).upper()
    respostas.append(prova)
for i in range(0,10):
    if respostas[i]==gabarito[i]:
        nota+=1

print(f'Nota final: {nota}')

'''
Solução Alura: 

# Inicializamos os dados
respostas = [] # Lista para receber as respostas
# Lista de gabaritos
gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
nota = 0 # Irá acumular a nota total

# Recebemos as respostas do aluno
for i in range(0, 10):
  respostas.append(input(f'Insira a resposta da questão {i + 1}: ').upper())

# Verificamos se as respostas são iguais e adicionamos à nota
for i in range(0,10):
  if respostas[i] == gabarito[i]:
    nota += 1

# Exibindo nota final
print(f'Nota final: {nota}')
'''