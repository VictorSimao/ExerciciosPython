#--- Exercício 1  - Funções - 1
#--- Escreva uma função que imprima um cabeçalho
#--- O cabeçalho deve ser escrito usando a multiplicação de carácter
#--- O cabeçalho deev conter o nome de uma empresa, que será uma variável
#--- Realize a chamada da função na ultima linha do seu programa

def header():
    empresa = 'HBSIS / Anheuser Busch InBev'
    print('#'*55, '\n')
    print(empresa)
    print('\n', '#'*55, '\n', sep='')


header()