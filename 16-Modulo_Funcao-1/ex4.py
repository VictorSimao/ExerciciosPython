#--- Exercício 4  - Funções - 1
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita em cima de uma variável que contenha um caracter pré-determinado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas funções, para exibir o resultado no console

def header(empresa, char):
    empresa = empresa
    char = char
    print(char*55, '\n')
    print(empresa)
    print('\n', char*55, '\n', sep='')
    return ''

def footer(char):
    char = char
    print('\n', char*55, sep='')
    return ''

empresa = 'HBSIS / Anheuser Busch InBev'
char = '*'

header(empresa, char)
print('CONTEÚDO')
footer(char)