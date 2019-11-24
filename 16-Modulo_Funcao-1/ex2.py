#--- Exercício 2  - Funções - 1
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a soma entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

def soma():
    n1 = float(input('\nDigite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    result_soma = n1 + n2
    return print(f'\nO reseultada da soma dos números é: {result_soma}')

soma()