#--- Exercício 1 - Funções - 2
#--- Crie um função que receba duas variáveis
#--- Calcule a multiplicação entre as duas variáveis e atribua o resultado em uma terceira variável
#--- Imprima o resultado juntamente com uma frase utilizando f-string
#--- Faça a leitura de dois números inteiros fora da função e atribua a duas variáveis
#--- Realize a chamada da função passando os dois valores lidos do console

# --- DEFs ---
def multip(num1, num2):
    print(f'{num1} X {num2} = {num1 * num2}')
    return 0

print('='* 50)
n1 = int( input('Digite um numero: ') )
n2 = int( input('Digite outro numero: ') )

multip(n1, n2)
print('='*50)

