#--- Exercício 4  - Funções - 1
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita em cima de uma variável que contenha um caracter pré-determinado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas função, para exibir o resultado no console


caracter_superior = input('Digite algo para o cabeçalho: ')
caracter_inferior = input('Digite algo para o rodapé: ')
vezes = int(input('Digite a quantidade de vezes a ser multiplicado: '))

empresa = 'HBSIS'

def cabecalho(caracter_superior, vezes):
    return caracter_superior * vezes

def rodape(caracter_inferior, vezes):
    return caracter_inferior * vezes

cabecalho = cabecalho(caracter_superior, vezes)
rodape = rodape(caracter_inferior, vezes)

print(cabecalho,'\n', empresa,'\n'*3, empresa,'\n', rodape)
