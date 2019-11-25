#--- Exercício 1 - Funções - 2
#--- Crie um função que receba duas variáveis
#--- Calcule a multiplicação entre as duas variáveis e atribua o resultado em uma terceira variável
#--- Imprima o resultado juntamente com uma frase utilizando f-string
#--- Faça a leitura de dois números inteiros fora da função e atribua a duas variáveis
#--- Realize a chamada da função passando os dois valores lidos do console

def mult(num1,num2):
    multi = num1 * num2
    return print (f'{num1} * {num2} = {multi}')

num1 = float(input('Numero: '))
num2 = float(input('Numero: '))
mult(num1,num2)
