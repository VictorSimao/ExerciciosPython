#--- Exercício 2  - Funções - 1
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a soma entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

def calcular():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    resultado = n1 + n2
    print(f'O resultado de {n1} + {n2} é = resultado {resultado}')

calcular()