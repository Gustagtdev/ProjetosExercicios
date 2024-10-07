'''
Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas.
A leitura deve ser encerrada ao ser enviado o valor -273°C.
'''
temp= float(input('Insira uma temperatura em Celsius: '))
soma=0
contadora=0

while temp != -273:
    soma+=temp
    contadora+=1
    temp= float(input('Insira uma temperatura em Celsius: '))

media= soma/contadora

media_final=round(media,2)

print(f'A média das temperaturas é: {media_final}')


