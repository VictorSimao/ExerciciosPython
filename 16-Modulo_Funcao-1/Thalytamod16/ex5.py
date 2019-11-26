#--- Exercício 5 - Funções - 1
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console e armazene em uma variável
#--- Realize o calculo da raiz e armazene em uma segunda variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

def calc_raiz (num1, indice):
    res = num1**(1/indice)
    print (f'Raiz de {num1} por {indice} é igual {res}')

numero = int(input('Digite um numero: '))
ind_raiz = int(input('Digite o indice da raiz: '))
calc_raiz(numero, ind_raiz)