#--- Exercício 3  - Variáveis
#--- Imprima dois parágrafos do último livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- As informações do Livro serão: 
#---    Título
#---    Edição
#---    Autor
#---    Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro

print('='*50, '\n')

Titulo = 'Good Omens'
Edicao = '1'
Autor = 'Neil Gaiman'
Publicacao = '1 de maio de 1990'


print(f'''E VOCÊ QUER IMAGINAR o futuro, imagine um garoto, seu cachorro e seus
amigos. E um verão que jamais termina.
E, se você quer imaginar o futuro, imagine uma bota... não, imagine um tênis,
cadarços se arrastando no chão, chutando uma pedrinha; imagine um graveto,
para mexer em coisas interessantes e ser atirado para um cão que pode ou não
decidir apanhá-lo; imagine um assobio sem melodia, martelando uma música po‐
pular desafortunada até a indiferença; imagine uma figura, meio anjo, meio
demônio, inteiramente humana...
Andando confiante e preguiçosamente em direção a Tadfield...
... para sempre.
\n O título é {Titulo}\n É a edição número {Edicao}\n O autor é {Autor}\n A data de publicação foi {Publicacao}''')

print('\n', '='*50)
