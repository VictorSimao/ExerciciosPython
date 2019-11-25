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

def menu(numero1):
    if numero1 == 0:
        print('='*50,'Usuário realizou o logoff','='*50)
    elif numero1 == 1:
        print('='*50,'Cadastro de usuários','='*50)
    elif numero1 == 2:
        print('='*50,'Lista de usuários cadastrados','='*50)
    else:
        print('='*50,'Opção inválida','='*50)

n1=int(input('''Digite
0- Para a funcao sair
1- Para a funcao cadastrar
2- Para a funcao listar
'''))

menu(n1)