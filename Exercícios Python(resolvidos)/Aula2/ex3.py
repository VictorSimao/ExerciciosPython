#--- Exercicio 3  - Variávies e impressão com interpolacão de string
#--- Imprima dois paragráfos do ultimo livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- Livro: Título, Edição, Autor, Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro

print('''\nPRIMEIRO PARÁGRAFO\n Hugo, um pacote para você! gritou Alberto, recebendo um pequeno
embrulho das mãos do carteiro. Assinou o nome do irmão no papelzinho e
foi levar-lhe a encomenda.''')

print('''\nSEGUNDO PARÁGRAFO\n Hugo, que acabara de fazer a barba, mirava-se no espelho, ensaiando
olhares longos e fatais para lançar às garotas na primeira oportunidade. O
cristal refletia um rosto sardento de dezoito anos, extremamente simpático e
sadio, aureolado por cabelos tão vermelhos que o moço era conhecido por
"Foguinho".''')

nome = input('\nDigite o nome do livro: ')
edicao = input('Digite a edição do livro: ')
autor = input('Digite o autor do livro: ')
data = input('Digite a data de publicação do livro: ')

print(f'\nNome do Livro: {nome}\nEdição do Livro: {edicao}\nAutor do Livro: {autor}\nData de Publicação: {data}')