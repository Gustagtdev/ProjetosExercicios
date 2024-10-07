'''
Crie um código que solicita 3 notas de um estudante e imprima a média das notas.
'''
nota1=float(input('Digite a 1°nota: '))

while not (0<=nota1<=10):
    print('Por favor insira uma nota no valor de 1 a 10: ')
    nota1=float(input('Digite a 1°nota: '))


nota2=float(input('Digite a 2°nota: '))

while not (0<=nota2<=10):
    print('Por favor insira uma nota no valor de 1 a 10: ')
    nota2=float(input('Digite a 2°nota: '))


nota3=float(input('Digite a 3°nota: '))

while not (0<=nota3<=10):
    print('Por favor insira uma nota no valor de 1 a 10: ')
    nota3=float(input('Digite a 3°nota: '))


soma= nota1+nota2+nota3
media= soma/ 3
print(f'A soma é: {soma}\nPortanto a média é: {media:.2f}')

