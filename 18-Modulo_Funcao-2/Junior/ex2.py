#--- Exercício 2 - Funções - 2
#--- Crie uma função que calcule a potência de um número inteiro
#--- A função deve receber dois número inteiros
#--- O primeiro número deverá servir como base e o segundo como expoente
#--- Realize o calculo da potencia e atribua o resultado a uma variável
#--- Imprima o resultado da potência juntamente com uma frase utilizando a função format()
#--- Realize a leitura da base e da potência fora da função 
#--- A leitura deve ser feita através do terminal e atribuída à duas variáveis
#--- Realize a chamada da função passando a base e a potência

def fun(n1,n2):
    cal = n1**n2
    return cal

a = int(input('Digite um numero que sirva como base para calcularmos sua potencia: '))
b = int(input('Digite outro numero que sirva como expoente: '))

print(f'A calcula da potencia de {b} sobre {a} é igual a: {fun(a,b)}')