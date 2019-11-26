#--- Exercício 2  - Funções - 1
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a soma entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

def somar(n1,n2):
    return n1,n2

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

print(f'A soma entre {n1} e {n2} resulta em {somar(n1,n2)}')