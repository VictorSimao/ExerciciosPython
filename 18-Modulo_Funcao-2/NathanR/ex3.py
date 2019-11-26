#--- Exercício 3 - Funções - 2
#--- Crie uma função para a impressão de um cabeçalho
#--- A função deve receber dois dados
#--- Um dado deve ser o nome do sistema
#--- O segundo dado deve ser o caracter que será multiplicado para fazer a linha de cabeçalho
#--- A impressão deve ser realizada utilizando f-string
#--- A função deve ser chamada informando os dois dados

def cab(carac,sistema,carac2):
    return print(f'{carac}'*50,f'{sistema}',f'{carac2}'*50)

sistema = input('Digite o nome do sistema: ')
carac = input('Digite o caracter desejado: ')
carac2 = input('Digite novamente o caracter desejado: ')

cab(carac,sistema,carac2)


    