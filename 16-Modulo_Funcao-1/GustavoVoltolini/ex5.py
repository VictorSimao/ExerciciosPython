#--- Exercício 5 - Funções - 1
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console e armazene em uma variável
#--- Realize o calculo da raiz e armazene em uma segunda variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

def raiz():
    indc = int(input('Qual o indice da raiz:'))
    num = float(input('Digite o numero:'))
    raiz = num ** (1/indc)
    print (f'Numero:{num}\nIndice:{indc}\nRaiz={raiz:2.2f}')

raiz()
