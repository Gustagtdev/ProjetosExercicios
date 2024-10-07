'''
Faça um programa que leia uma lista de lutadores que ganharam mais lutas no ano 
e verifique qual deles foi o que ganhou mais lutas
Todos eles lutaram 20 vezes.
'''
def contagemLutas():
    lutador1=0
    lutador2=0
    lutador3=0
    lutador4=0
    lutador5=0
    max_lutas=0
    lutador_mais_votado= None
    try:
        for i in range(0,20+1,1):
            aposta=int(input('Faça a sua aposta: '))
            if aposta==1:
                lutador1+=1
            elif aposta==2:
                lutador2+=1
            elif aposta==3:
                lutador3+=1
            elif aposta==4:
                lutador4+=1
            elif aposta==5:
                lutador5+=1
            else:
                print('Por favor,insira um lutador disponível !')
            if lutador1>max_lutas:
                lutador_mais_votado= 'lutador1'
                max_lutas=lutador1
            elif lutador2>max_lutas:
                lutador_mais_votado= 'lutador2'
                max_lutas=lutador2
            elif lutador3>max_lutas:
                lutador_mais_votado= 'lutador3'
                max_lutas=lutador3
            elif lutador4>max_lutas:
                lutador_mais_votado= 'lutador4'
                max_lutas=lutador4
            elif lutador5>max_lutas:
                lutador_mais_votado= 'lutador5'
                max_lutas=lutador5
    except ValueError:
        print('Por favor,insira um valor válido! (número inteiro)')
    
    return{'lutador1':lutador1,
           'lutador2': lutador2,
           'lutador3': lutador3,
           'lutador4': lutador4,
           'lutador5': lutador5,
           'lutador_mais_votado':lutador_mais_votado}
r= contagemLutas()

print(f'O Lutador 1 ganhou: {r['lutador1']} lutas')
print(f'O Lutador 2 ganhou: {r['lutador2']} lutas')
print(f'O Lutador 3 ganhou: {r['lutador3']} lutas')
print(f'O Lutador 4 ganhou: {r['lutador4']} lutas')
print(f'O Lutador 5 ganhou: {r['lutador5']} lutas')

print(f'O lutador que venceu mais lutas foi: O {r['lutador_mais_votado']}')
