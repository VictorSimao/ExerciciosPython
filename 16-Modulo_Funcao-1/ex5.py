#--- Exercício 5 - Funções - 1
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console e armazene em uma variável
#--- Realize o calculo da raiz e armazene em uma segunda variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)


def raiz(numero , indice):
    raiz = numero**(1/indice)
    return(raiz)

numero = float(input('Informe um número: '))
indice = float(input('Informe o índice da raiz: '))

print(f'A Raiz de {numero}, sendo seu indice {indice} é {raiz(numero,indice):.5f}')    

