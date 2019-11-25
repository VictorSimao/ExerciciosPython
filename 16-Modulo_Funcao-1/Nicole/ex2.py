#--- Exercício 2  - Funções - 1
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a soma entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

def numeros ():
    n1=int(input('Digite o primeiro numero: '))
    n2=int(input('Digite o segundo numero: '))
    soma=n1+n2
    print(f'A soma dos numeros {n1} e {n2} é {soma}')

numeros()