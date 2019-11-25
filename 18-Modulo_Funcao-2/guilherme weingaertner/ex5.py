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

from metodo_1 import sair,cadastrar,listar
print('#'*80)
print('0-Chamar uma função Sair')
print('1-Chamar uma função Cadastrar')
print('2-Chamar uma função Listar')
print('#'*80)

n1 = int(input('Digite o numero(0,1,2)'))
print('#'*80)

if n1 > 2 or n1 < 0:
        print('ERRO,DIGITE UM NUMERO INTEIRO ENTRE 0-2')
else:
    if n1 == 0:
        print(f'{sair()}')
    elif n1 == 1:
        print(f'{cadastrar()}')
    else:
        print(f'{listar()}')
