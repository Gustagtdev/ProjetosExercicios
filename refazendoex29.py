'''
Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite")
e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso
'''
turno= str(input('Você estuda em qual turno?(M/T/N): '))

if turno.lower() and turno.upper()== 'M':
    print('Bom dia!')
elif turno.lower() and turno.upper()=='T':
    print('Boa Tarde!')
elif turno.lower() and turno.upper()=='N':
    print('Boa noite!')
else:
    print('Valor inválido!')