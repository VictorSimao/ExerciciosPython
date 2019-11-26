#--- Exercício 3 - Funções - 2
#--- Crie uma função para a impressão de um cabeçalho
#--- A função deve receber dois dados
#--- Um dado deve ser o nome do sistema
#--- O segundo dado deve ser o caracter que será multiplicado para fazer a linha de cabeçalho
#--- A impressão deve ser realizada utilizando f-string
#--- A função deve ser chamada informando os dois dados

def cabecalho(nome,caracter):
    resultado = (caracter*15)+nome+(caracter*15)
    return resultado

nome = input("Digite o nome do sistema: ")
caracter = input("Digite o caracter a ser multiplicado: ")

print(f'{cabecalho(nome,caracter)}')