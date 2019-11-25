#--- Exercício 2  - Funções - 1
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a soma entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)


v1 = ''
v2 = ''

def soma (v1,v2):
    v1 = int(input('Digite numero 1: '))
    v2 = int(input('Digite numero 2: '))
    resultado = v1 + v2
    return resultado

resultado = soma(v1,v2)

print(f'A soma de {v1} + {v2} é {resultado}')
