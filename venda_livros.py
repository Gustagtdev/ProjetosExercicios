livro = {
    'titulo': 'Aprendendo Python',
    'autor': 'Fabrício Silva',
    'ISBN': '12345',
    'preco': 59.90,
    'em_estoque': True
}
livro['preco']= 69.90
print(livro)

''' Outra forma de validar a atualização do preço do livro
livro.update({'preco': 69.90})
'''
