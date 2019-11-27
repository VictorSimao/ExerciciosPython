#--- Exercício 3 - Funções - 2
#--- Crie uma função para a impressão de um cabeçalho
#--- A função deve receber dois dados
#--- Um dado deve ser o nome do sistema
#--- O segundo dado deve ser o caracter que será multiplicado para fazer a linha de cabeçalho
#--- A impressão deve ser realizada utilizando f-string
#--- A função deve ser chamada informando os dois dados
def cabecalho (sistema,caracter):
    print(f'{caracter*20} {sistema} {caracter*20}')


sistema = input('digite o nome do sistema: ')
caracter = input('digite o caracter: ')
cabecalho(sistema,caracter)
