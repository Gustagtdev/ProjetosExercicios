'''
Crie um código que solicite uma frase à pessoa usuária
e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.

Crie um código que solicite uma frase à pessoa usuária
e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.

Crie um código que solicite uma frase à pessoa usuária
e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.
'''

frase= str(input('Digite uma frase: ')).strip().upper().lower()
frase2= str(input('Digite mais uma frase: ')).strip().upper().lower()

trocas= frase.replace('a','f').upper().lower()
sem_espacos= ' '.join(trocas.split())

trocas_frase= frase.replace('s','$').upper().lower()
sem_espacosfrase= ' '.join(trocas_frase.split())

trocas2= frase2.replace('a','@').upper().lower()
sem_espacos2= ' '.join(trocas2.split())

trocas_frase2= frase2.replace('s','$').upper().lower()
sem_espacosfrase2= ' '.join(trocas_frase2.split())

print(sem_espacos.capitalize())
print(sem_espacosfrase.capitalize())

print(sem_espacos2.capitalize())
print(sem_espacosfrase2.capitalize())