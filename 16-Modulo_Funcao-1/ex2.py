#--- Exercício 2  - Funções - 1
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a soma entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

def calcula_soma():
    x = float(input('Informe o primeiro número\n'))
    y = float(input('Informe o segundo número\n'))
    resultado = x + y
    print(f'{x} + {y} = {resultado}')

calcula_soma()