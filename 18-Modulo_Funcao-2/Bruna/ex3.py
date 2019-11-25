#--- Exercício 3 - Funções - 2
#--- Crie uma função para a impressão de um cabeçalho
#--- A função deve receber dois dados
#--- Um dado deve ser o nome do sistema
#--- O segundo dado deve ser o caracter que será multiplicado para fazer a linha de cabeçalho
#--- A impressão deve ser realizada utilizando f-string
#--- A função deve ser chamada informando os dois dados

def c(cab,sis):
    # print(cab* 50 ) 
    # print(sis)
    print(f'{cab*50}\n{sis}\n{cab*50}')

c('-','.: N O M E   D O   S I S T E M A :.')

    