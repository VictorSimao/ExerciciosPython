#--- Exercício 2 - Funções - 2
#--- Crie uma função que calcule a potência de um número inteiro
#--- A função deve receber dois número inteiros
#--- O primeiro número deverá servir como base e o segundo como expoente
#--- Realize o calculo da potencia e atribua o resultado a uma variável
#--- Imprima o resultado da potência juntamente com uma frase utilizando a função format()
#--- Realize a leitura da base e da potência fora da função 
#--- A leitura deve ser feita através do terminal e atribuída à duas variáveis
#--- Realize a chamada da função passando a base e a potência
def pot (a,b):
    rs = a**b
    print('O resultado da equação é de: {}'.format(rs))

n1 = int(input('Digite a base, da potencia que deseja obter: '))
n2 = int(input('Digite o expoente para sua base ,que foi digitada na linha a cima'))
pot(n1, n2)