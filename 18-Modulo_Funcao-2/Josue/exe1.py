#--- Exercício 1 - Funções - 2
#--- Crie um função que receba duas variáveis
#--- Calcule a multiplicação entre as duas variáveis e atribua o resultado em uma terceira variável
#--- Imprima o resultado juntamente com uma frase utilizando f-string
#--- Faça a leitura de dois números inteiros fora da função e atribua a duas variáveis
#--- Realize a chamada da função passando os dois valores lidos do console


from funcaoexe1 import multiplicacao

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

resultado = multiplicacao(n1, n2)

print(f'A multiplicação entre os números é: {resultado}')