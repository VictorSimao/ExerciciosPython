#--- Exercicio 1  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia dois números inteiros
#--- Realize as 4 operações matemáticas básicas com os números lidos
#--- Imprima os resultados das operações
#--- Informe qual número é maior ou se os dois são iguais

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print(f'{n1} + {n2} = {n1+n2}')
print(f'{n1} - {n2} = {n1-n2}')
print(f'{n1} x {n2} = {n1*n2}')
print(f'{n1} ÷ {n2} = {n1/n2}')

if n1>n2:
    print(f'O maior número é o {n1}')
elif n2>n1:
    print(f'O maior número é o {n2}')
else:
    print('Os números são iguais')