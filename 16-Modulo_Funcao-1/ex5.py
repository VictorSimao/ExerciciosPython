#--- Exercício 5 - Funções - 1
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console e armazene em uma variável
#--- Realize o calculo da raiz e armazene em uma segunda variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

n = float(input('Informe o número: '))
tipo = int(input('Informe o tipo de raiz: '))

def raiz(n,tipo):
    r = n**(1/tipo)
    return r

rraiz = raiz(n,tipo)
print ('\n',f'A raiz {tipo} de {n} é {rraiz}')