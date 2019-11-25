#--- Exercício 2  - Funções - 1
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a soma entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

n1 =int(input('Informe um numero'))
n2 =int(input('Informe outro numero'))

def soma(n1,n2):
    resultado = n1+n2
    return resultado

print(f'A soma entre {n1} e {n2} = {soma(n1,n2)}')    