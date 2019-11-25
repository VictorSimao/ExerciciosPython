#--- Exercício 5 - Funções - 2
#--- Crie uma função que valida um menu
#--- A função deve receber um número inteiro
#--- A função deve checar se o número está entre 0 e 2
#--- Caso o número esteja fora deste range deve ser informado 'Opção inválida'
#--- Caso o número informado esteja dentro do range deve seguir as seguintes regras:
#---    0-Chamar uma função Sair(), esta função deve imprimir 'Usuário realizou o logoff'
#---    1-Chamar uma função Cadastrar(), esta função deve imprimir 'Cadastro de usuários'
#---    2-Chamar uma função Listar(), esta função deve imprimir 'Lista de usuários cadastrados'
#--- Crie um menu com cabeçalho e rodapé com as opções listadas acima
#--- Realize a leitura da opção digitada pelo usuário no terminal
#--- Realize a chamada da função que valida o menu e passe o variável criada durante a leitura do terminal

def valida(opcao : int):
    if opcao < 0 or opcao > 2:
        return False
    return True

def Sair():
    print('Usuario fazendo logoff')

def Cadastrar():
    print('Cadastro de usuario')

def Listar():
    print('Lista de usuarios cadastrados')

def cabecalho():
    print('*' * 50, '\n')
    print('0 - Sair\n1 - Cadastrar\n2 - Listar\n')
    print('*' * 50, '\n')

cabecalho()
op = int(input('Digite a opção desejada: \n'))

if valida(op):
    if op == 0:
        Sair()
    elif op == 1:
        Cadastrar()
    else:
        Listar()
else:
    print('Opção invalida')