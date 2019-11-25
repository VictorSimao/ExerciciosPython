#--- Exercício 3  - Variáveis
#--- Imprima dois parágrafos do último livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- As informações do Livro serão: 
#---    Título
#---    Edição
#---    Autor
#---    Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro

tit = input("Digite o nome do livro: ")
edicao = input('Digite a edição do livro: ')
autor = input('Digite o nome do auto: ')
datap = input('Digite a data de publicação: ')

print(f'\nTitulo: {tit} \nEdição: {edicao} \nAutor: {autor} \nData de publicação: {datap}')