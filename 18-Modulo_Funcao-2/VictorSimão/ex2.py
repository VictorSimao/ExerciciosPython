#--- Exercício 2 - Funções - 2
#--- Crie uma função que calcule a potência de um número inteiro
#--- A função deve receber dois número inteiros
#--- O primeiro número deverá servir como base e o segundo como expoente
#--- Realize o calculo da potencia e atribua o resultado a uma variável
#--- Imprima o resultado da potência juntamente com uma frase utilizando a função format()
#--- Realize a leitura da base e da potência fora da função 
#--- A leitura deve ser feita através do terminal e atribuída à duas variáveis
#--- Realize a chamada da função passando a base e a potência

def exp(n1,n2):
    resultado=n1**n2
    print(f'Rsultado {n1} ** {n2} = {resultado}')

numero1 = int(input('Digite 1 numero: '))
numero2 = int(input('Digite 2 numero: '))

exp(numero1,numero2)