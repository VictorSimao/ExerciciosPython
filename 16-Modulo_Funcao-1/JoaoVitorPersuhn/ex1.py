#--- Exercício 1  - Funções - 1
#--- Escreva uma função que imprima um cabeçalho
#--- O cabeçalho deve ser escrito usando a multiplicação de carácter
#--- O cabeçalho deev conter o nome de uma empresa, que será uma variável
#--- Realize a chamada da função na ultima linha do seu programa

def escreveCabecalho(empresa : str):
    print('=' * 50, '\n')
    print('\t' * 2,f'{empresa} \n')
    print('=' * 50)

nomeEmpresa = input('Digite o nome da empresa: ')
escreveCabecalho(nomeEmpresa)