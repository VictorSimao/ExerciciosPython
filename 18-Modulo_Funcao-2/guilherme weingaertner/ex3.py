#--- Exercício 3 - Funções - 2
#--- Crie uma função para a impressão de um cabeçalho
#--- A função deve receber dois dados
#--- Um dado deve ser o nome do sistema
#--- O segundo dado deve ser o caracter que será multiplicado para fazer a linha de cabeçalho
#--- A impressão deve ser realizada utilizando f-string
#--- A função deve ser chamada informando os dois dados

from metodo_1 import cabecalho

n1 = input('Digite o nome do sistema:')
n2 = input('Digite o caracter que será multiplicado para fazer a linha de cabeçalho:')

print(f'{cabecalho(n2)}\n')
print(f'{n1}')
print(f'\n{cabecalho(n2)}')