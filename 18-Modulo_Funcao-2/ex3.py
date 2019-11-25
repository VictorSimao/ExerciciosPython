#--- Exercício 3 - Funções - 2
#--- Crie uma função para a impressão de um cabeçalho
#--- A função deve receber dois dados
#--- Um dado deve ser o nome do sistema
#--- O segundo dado deve ser o caracter que será multiplicado para fazer a linha de cabeçalho
#--- A impressão deve ser realizada utilizando f-string
#--- A função deve ser chamada informando os dois dados

def header(sistema, char):
    print(f'{char*55}\n{sistema}\n{char*55}\n')
    return ''

sistema = '\nHB\n'
char = '#'

header(sistema, char)