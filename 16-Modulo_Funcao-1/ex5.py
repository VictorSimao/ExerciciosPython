#--- Exercício 5 - Funções - 1
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console e armazene em uma variável
#--- Realize o calculo da raiz e armazene em uma segunda variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

def raiz():
    indice = int(input('\nDigite o indice: '))
    radicando = int(input('Digite o radicando: '))
    resultado = radicando ** (1/indice)
    return print(f'\nO resulto da raíz é entre os dois números é: {resultado}')

raiz()