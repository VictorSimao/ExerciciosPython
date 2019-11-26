#--- Exercício 4  - Funções - 1
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita em cima de uma variável que contenha um caracter pré-determinado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas funções, para exibir o resultado no console

def header():
    empresa = 'HBSIS / Anheuser Busch InBev'
    char = '*'
    print(char*55, '\n')
    print(empresa)
    print('\n', char*55, '\n', sep='')

def footer():
    char = '*'
    print('\n', char*55, sep='')

header()
print('CONTEÚDO')
footer()