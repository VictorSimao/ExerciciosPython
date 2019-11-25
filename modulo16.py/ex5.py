#--- Exercício 5 - Funções - 1
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console e armazene em uma variável
#--- Realize o calculo da raiz e armazene em uma segunda variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

def raiz ():
    a = int(input('Digite o valor que deseja obter a raiz do mesmo: '))
    b = int(input('Digite o o indice da raiz: '))
    rs_raiz = (a**(1/b))
    print(f'Com indice de:{b} o número:{a} tem raiz de: {rs_raiz}')

raiz()




