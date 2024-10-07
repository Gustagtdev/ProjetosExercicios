'''
Crie um código que solicite uma frase à pessoa usuária e
imprima a mesma frase digitada mas com todas as letras maiúsculas.
'''

frase= str(input('Digite uma frase: '))

if 'Eu gosto de Java' in frase:
    print('Esta frase está proibida!')
else:
    print(frase.upper())