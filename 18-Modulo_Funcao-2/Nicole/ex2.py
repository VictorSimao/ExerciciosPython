#--- Exercício 2 - Funções - 2
#--- Crie uma função que calcule a potência de um número inteiro
#--- A função deve receber dois número inteiros
#--- O primeiro número deverá servir como base e o segundo como expoente
#--- Realize o calculo da potencia e atribua o resultado a uma variável
#--- Imprima o resultado da potência juntamente com uma frase utilizando a função format()
#--- Realize a leitura da base e da potência fora da função 
#--- A leitura deve ser feita através do terminal e atribuída à duas variáveis
#--- Realize a chamada da função passando a base e a potência

def numeros (numero1,numero2):
    potencia=numero1**numero2
    print('A potencia dos numeros {} como base, e {} como expoente, tera resultado {}'.format(numero1,numero2,potencia))

n1=int(input('Digite o primeiro numero: '))
n2=int(input('Digite o segundo numero: '))
numeros(n1,n2)