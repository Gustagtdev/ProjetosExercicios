'''
Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa,
precisamos verificar se as notas são válidas.
Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados
e verificar se é um valor válido.
Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita
até que a pessoa usuária insira um valor válido.
'''
'''Minha solução:
'''
for i in range(1,15+1):
    notas= float(input(f'Digite uma avaliação de 0 a 5 do usuário {i}: '))
    if 0<=notas<=5:
        continue
    else:
        notas= float(input(f'Nota inválida, insira novamente a nota da pessoa usuária {i}: '))
print('Verificação completa.Todas as notas são válidas!')
print(f'Total de avaliações: {i}')

'''
Solução Alura:
# laço para pegar as 15 notas
for i in range(1,15+1):
  nota = float(input(f'Insira a nota da pessoa usuária {i}: '))

  # verifica se a nota está entre 0 e 5
  # se estiver, o laço rodará ininterruptamente até ser obtido um valor válido
  while (nota < 0) or (nota > 5):
    nota = float(input(f'Nota inválida, insira novamente a nota da pessoa usuária {i}: '))

print('Verificação feita. Todas as notas são válidas')
'''