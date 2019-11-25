#--- Exercício 1  - Funções - 1
#--- Escreva uma função que imprima um cabeçalho
#--- O cabeçalho deve ser escrito usando a multiplicação de carácter
#--- O cabeçalho deev conter o nome de uma empresa, que será uma variável
#--- Realize a chamada da função na ultima linha do seu programa

caracter = input('Digite um caracter a ser multiplicado: ')
vezes = int(input('Digite a quantidade de vezes a ser multiplicado: '))

empresa = 'HBSIS'

def cabecalho(caracter, vezes):
    return caracter * vezes

cabecalho = cabecalho(caracter, vezes)
print(empresa,'\n', cabecalho)