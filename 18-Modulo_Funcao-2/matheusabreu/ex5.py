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

def validar(op):
    if op < 0 or op >2:
        return print('\nOpção inválida')
    elif op == 0:
        return sair()
    elif op == 1:
        return cadastrar()
    elif op == 2:
        return listar()
def sair():
    return print('\nUsuário realizou o logoff.')

def cadastrar():
    return print('\nCadastro de usuários')

def listar():
    return print('\nLista de usuários cadastrados')

print('#'*55, '\n', sep='')
print(f'MENU \n1 -> Cadastrar \n2 -> Listar \n0 -> Sair')
print('\n', '#'*55, sep='')
op = int(input('\nSelecione uma opção: '))
validar(op)