#--- Exercício 1 - Funções - 2
#--- Crie um função que receba duas variáveis
#--- Calcule a multiplicação entre as duas variáveis e atribua o resultado em uma terceira variável
#--- Imprima o resultado juntamente com uma frase utilizando f-string
#--- Faça a leitura de dois números inteiros fora da função e atribua a duas variáveis
#--- Realize a chamada da função passando os dois valores lidos do console

def multiplicar(num1 = 5, num2 = 5):
    return num1 * num2

mult = multiplicar()

print(f'5 X 5 = {mult}')

num3 = int(input("Insira um inteiro: "))
num4 = int(input("Insira um inteiro: "))

mult = multiplicar(num3, num4)

print(f'{num3} X {num4} = {mult}')
