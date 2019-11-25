#--- Exercício 2  - Funções - 1
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a soma entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)
def cal():
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro numero: '))
    soma = n1 + n2
    return (soma)

print(f'A soma entre os numeros é: {cal()}')