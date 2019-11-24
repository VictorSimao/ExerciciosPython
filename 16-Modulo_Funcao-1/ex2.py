#--- Exercício 2  - Funções - 1
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a soma entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

def calcula_soma(x , y):
    resultado = x + y
    return(resultado)

x = int(input('Informe o primeiro número\n'))
y = int(input('Informe o segundo número\n'))

resultado = calcula_soma(x , y)
print(f'{x} + {y} = {resultado}')