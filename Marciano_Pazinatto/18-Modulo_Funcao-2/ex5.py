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

############################# area da função ##################################################################
def menu(a):
    if a==1:
       Cadastrodeusuario()        
    elif a==2:
        listarfuncionario()
    elif a==0:
        sairmenu()
    else:
        erromenu()
    return 

def Cadastrodeusuario():
    print('Cadastro de usuário')

def listarfuncionario():
    print('Lista de usuários cadastrados')    

def sairmenu():
    print('Usuário realizou o logoff')

def erromenu():
    print('OPção inválida')

########################################## codigo do programa ################################################
a=int(input('(1) CADASTRAR.\n(2) MOSTRAR CADASTROS\n(0) SAIR \n Digite uma opção: '))


menu(a)


