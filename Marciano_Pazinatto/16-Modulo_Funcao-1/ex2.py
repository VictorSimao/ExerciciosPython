#--- Exercício 2  - Funções - 1
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a soma entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)
num1=float(input('Digite o primeiro número: '))
num2=float(input('Digite o segundo número: '))
soma=num1+num2
print(f'A soma dos números {num1} + {num2} = {soma:.2f}')