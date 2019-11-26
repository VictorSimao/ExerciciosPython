#--- Exercício 5 - Funções - 1
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console e armazene em uma variável
#--- Realize o calculo da raiz e armazene em uma segunda variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)
n1 =0
n2 =0

def raiz(n1,n2):
    n1 = int(input('Digite o numero: '))
    n2 = int(input('Digite o indice da raiz: '))
    n3 = n1 ** (1/n2)
    return print(f'{n3}')


raiz(n1,n2)