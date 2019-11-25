#--- Exercício 1 - Funções - 2
#--- Crie um função que receba duas variáveis
#--- Calcule a multiplicação entre as duas variáveis e atribua o resultado em uma terceira variável
#--- Imprima o resultado juntamente com uma frase utilizando f-string
#--- Faça a leitura de dois números inteiros fora da função e atribua a duas variáveis
#--- Realize a chamada da função passando os dois valores lidos do console

def mult (a,b):
    rs = (a*b)
    print(f'O resultado dará um total de: {rs}')
v1 = float(input('Digite o primeiro  número a ser multiplicado: '))
v2 = float(input('Digite o número que será usado para ser multiplicado com o primeiro: '))


mult(v1, v2)





