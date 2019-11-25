#--- Exercício 3  - Variáveis
#--- Imprima dois parágrafos do último livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- As informações do Livro serão: 
#---    Título
#---    Edição
#---    Autor
#---    Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro

titulo = "Uma noite na Taverna"
edicao = "1º"
autor = "Alvares de Azevedo"
publicação = 1855

paragrafo = """\tA mulher recuava... recuava. O moço tomou-a nos braços, pregou os lábios nos dela... Ela deu um
grito e caiu-lhe das mãos. Era horrível de se ver. O moço tomou o punhal, fechou os olhos, apertou-o no
peito, e caiu sobre ela. Dois gemidos sufocaram-se no estrondo do baque de um corpo...
\n\tA lâmpada apagou-se."""

print('=' * 103 + "\n")
print(paragrafo + "\n" * 2)
print('=' * 103)
print(f'Informações do livro: \n\tTitulo: {titulo}\n\tEdição: {edicao}\n\tAutor: {autor}\n\tData de publicação: {publicação}')
print('=' * 103)