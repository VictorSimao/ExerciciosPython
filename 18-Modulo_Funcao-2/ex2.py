#--- Exercício 2 - Funções - 2
#--- Crie uma função que calcule a potência de um número inteiro
#--- A função deve receber dois número inteiros
#--- O primeiro número deverá servir como base e o segundo como expoente
#--- Realize o calculo da potencia e atribua o resultado a uma variável
#--- Imprima o resultado da potência juntamente com uma frase utilizando a função format()
#--- Realize a leitura da base e da potência fora da função 
#--- A leitura deve ser feita através do terminal e atribuída à duas variáveis
#--- Realize a chamada da função passando a base e a potência

def pot(base, expo):
    result_pot = base**expo
    return print('\nO resultado da potência com base {} e expoente {} é: {}'.format(base, expo, result_pot))

base = int(input('\nDigite a base da potência: '))
expo = int(input('Digite o expoente: '))

pot(base, expo)