#--- Exercício 1  - Funções - 1
#--- Escreva uma função que imprima um cabeçalho
#--- O cabeçalho deve ser escrito usando a multiplicação de carácter
#--- O cabeçalho deev conter o nome de uma empresa, que será uma variável
#--- Realize a chamada da função na ultima linha do seu programa

def cabecalho(nome_emp):
    return print('_'*50 + f'\nNome da empresa: {nome_emp}\n' + '#'*50)

nome_empresa = input('Digite o nome da empresa: ')
cabecalho(nome_empresa)