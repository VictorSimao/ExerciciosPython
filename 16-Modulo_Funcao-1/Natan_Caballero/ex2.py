#--- Exercício 2  - Funções - 1
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a soma entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

print('='*50, '\n')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

r = n1 + n2
print(f'A some entre {n1} e {n2} é igual a {r}')

print('\n', '='*50)