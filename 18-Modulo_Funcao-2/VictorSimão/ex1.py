#--- Exercício 1 - Funções - 2
#--- Crie um função que receba duas variáveis
#--- Calcule a multiplicação entre as duas variáveis e atribua o resultado em uma terceira variável
#--- Imprima o resultado juntamente com uma frase utilizando f-string
#--- Faça a leitura de dois números inteiros fora da função e atribua a duas variáveis
#--- Realize a chamada da função passando os dois valores lidos do console

def multiplicacao(n1,n2):
    resultado = n1*n2
    print(f'Resultado {n1} * {n2} = {resultado}')

numero1 = int(input('Digite 1 numero: '))
numero2 = int(input('Digite 2 numero: '))

multiplicacao(numero1,numero2)