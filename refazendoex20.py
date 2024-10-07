'''
Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha.
Em seguida, imprima a frase sem espaços em branco no início e no fim.

Crie um código que solicite uma frase à pessoa usuária
e imprima a mesma frase sem espaços em branco no início e no fim.
'''
frase= str(input('Digite uma frase: ')).strip()
sem_espaco_nenhum= ' '.join(frase.split())

print(sem_espaco_nenhum)
