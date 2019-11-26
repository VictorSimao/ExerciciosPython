#--- Exercício 1 - Funções - 2
#--- Crie um função que receba duas variáveis
#--- Calcule a multiplicação entre as duas variáveis e atribua o resultado em uma terceira variável
#--- Imprima o resultado juntamente com uma frase utilizando f-string
#--- Faça a leitura de dois números inteiros fora da função e atribua a duas variáveis
#--- Realize a chamada da função passando os dois valores lidos do console

def calcular(n1,n2):
    resultado = n1 * n2
    print(f'O resultado entre  {n1} * {n2} é {resultado}')



n1 = int(input('digite um número: '))
n2 = int(input('digite outro número: '))
calcular(n1,n2)