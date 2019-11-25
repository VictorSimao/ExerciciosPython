#--- Exercício 4  - Funções - 1
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita em cima de uma variável que contenha um caracter pré-determinado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas função, para exibir o resultado no console

v_cabecalho = '='
v_rodape = '='

def cabecalho(v_cabecalho):
    return print(f'{v_cabecalho}'*55,'\n'*3)

def rodape(v_rodape):
    return print('\n'*3,f'{v_rodape}'*55)

get_cabecalho = cabecalho(v_cabecalho)
get_rodape = rodape(v_rodape)



