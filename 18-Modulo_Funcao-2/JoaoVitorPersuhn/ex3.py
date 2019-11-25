#--- Exercício 3 - Funções - 2
#--- Crie uma função para a impressão de um cabeçalho
#--- A função deve receber dois dados
#--- Um dado deve ser o nome do sistema
#--- O segundo dado deve ser o caracter que será multiplicado para fazer a linha de cabeçalho
#--- A impressão deve ser realizada utilizando f-string
#--- A função deve ser chamada informando os dois dados
def imprime(nome , caracter):
    print(caracter * 50, '\n')
    print('\t' * 2, f'Nome da empresa: {nome}')
    print('\n', caracter * 50)

nome = input('Digite o nome da empresa: ')
caracter = input('Digite o caracter do cabeçalho: ')
imprime(nome,caracter)