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

def menu(opcao):
    if opcao == 0:
        return 'Usuário realizou o logoff'

    elif opcao == 1:
        return 'Cadastro de usuários'

    elif opcao == 2:
        return 'Lista de usuários cadastrados'

    else:
        return "Opcao invalida"


print(f'{"=" * 50}\n\n\t0 - Sair\n\t1 - Cadastrar\n\t2 - Listar\n\n{"=" * 50}')

opcao = int(input("Insira a opcao: "))

validacao = menu(opcao)

print(validacao)