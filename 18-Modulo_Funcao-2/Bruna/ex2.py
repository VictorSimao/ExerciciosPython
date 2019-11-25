#--- Exercício 2 - Funções - 2
#--- Crie uma função que calcule a potência de um número inteiro
#--- A função deve receber dois número inteiros
#--- O primeiro número deverá servir como base e o segundo como expoente
#--- Realize o calculo da potencia e atribua o resultado a uma variável
#--- Imprima o resultado da potência juntamente com uma frase utilizando a função format()
#--- Realize a leitura da base e da potência fora da função 
#--- A leitura deve ser feita através do terminal e atribuída à duas variáveis
#--- Realize a chamada da função passando a base e a potência

def potencia(n1_pot,n2_pot):
    res_pot = n1_pot**(1/n2_pot)
    return res_pot

n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))


print('O resultado da potencia entre os número {} e {} é {}'.format(n1,n2,potencia(n1,n2)))