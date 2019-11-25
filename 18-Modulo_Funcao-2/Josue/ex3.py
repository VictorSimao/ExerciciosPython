#--- Exercício 3 - Funções - 2
#--- Crie uma função para a impressão de um cabeçalho
#--- A função deve receber dois dados
#--- Um dado deve ser o nome do sistema
#--- O segundo dado deve ser o caracter que será multiplicado para fazer a linha de cabeçalho
#--- A impressão deve ser realizada utilizando f-string
#--- A função deve ser chamada informando os dois dados

from funcaoexe3 import cabecalho

nome = input('Qual nome do Sitema? ')
caract = input('Qual caracter que adicionar? ')

caract = cabecalho(caract)

print(f'{caract} \n  {nome} \n{caract} ')