#--- Exercício 3  - Variáveis
#--- Imprima dois parágrafos do último livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- As informações do Livro serão: 
#---    Título
#---    Edição
#---    Autor
#---    Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro

Título = input('Digite o titulo: ')
Edição = input('Digite a edição: ')
Autor = input('Digite o autor: ')
Data_de_publicação = input('digite a data de publicação: ')

print('='*80,'\n')
print(f'Titulo: {Título}')
print(f'Edição: {Edição}')
print(f'Autor: {Autor}')
print(f'data de publicação: {Data_de_publicação}')
print('\n','='*80)