#--- Exercício 2 - Funções - 2
#--- Crie uma função que calcule a potência de um número inteiro
#--- A função deve receber dois número inteiros
#--- O primeiro número deverá servir como base e o segundo como expoente
#--- Realize o calculo da potencia e atribua o resultado a uma variável
#--- Imprima o resultado da potência juntamente com uma frase utilizando a função format()
#--- Realize a leitura da base e da potência fora da função 
#--- A leitura deve ser feita através do terminal e atribuída à duas variáveis
#--- Realize a chamada da função passando a base e a potência

def calcula_potencia(x , y):
    potencia = x ** y
    return('{} elevado à {}ª potência é igual a {}'.format(x , y , potencia))

base = int(input('Informe o número da base\n'))
potencia = int(input('Informe o número da potência\n'))

print(calcula_potencia(base , potencia))