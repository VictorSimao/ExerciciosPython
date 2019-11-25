#--- Exercício 3 - Funções - 2
#--- Crie uma função para a impressão de um cabeçalho
#--- A função deve receber dois dados
#--- Um dado deve ser o nome do sistema
#--- O segundo dado deve ser o caracter que será multiplicado para fazer a linha de cabeçalho
#--- A impressão deve ser realizada utilizando f-string
#--- A função deve ser chamada informando os dois dados


def informação_dois_dados():
    nome = input('Nome do sistema:')
    carc = input('Caracter:')
    print(f'{carc}'*50    ,"\n" + f'{nome}' ,    "\n" + f'{carc}'*50)

informação_dois_dados()