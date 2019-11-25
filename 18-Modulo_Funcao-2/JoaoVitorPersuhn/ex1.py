#--- Exercício 1 - Funções - 2
#--- Crie um função que receba duas variáveis
#--- Calcule a multiplicação entre as duas variáveis e atribua o resultado em uma terceira variável
#--- Imprima o resultado juntamente com uma frase utilizando f-string
#--- Faça a leitura de dois números inteiros fora da função e atribua a duas variáveis
#--- Realize a chamada da função passando os dois valores lidos do console
def calcula(n1 : float, n2 : float):
    return n1 * n2

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
resultado = calcula(n1,n2)
print(f'O resultado da multiplicação entre {n1} e {n2} é {resultado}')