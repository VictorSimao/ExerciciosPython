#--- Exercício 2  - Funções - 1
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a soma entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

def numeross(num1,num2):
    resultado = num1 + num2
    return print (f'{num1} + {num2} = {resultado}')

num1 = int(input('Numero 1:'))
num2 = int(input('Numero 2:'))
numeross(num1,num2)

