#--- Exercício 1 - Funções - 2
#--- Crie um função que receba duas variáveis
#--- Calcule a multiplicação entre as duas variáveis e atribua o resultado em uma terceira variável
#--- Imprima o resultado juntamente com uma frase utilizando f-string
#--- Faça a leitura de dois números inteiros fora da função e atribua a duas variáveis
#--- Realize a chamada da função passando os dois valores lidos do console

def conta(n1,n2):
    mult=n1*n2
    return mult

n1=int(input('Digite o primeiro número: '))
n2=int(input('Digite o segundo número: '))

print(f'A multiplicação de {n1} * {n2} = {conta(n1,n2)}')