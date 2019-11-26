#--- Exercício 3  - Funções - 1
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)
#--- Deve ser impresso apenas duas cadas após a vírgula

print('='*50, '\n')

from metodos import media

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite outro número: '))

print(f'A média entre os tres números é igual a {media(n1, n2, n3):.2f}')

print('\n', '='*50)
