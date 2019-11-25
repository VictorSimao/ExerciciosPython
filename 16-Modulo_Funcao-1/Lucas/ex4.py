#--- Exercício 4  - Funções - 1
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita em cima de uma variável que contenha um caracter pré-determinado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas função, para exibir o resultado no console

cabeca = input('Qual o caracter do cabeçalho?')
pe = input('Qual o caracter do rodapé?')

def cabecalho(cabeca):
    return print(f'{cabeca}'*50)
def rodape(pe):
    return print(f'{pe}'*50)
cabecalho(cabeca)
rodape(pe)