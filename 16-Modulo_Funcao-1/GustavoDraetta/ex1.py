#--- Exercício 1  - Funções - 1
#--- Escreva uma função que imprima um cabeçalho
#--- O cabeçalho deve ser escrito usando a multiplicação de carácter
#--- O cabeçalho deev conter o nome de uma empresa, que será uma variável
#--- Realize a chamada da função na ultima linha do seu programa

def cabecalho(empresa_nome, caractere):
    qnt_caract = int( len(empresa_nome) ) # conta a quantidade de caracteres
    print(f'{caractere}'*(qnt_caract+50)) # Multiplica o caractere desejado pela soma da quantidade de caracteres no nome do sistema com 50
    print(f' '*(24), f'{empresa_nome}')   # Mostra  nome do sistema 
    print(f'{caractere}'*(qnt_caract+50)) 
    return 0


empresa_nome = input('Digite o nome da empresa: ')
caractere = input('Digite o caractere desejado: ')

cabecalho(empresa_nome, caractere)