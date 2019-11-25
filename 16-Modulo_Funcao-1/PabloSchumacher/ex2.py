#--- Exercício 2  - Funções - 1
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a soma entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

def calc(n1,n2):
    r = (n1+n2)
    return r

rcalc = calc(n1,n2)
print(f'A soma entre {n1} e {n2} é de {rcalc}')