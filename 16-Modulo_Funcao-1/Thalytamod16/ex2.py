#--- Exercício 2  - Funções - 1
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a soma entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

def calc_soma ():
    num1 = int(input('Digite um numero:'))
    num2 = int(input('Digite outro numero:'))
    resultado = num1 + num2
    print (f'A soma de {num1} e {num2} é igual a {resultado}')

(calc_soma())