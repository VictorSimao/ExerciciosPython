#--- Exercício 3 - Funções - 2
#--- Crie uma função para a impressão de um cabeçalho
#--- A função deve receber dois dados
#--- Um dado deve ser o nome do sistema
#--- O segundo dado deve ser o caracter que será multiplicado para fazer a linha de cabeçalho
#--- A impressão deve ser realizada utilizando f-string
#--- A função deve ser chamada informando os dois dados

def cabecalho():
    nomeSistema = input('Digite o nome do sistema: ')
    caracter = input('Digite um caracter a ser multiplicado: ')
    print('\n'*2, nomeSistema, '\n', caracter * 100, '\n'*2)

cabecalho()


# def cabecalho(caracter):
#     return caracter * 100

# nomeSistema = input('Digite o nome do sistema: ')
# caracter = input('Digite um caracter a ser multiplicado: ')

# cabecalho = cabecalho(caracter)

# print('\n'*2, nomeSistema, '\n', cabecalho, '\n')