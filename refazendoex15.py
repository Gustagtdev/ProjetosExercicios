'''
Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15
com pesos respectivamente iguais a 1, 2, 3 e 4.
'''
'''Solução 1
numeros= 5,12,20,15
pesos= 1,2,3,4
media_p= (5*1 + 12*2 + 20*3 + 15*4) / sum(pesos)

print(f'A média ponderada dos números é de: {media_p}')
'''
#Solução alternativa:

def media_ponderada(numeros,peso):
    soma_ponderada= sum(numeros*peso for numeros,peso in zip(numeros,peso))
    soma_pesos= sum(peso)

    return soma_ponderada/ soma_pesos

numeros=[5,12,20,15]
peso= [1,2,3,4]

resultado= media_ponderada(numeros,peso)
print(f'A média ponderada é de: {resultado}')