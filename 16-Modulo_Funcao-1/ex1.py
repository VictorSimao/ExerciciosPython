#--- Exercício 1  - Funções - 1
#--- Escreva uma função que imprima um cabeçalho
#--- O cabeçalho deve ser escrito usando a multiplicação de carácter
#--- O cabeçalho deev conter o nome de uma empresa, que será uma variável
#--- Realize a chamada da função na ultima linha do seu programa

def imprimirCabecalho(nome_empresa, tam_string):
    print('=' * tam_string)

    print(nome_empresa)

if __name__ == "__main__":

    tam_string = 50
    nome = input("Nome da empresa: ")
    imprimirCabecalho(nome, tam_string)