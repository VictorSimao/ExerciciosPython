#--- Exercício 3  - Variáveis
#--- Imprima dois parágrafos do último livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- As informações do Livro serão: 
#---    Título
#---    Edição
#---    Autor
#---    Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro

print('='*50, '\n'*3)
Titulo = 'Um Estudo em Vermelho'
Edicao = '1ª Edição'
Autor = 'Arthur Conan Doyle'
Data_publicacao = 'Data da Publicação: 1887'
Paragrafo = ''' 

    No ano de 1878, formei-me em medicina pela Universidade de Londres e logo parti
para Netley, a fim de seguir o curso exigido aos médicos militares. Terminados os meus
estudos, fui designado para o Quinto Regimento de Fuzileiros de Northumberland,
como cirurgião assistente. Nessa época, o Quinto estava acantonado na Índia, e antes
que eu pudesse me apresentar eclodiu a Segunda Guerra Afegã. Ao desembarcar em
Bombaim, soube que o meu regimento já havia atravessado os desfiladeiros e se achava
embrenhado em território inimigo. Tomei o mesmo caminho, com muitos outros oficiais
que estavam em idêntica situação, e consegui chegar são e salvo a Kandahar, onde
encontrei minha unidade e imediatamente assumi minhas novas funções. 

     A campanha trouxe honras e promoções para muitos, mas a mim só proporcionou
infortúnios e desastres. Fui transferido da minha brigada para as tropas de Berkshire,
com as quais tomei parte na fatídica Batalha de Maiwand. Ali, a bala de um mosquete
afegão atingiu-me o ombro, fraturando o osso e raspando a artéria subclávica. Teria
caído nas mãos dos ferozes ghazis, se não fosse a devoção e a coragem do ordenança
Murray, que me pôs num cavalo de carga e conseguiu levar-me são e salvo para as
linhas britânicas. 

'''
print('\t', Titulo, '\n', '\t', Edicao, '\n', '\t', Autor, '\n', '\t', Data_publicacao, '\n',)
print(Paragrafo)
print('\n'*3, '='*50)