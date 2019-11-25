#--- Exercício 3 - Funções - 2
#--- Crie uma função para a impressão de um cabeçalho
#--- A função deve receber dois dados
#--- Um dado deve ser o nome do sistema
#--- O segundo dado deve ser o caracter que será multiplicado para fazer a linha de cabeçalho
#--- A impressão deve ser realizada utilizando f-string
#--- A função deve ser chamada informando os dois dados

def cabecalho(nome,caracter):
    return print(f'{caracter}'*50,f'\n \t{nome}')

nome = input('Digite o nome da empresa')
caracter= input('Digite o caracter a ser usado no cabeçalho')
cabecalho(nome,caracter)