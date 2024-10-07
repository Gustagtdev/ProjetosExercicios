'''
Crie um código que solicite uma frase à pessoa usuária e imprima a mesma
frase sem espaços em branco no início e no fim e em letras minúsculas.

Crie um código que solicite uma frase à pessoa usuária
e imprima a mesma frase sem espaços em branco no início e no fim e em letras maiúsculas.
'''
frase= str(input('Digite uma frase: ')).strip().lower()

sem_espacos= ' '.join(frase.split())

print(sem_espacos)

print(sem_espacos.upper())