#--- Exercício 1  - Funções - 1
#--- Escreva uma função que imprima um cabeçalho
#--- O cabeçalho deve ser escrito usando a multiplicação de carácter
#--- O cabeçalho deev conter o nome de uma empresa, que será uma variável
#--- Realize a chamada da função na ultima linha do seu programa

nome_empresa = input('Nome da empresa:')

def cabecalho (nome_empresa):
    print ('='*70)
    print (" "*30, nome_empresa)
    print ('='*70)

cabecalho(nome_empresa)