'''
2)Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria
A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de
crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.
'''

colonia_a= 4 
colonia_b= 10
taxa_a = 3
taxa_b= 1.5
dias=0
while colonia_a <=colonia_b:
    colonia_a*= (1+taxa_a/100)
    colonia_b*= (1+taxa_b/100)
    dias+=1

print(f'A colônia A vai ultrapassar ou igualar-se a colônia B em {dias} dias')