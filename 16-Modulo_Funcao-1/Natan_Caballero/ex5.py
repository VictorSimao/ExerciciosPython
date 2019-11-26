#--- Exercício 5 - Funções - 1
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console e armazene em uma variável
#--- Realize o calculo da raiz e armazene em uma segunda variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

from metodos import raiz

print('='*50, '\n')


n = int(input('Digite um núero: '))
n1 = int(input('Digite um número: '))

print(f'A raiz {n1} de {n} é {raiz(n,n1)}')

print('\n', '='*50)
