#--- Exercício 4  - Funções - 1
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita em cima de uma variável que contenha um caracter pré-determinado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas função, para exibir o resultado no console

def variavel ():
    cabeçalho = '='
    print(cabeçalho*100)
    print('\n'*10)
    rodape = '='
    print(rodape*100)
variavel()