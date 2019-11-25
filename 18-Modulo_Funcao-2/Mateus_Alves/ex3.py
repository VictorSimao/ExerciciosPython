#--- Exercício 3 - Funções - 2
#--- Crie uma função para a impressão de um cabeçalho
#--- A função deve receber dois dados
#--- Um dado deve ser o nome do sistema
#--- O segundo dado deve ser o caracter que será multiplicado para fazer a linha de cabeçalho
#--- A impressão deve ser realizada utilizando f-string
#--- A função deve ser chamada informando os dois dados

def imprimir(n,sistema):
    print(n*50 ,'\n'*3)
    print(f'Nomedo do Sistema: {sistema}')
    print('\n'*3)
    print(n*50)

n = input(' Qual qual simbulo quer que esteja no cabeçalho ' )
sistema = input('Informe o nome do Sistema')

imprimir(n,sistema)