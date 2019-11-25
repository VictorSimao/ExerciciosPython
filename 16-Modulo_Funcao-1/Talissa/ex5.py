#--- Exercício 5 - Funções - 1
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console e armazene em uma variável
#--- Realize o calculo da raiz e armazene em uma segunda variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite o indice da raiz: '))

def raiz(n1,n2):
    raiz = n1 * (1/n2)
    return raiz

raiz = raiz(n1,n2)

print(f'A raiz é: {raiz}')