#--- Exercício 1 - Funções - 2
#--- Crie um função que receba duas variáveis
#--- Calcule a multiplicação entre as duas variáveis e atribua o resultado em uma terceira variável
#--- Imprima o resultado juntamente com uma frase utilizando f-string
#--- Faça a leitura de dois números inteiros fora da função e atribua a duas variáveis
#--- Realize a chamada da função passando os dois valores lidos do console

def calcula_multiplicacao(x , y):
    multiplicacao = x * y
    return(f'{x} x {y} = {multiplicacao}')

x = int(input('Informe o primeiro número\n'))
y = int(input('Informe o segundo número\n'))

print(calcula_multiplicacao(x , y))