#--- Exercício 5 - Funções - 1
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console e armazene em uma variável
#--- Realize o calculo da raiz e armazene em uma segunda variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

def calc(n1):
    perg = input('Qual Raiz deseja aplicar na conta? [1] Raiz Quadrada [2] Raiz Cubica: ')
    raiz_quadrada = n1 **(1/2)
    raiz_cubica = n1 ** (1/3)
    if perg == '1':
        print(f'A Raiz quadrada de {n1} é {raiz_quadrada:.0f}')
    if perg == '2':
        print(f'A Raiz cubica de {n1} é {raiz_cubica:.0f}')
    return(raiz_quadrada, raiz_cubica)

n1 = int(input('Digite um numero que queira descobrir a sua raiz: '))
calc(n1)

