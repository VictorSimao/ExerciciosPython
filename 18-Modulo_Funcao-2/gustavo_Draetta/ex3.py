#--- Exercício 3 - Funções - 2
#--- Crie uma função para a impressão de um cabeçalho
#--- A função deve receber dois dados
#--- Um dado deve ser o nome do sistema
#--- O segundo dado deve ser o caracter que será multiplicado para fazer a linha de cabeçalho
#--- A impressão deve ser realizada utilizando f-string
#--- A função deve ser chamada informando os dois dados

# --- DEFs ---
# Funcao que recebe o nome da empresa e o caractere para 
def cabeçalho(empresa_sist, caractere):
    qnt_caract = int( len(empresa_sist) ) # conta a quantidade de caracteres
    print(f'{caractere}'*(qnt_caract+50)) # Multiplica o caractere desejado pela soma da quantidade de caracteres no nome do sistema com 50
    print(f' '*(24), f'{empresa_sist}')   # Mostra  nome do sistema 
    print(f'{caractere}'*(qnt_caract+50)) 
    return 0

# --- ENTRADA ---
empresa_sist = input('Digite o nome da empresa: ')
caractere = input('digite o caractere desejado')

# Funcao que recebe o nome do sistema e o caractere desejado pra fazer um cabeçalho
# O nome da empresa sempre vai ficar no meio
cabeçalho(empresa_sist, caractere)