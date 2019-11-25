#--- Exercício 2 - Funções - 2
#--- Crie uma função que calcule a potência de um número inteiro
#--- A função deve receber dois número inteiros
#--- O primeiro número deverá servir como base e o segundo como expoente
#--- Realize o calculo da potencia e atribua o resultado a uma variável
#--- Imprima o resultado da potência juntamente com uma frase utilizando a função format()
#--- Realize a leitura da base e da potência fora da função 
#--- A leitura deve ser feita através do terminal e atribuída à duas variáveis
#--- Realize a chamada da função passando a base e a potência

# --- DEFs ---
def pott(num1, num2):
    res = num1**num2
    print('{} elevado  a {} é {}.'.format(res, num1, num2))
    return 0
# --- ENTRADA ---
num1 = int( input('Digite um numero: ') )
num2 = int( input('Digite outro numero: ') )

# Função que pede 2 numeros e imprime o primeiro elevado ao segundo.
pott(num1, num2)
