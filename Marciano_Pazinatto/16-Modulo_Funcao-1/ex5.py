#--- Exercício 5 - Funções - 1
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console e armazene em uma variável
#--- Realize o calculo da raiz e armazene em uma segunda variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)
numero=int(input('Digite um número: '))
valor=int(input('Digite o tipo de raiz: '))
raiz=numero**(1/valor)

print(f'O número {numero} calculando a raiz de {valor} é igual a {raiz}')