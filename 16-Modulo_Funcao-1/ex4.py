#--- Exercício 4  - Funções - 1
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita em cima de uma variável que contenha um caracter pré-determinado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas função, para exibir o resultado no console

import ex1

def imprimirRodape(tam_string):
    print('=' * tam_string)

if __name__ == "__main__":
    texto = input("Insira algo: ")
    tam_string = int(input("Insira o tamanho do cabeçalho e rodape: "))
    ex1.imprimirCabecalho(texto, tam_string)
    imprimirRodape(tam_string)