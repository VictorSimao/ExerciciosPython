#--- Exercício 4  - Funções - 1
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita em cima de uma variável que contenha um caracter pré-determinado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas função, para exibir o resultado no console


def cabecalhoRodape():
    empresa = 'HBSIS'
    caracter_superior = input('Digite algo para o cabeçalho: ')
    caracter_inferior = input('Digite algo para o rodapé: ')
    vezes = int(input('Digite a quantidade de vezes a ser multiplicado: '))
    print(caracter_superior * vezes,'\n'*3, empresa,'\n'*3, caracter_inferior * vezes)
    return

cabecalhoRodape()
