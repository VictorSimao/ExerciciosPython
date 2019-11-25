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

# --- IMPORTS ---
import os 

# --- DEFs ---
def cabeçalho(empresa_sist, caractere):
    qnt_caract = int( len(empresa_sist) ) # conta a quantidade de caracteres
    print(f'{caractere}'*(qnt_caract+50)) # Multiplica o caractere desejado pela soma da quantidade de caracteres no nome do sistema com 50
    print(f' '*(24), f'{empresa_sist}')   # Mostra  nome do sistema 
    print(f'{caractere}'*(qnt_caract+50)) 
    return (qnt_caract+50)

def verifica(n1): # função que verifica se o numero está entre 0 e 2
    if n1 < 0 or n1 > 2:
        print('opção inválida')
        return False

    else: 
        return True

def Sair():
    print('Usuário realizou logoff.')
    return False

def Cadastrar():
    print('Cadastro de Usuários: ')
    return 0

def Listar():
    print('Lista de usuários cadastrados: ')
    return 0

# --- MAIN ---
i = True
while(i):
    os.system('cls' if os.name == 'nt' else 'clear')
    qnt_caract = cabeçalho('MENU CADASTRO', '=')
    print('0 - [ SAIR ]')
    print('1 - [ CADASTRAR ]')
    print('2 - [ LISTAR ]')
    print('='*qnt_caract)
    choice = int( input('Digite o numero da opção desejada: ') )
    # Verifica se o numero está entre 0 e 2
    verifica(choice)
    print('='*qnt_caract)

    if choice == 0:
        i = Sair()

    elif choice == 1:
        Cadastrar()

    elif choice == 2:
        Listar()
        
    print('='*qnt_caract)

    enter = input('Pressione Enter para continuar.')
    os.system('cls' if os.name == 'nt' else 'clear')

    cabeçalho('MENU CADASTRO', '=')

