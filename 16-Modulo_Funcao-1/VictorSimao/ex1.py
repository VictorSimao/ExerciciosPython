#--- Exercício 1  - Funções - 1
#--- Escreva uma função que imprima um cabeçalho
#--- O cabeçalho deve ser escrito usando a multiplicação de carácter
#--- O cabeçalho deve conter o nome de uma empresa, que será uma variável
#--- Realize a chamada da função na ultima linha do seu programa

def cabecalho():
    print('='*46,)
    print(f'{empresa} - Blumenau - 17/11/19')
    print('='*46)

empresa='Cervejaria AMBEV / HBSIS'

cabecalho()