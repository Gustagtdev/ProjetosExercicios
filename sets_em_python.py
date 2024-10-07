'''Sets em Python:

O que são sets?: Coleção de dados não ordenada
Característica dos sets: Não permite duplicatas

É uma estrutura de Dados built-in do Python

'''
'''
carros={'Corolla','Versa','Gol','Hilux','Fusca'}
print(carros)
#Sets com elementos diferentes:
elementos_diferentes= {2020,'Compass',12543.56,True}
print(elementos_diferentes)
Não da para saber qual é o elemento através do índice por conta que o set é uma lista não ordenada
carros[0]

#Forma de mostrar os elementos de maneira individual
for i in carros:
    print(i)
'''
#Criando sets a partir de listas:
'''
lista_escolas= ['Programação','Data Science','UI/UX Design','Mobile','DevOps']

escolas_set= set(lista_escolas)

print(escolas_set)
'''
#Trabalhando com elementos repetidos:
'''
carros=['Corolla','Versa','Versa','Corolla','Gol','Gol','Hilux','Hilux','Fusca','Fusca']

#Utilizando a função len() para verificar a quantidade de elementos
print(len(carros))
#Conversão de lista para set
nova_lista= set(carros)
print(len(nova_lista))
'''
'''Operações com sets:
Sets podem ser como os conjuntos da matemática.
Operações: disjunção,união,interseção.
Exemplo:
'''

acessorios_passat={'Rodas de liga','Travas elétricas','Piloto automático','Central multimídia'}
#print(acessorios_passat)

acessorios_crossfox={'Piloto automático','Teto panorâmico','4 X 4','Central multimídia'}
#print(acessorios_crossfox)

acessorios_jetta={'Controle de estabilidade','Câmbio automático','Travas elétricas','Rodas de liga'}
#print(acessorios_jetta)

#Disjunção: Dois conjuntos são disjuntos se eles não possuem nenhum elemento em comum.

#print(set.isdisjoint(acessorios_crossfox,acessorios_passat))

#Interseção: Retorna os elementos em comum em dois conjuntos.
#Maneira que funcionou.
'''
intersecao= acessorios_passat & acessorios_crossfox
intersecao2= acessorios_passat & acessorios_jetta
print(intersecao)
print(intersecao2)
#Tentando resolver o problema do set.intersection:
print(set.intersection(acessorios_passat,acessorios_crossfox))#Resolvido(funcionou com dois conjuntos)
inter= set.intersection(acessorios_passat,acessorios_crossfox)#Resolvido(funcionou com dois conjuntos)
print(inter)
#Tentativa com 3 conjuntos:
#Teste 01: Atribuindo o set há uma variável
inter3= set.intersection(acessorios_crossfox,acessorios_jetta,acessorios_passat)
print(inter3)
Output: set() -> Certo,pois os elementos nos 3 conjuntos não possuem uma característica
em comum ao mesmo tempo
#Teste 02: Fazendo um print na função set.intersection:
print(set.intersection(acessorios_crossfox,acessorios_jetta,acessorios_passat))
Output: set() -> Certo,pois os elementos nos 3 conjuntos não possuem uma característica
em comum ao mesmo tempo
'''
#União: Representa a junção de todos os elementos de dois conjuntos:
'''
uniao= acessorios_passat | acessorios_crossfox
print(uniao) 
uniao_total= set.union(acessorios_jetta,acessorios_crossfox,acessorios_passat,{'Teto Solar'})
print(uniao_total)
print(set.union(acessorios_jetta,acessorios_crossfox,acessorios_passat,{'Teto Solar'}))
'''
#Todos os exemplos acima sobre união funcionaram como previsto.
'''
#Performance em sets: 
carros={'Corolla','Versa','Gol','Hilux','Fusca'}
print(carros)
if 'Corolla' in carros: 
    print('Corolla')
else:
    print('O carro não está na lista!')
'''
#Perfomace com vários elementos: Vá no arquivo ipynb