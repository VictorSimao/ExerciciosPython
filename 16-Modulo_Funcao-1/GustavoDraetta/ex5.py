#--- Exercício 5 - Funções - 1
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console e armazene em uma variável
#--- Realize o calculo da raiz e armazene em uma segunda variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

# --- DEFs ---
def raiz():
    indice = int( input('Digite o indice da raiz :') )
    num = float( input('Digite um numero para ser tirada a raiz: ') )
    res  = num ** (1/indice)

    print(f'{num} raiz de {indice} é {res}')

raiz()
    