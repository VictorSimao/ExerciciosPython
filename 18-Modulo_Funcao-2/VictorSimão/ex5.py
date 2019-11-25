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

def menu():
    
    if x>=0 and x<=2:
        if x==0:
            sair()
        elif x==1:
            cadastrar()
        elif x==2:
            listar()
    else:
        print('Opção invalida')

def sair():
    print('Usuario realizou logoff')

def cadastrar():
    print('Cadastro de usuario')

def listar():
    print('Lista de usuários cadastrados')

print('='*10,'MENU','='*10)
print('Sair - 0')
print('Cadastrar - 1')
print('Listar - 2')
x=int(input('Digite a opção: '))
print('='*26)

menu()