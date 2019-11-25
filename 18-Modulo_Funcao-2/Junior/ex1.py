#--- Exercício 1 - Funções - 2
#--- Crie um função que receba duas variáveis
#--- Calcule a multiplicação entre as duas variáveis e atribua o resultado em uma terceira variável
#--- Imprima o resultado juntamente com uma frase utilizando f-string
#--- Faça a leitura de dois números inteiros fora da função e atribua a duas variáveis
#--- Realize a chamada da função passando os dois valores lidos do console


def mult(n1,n2):
    multi = n1*n2
    return multi

a = int(input('Digite um numero: '))
b = int(input('Digite outro valor: '))
print(f'A multiplicação entre {a} e {b} é igual a : {mult(a,b)}')