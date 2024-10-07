'''
2) Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento
(porcentagem positiva) ou decrescimento (porcentagem negativa).
'''

producao= float(input('Informe o percentual de produção da empresa: '))

if producao>0:
    print(f'Houve um crescimento de {producao}% na produção da empresa')
elif producao<0:
    print(f'Houve um decrescimento de {producao}% na produção da empresa')
else: 
    print('O percentual de produção da empresa continua o mesmo!')