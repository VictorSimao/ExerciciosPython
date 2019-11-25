#--- Exercício 1 - Funções - 2
#--- Crie um função que receba duas variáveis
#--- Calcule a multiplicação entre as duas variáveis e atribua o resultado em uma terceira variável
#--- Imprima o resultado juntamente com uma frase utilizando f-string
#--- Faça a leitura de dois números inteiros fora da função e atribua a duas variáveis
#--- Realize a chamada da função passando os dois valores lidos do console

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))
def numeros(n1, n2):
    mult = n1 * n2
    return mult

mengao = numeros(n1, n2)
print(f'A multiplicação entre {n1} * {n2} = {mengao:0.2f}')