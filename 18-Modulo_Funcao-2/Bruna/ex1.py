#--- Exercício 1 - Funções - 2
#--- Crie uma função que receba duas variáveis
#--- Calcule a multiplicação entre as duas variáveis e atribua o resultado em uma terceira variável
#--- Imprima o resultado juntamente com uma frase utilizando f-string
#--- Faça a leitura de dois números inteiros fora da função e atribua a duas variáveis
#--- Realize a chamada da função passando os dois valores lidos do console


def mult(n1_fun,n2_fun):
    res_mult = n1_fun * n2_fun
    return res_mult

n1= int(input('Digite um numero inteiro: '))
n2= int(input('Digite outro numero inteiro: ')) 

print(f'O resultado da multiplicação entre {n1} e {n2} é: {mult(n1,n2)}')