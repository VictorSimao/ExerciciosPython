#--- Exercício 4  - Funções - 1
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita em cima de uma variável que contenha um caracter pré-determinado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas função, para exibir o resultado no console

caracter = input('Digite um caracter: ')

def cabecalho(caracter):
    print(caracter*46,)
    print('Cervejaria AMBEV / HBSIS - Blumenau - 17/11/19')
    print(caracter*46)

def rodape(caracter):
    print(caracter*46,)
    print('         que a força esteja com voce')
    print(caracter*46)

cabecalho(caracter)
rodape(caracter)