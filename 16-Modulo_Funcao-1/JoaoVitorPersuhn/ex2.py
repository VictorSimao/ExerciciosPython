#--- Exercício 2  - Funções - 1
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a soma entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)
def soma(n1 : float, n2 : float):
    return n1 + n2

def leNumeros():
    n1 = float(input('Digite o valor do primeiro numero: '))
    n2 = float(input('Digite o valor do segundo numero: '))
    resultado = soma(n1, n2)
    print(f'O resultado da soma entre {n1} e {n2} é {resultado}')

leNumeros()