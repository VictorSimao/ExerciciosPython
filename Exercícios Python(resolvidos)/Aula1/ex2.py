#--- Exercicio 2  - Impressão de dados com a função Print
#--- Imprima o menu de uma aplicação de cadastro de pessoas
#--- O menu deve conter as opções de Cadastrar, Alterar, listar pessoas, alem da opção sair

print('\nMENU DE CADASTRAMENTO')
print('='*20)
print('1 - Cadastrar\n2 - Alterar\n3 - Listar Pessoas\n4 - Sair')
print('='*20)
numero = int(input('Digite o número da opção desejada: '))
print('='*20)

if numero == 1:
    nome = input('Digite o seu nome: ')
    sobrenome = input('Digite seu sobrenome: ')
    idade = input('Digite sua idade (somente números): ')
    print(f'Seu nome completo é {nome} {sobrenome} e você tem {idade} anos.')

if numero == 2:
    alterar = input('Para alterar o nome digite 1: \nPara alterar o sobrenome digite 2: \nPara alterar a idade digite 3: ')
    if alterar == 1:
        nome = ('Digite seu nome: ')
        print(f'Seu nome foi alterado para {nome}')
    elif alterar == 2:
        sobrenome = ('Digite seu sobrenome: ')
        print(f'Seu sobrenome foi alterado para {sobrenome}')
    elif alterar == '3':
        idade = input('Digite sua idade: ')
        print(f'Sua idade foi alterada para {idade} anos.')
    else:
        print('ERROR 404')

elif numero == 3:
    print('Lista de pessoas cadastradas: ')

elif numero == 4:
    print('PROGRAMA ENCERRADO')