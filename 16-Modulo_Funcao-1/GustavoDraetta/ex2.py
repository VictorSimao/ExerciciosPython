#--- Exercício 2  - Funções - 1
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a soma entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

def read_num():
    num1 = int( input('Digite um numero: ') )
    num2 = int( input('Digite um numero: ') )
    
    result = num1 + num2
    
    print(f'{num1} + {num2} = {result}')

    return 0

print('='*50)
read_num()
print('='*50)

