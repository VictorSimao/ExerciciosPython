#--- Exercício 1  - Funções - 1
#--- Escreva uma função que imprima um cabeçalho
#--- O cabeçalho deve ser escrito usando a multiplicação de carácter
#--- O cabeçalho deev conter o nome de uma empresa, que será uma variável
#--- Realize a chamada da função na ultima linha do seu programa

empresa = input('Informe o nome da empresa')

def cabeçalho(empresa):
    
    print('='*50,'\n')
    print(empresa )
    print('\n')
    print('='*50)


cabeçalho(empresa)