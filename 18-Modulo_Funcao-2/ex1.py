#--- Exercício 1 - Funções - 2
#--- Crie um função que receba duas variáveis
#--- Calcule a multiplicação entre as duas variáveis e atribua o resultado em uma terceira variável
#--- Imprima o resultado juntamente com uma frase utilizando f-string
#--- Faça a leitura de dois números inteiros fora da função e atribua a duas variáveis
#--- Realize a chamada da função passando os dois valores lidos do console

def multiplicacao(a , b):
    multiplicacao = a * b
    return print(f'{a} x {b} = {multiplicacao}')

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))

multiplicacao(a , b) 

