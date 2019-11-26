#--- Exercício 3 - Funções - 2
#--- Crie uma função para a impressão de um cabeçalho
#--- A função deve receber dois dados
#--- Um dado deve ser o nome do sistema
#--- O segundo dado deve ser o caracter que será multiplicado para fazer a linha de cabeçalho
#--- A impressão deve ser realizada utilizando f-string
#--- A função deve ser chamada informando os dois dados

def imprimir(nome, caractere):
    string = f"{caractere*50}\n\n\t{nome}\n\n{caractere*50}"
    return string

nome = input("Nome da empresa: ")
caractere = input("Insira o caractere: ")

string = imprimir(nome, caractere)

print(f'{string}')