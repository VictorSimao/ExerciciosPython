#--- Exercício 1  - Funções - 1
#--- Escreva uma função que imprima um cabeçalho
#--- O cabeçalho deve ser escrito usando a multiplicação de carácter
#--- O cabeçalho deev conter o nome de uma empresa, que será uma variável
#--- Realize a chamada da função na ultima linha do seu programa

def cabecalho(empresa_funcao):
    output_funcao=(f'{"="*15} {empresa_funcao} {"="*15}')
    return output_funcao

#############################################################################
hbsis = "HBSIS Soluções"

print(cabecalho(hbsis))
