'''
Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A
ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de
3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.
'''
'''
Minha solução:
'''
coloniaA= 4
coloniaB=10
taxaA= 00.3
taxaB= 0.15

dias=0

while coloniaA<=coloniaB:
    coloniaA*=(1+taxaA/100)
    coloniaB*=(1+taxaB/100)
    dias+=1
print(f'Vai levar {dias} dias para a colonia A ultrapassar ou igualar-se a colonia B')

'''Solução Alura:
# número inicial de bactérias
colonia_a = 4
colonia_b = 10

# taxas de crescimento das colônias
taxa_a = 0.03
taxa_b = 0.015

# contador de dias
dias = 0

# A condição que finaliza o laço é o caso em que
# a colônia A ultrapasse a colônia B
while colonia_a <= colonia_b:
  # usamos um operador de atribuição com multiplicação
  colonia_a *= 1 + taxa_a
  colonia_b *= 1 + taxa_b
  # contamos o dia para cada iteração
  dias += 1

# resultado final
print(f'Irá levar {dias} dias para a colônia A ultrapassar a colônia B.')
'''
