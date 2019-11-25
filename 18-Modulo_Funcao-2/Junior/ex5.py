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


def função(a):
    if a >2:
        print('Opção invalida')
        while a >2:
            a = int(input('Bem Vindo ao menu dos funcionarios\nDigite o numero de acordo com a opçao desejada: \n[0] Realizar Logoff.\n[1]Cadastro de Funcionarios.\n[2]Lista de Usuarios Cadastrados.\nDigite aqui: '))
            if a == 0:
                print('Usuário realizou o logoff')
            elif a == 1:
                print('Cadastro de usuários')
            elif a == 2:
                print('Lista de usuários cadastrados')
    elif a == 0:
        print('Usuário realizou o logoff')
    elif a == 1:
        print('Cadastro de usuários')
    elif a == 2:
        print('Lista de usuários cadastrados')
    return a

print('\n','='*20,'Cadastramento de Funcionarios HBSIS','='*20,'\n'*2)

n1 = int(input('Bem Vindo ao menu dos funcionarios\nDigite o numero de acordo com a opçao desejada: \n[0] Realizar Logoff.\n[1]Cadastro de Funcionarios.\n[2]Lista de Usuarios Cadastrados.\n\nDigite aqui: '))
print(f'{função(n1)}')

print('\n','='*20,'Cadastramento de Funcionarios HBSIS','='*20)