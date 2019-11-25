#--- Exercício 2  - Funções - 1
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a soma entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

def soma():
    n1= int(input('Digite um numero'))
    n2= int(input('Digite um numero'))
    n3 = n1+n2
    return print(f'A soma de {n1}+{n2}={n3}')
soma()