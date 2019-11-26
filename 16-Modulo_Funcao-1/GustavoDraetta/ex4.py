#--- Exercício 4  - Funções - 1
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita em cima de uma variável que contenha um caracter pré-determinado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas função, para exibir o resultado no console

# --- DEFs ---
def cabecalho(empresa_nome, caractere):
    qnt_caract = int( len(empresa_nome) ) # conta a quantidade de caracteres  (PEGUEI DOS MEUS OUTROS EXERCICIOS PRONTOS RSRS)
    print(f'{caractere}'*(qnt_caract+50)) # Multiplica o caractere desejado pela soma da quantidade de caracteres no nome do sistema com 50
    print(f' '*(24), f'{empresa_nome}')   # Mostra  nome do sistema 
    print(f'{caractere}'*(qnt_caract+50)) 
    return 0

def rodape(empresa_nome, caractere):
    qnt_caract = int( len(empresa_nome) ) # conta a quantidade de caracteres
    print(f'{caractere}'*(qnt_caract+50)) # Multiplica o caractere desejado pela soma da quantidade de caracteres no nome do sistema com 50
    print(f' '*(24), f'{empresa_nome}')   # Mostra  nome do sistema 
    print(f'{caractere}'*(qnt_caract+50)) 
    return 0

# --- MAIN ---
# Pede como será feito o cabeçalho
empresa_nomeC = input('Digite o conteudo do cabeçalho: ')      
caractereC = input('Digite o caractere a se formar o cabeçalho: ')

# Pede como será feito o rodapé
empresa_nomeR = input('Digite o conteudo do rodapé: ')
caractereR = input('Digite o caractere a se formar o rodapé: ')

cabecalho(empresa_nomeC, caractereC)
print('\n'*4, 'ONTEUDO CONTEUDO CONTEUDO CONTEUDO CONTEUDO ', '\n'*4)
rodape(empresa_nomeR, caractereR)
