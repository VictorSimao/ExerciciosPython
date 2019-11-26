#--- Exercício 2  - Funções - 1
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a soma entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

# def soma (numero1, numero2, resultado):
#     resultado = numero1 + numero2
#     return resultado

# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))
#soma(n1,n2,r)
# print(f'{n1} + {n2} = {r}')


def soma (n1,n2):
    return n1 + n2

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print(f'{n1} + {n2} = {soma(n1,n2)}')