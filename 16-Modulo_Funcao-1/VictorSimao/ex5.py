#--- Exercício 5 - Funções - 1
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console e armazene em uma variável
#--- Realize o calculo da raiz e armazene em uma segunda variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

def raiz():
    indice = int(input('Digite o indice da raiz: '))
    numero = int(input('Digite um número: '))
    raiz = numero**(1/indice)
    print(f'{numero} raiz de {indice} é {raiz}')

raiz()