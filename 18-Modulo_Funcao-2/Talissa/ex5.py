def sair():
    return 'Usuário realizou o logoff'

def cadastrar():
    return 'Cadastro de usuários'

def listar():
    return 'Lista de usuários cadastrados'

opcao0 = sair()
opcao1 = cadastrar()
opcao2 = listar()

opcao = int(input('Digite 0 para sair, 1 para cadastrar usuários ou 2 para listar os usuários existentes: '))

if opcao == 0:
    print(opcao0)

elif opcao == 1:
    print(opcao1)

elif opcao == 2:
    print(opcao2)

else:
    print('Opção inválida')
