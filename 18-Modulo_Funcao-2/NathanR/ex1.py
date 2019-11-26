#--- Exercício 1 - Funções - 2
#--- Crie um função que receba duas variáveis
#--- Calcule a multiplicação entre as duas variáveis e atribua o resultado em uma terceira variável
#--- Imprima o resultado juntamente com uma frase utilizando f-string
#--- Faça a leitura de dois números inteiros fora da função e atribua a duas variáveis
#--- Realize a chamada da função passando os dois valores lidos do console

def multiplicação(numero1, numero2):
        resultado = numero1 * numero2
        print(f'O resultado da multiplicacao é {resultado}')
    
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
multiplicação(n1, n2)
