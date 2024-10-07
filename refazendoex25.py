'''
Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.
'''

vogais= ('a,e,i,o,u')
consoantes= ('B, C, D, F, G, J,K, L, M, N, P, Q,R, S, T, V, W, X, Z').lower()



letra= str(input('Digte uma letra: '))

if letra.upper() and letra.lower() in vogais:
    print(f'A letra {letra.upper()} é uma vogal!')
elif letra.upper() and letra.lower() in consoantes: 
    print(f'A letra {letra.upper()} é uma consoante!')
