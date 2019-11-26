#--- Exercício 2  - Funções - 1
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a soma entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

def calcular ():
    n1=int(input('digite um numero: '))
    n2=int(input('digite outro numero: '))
    res=n1+n2
    print(f'o resultado de {n1} + {n2} é = {res}')
calcular ()