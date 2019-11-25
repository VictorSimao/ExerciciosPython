#--- Exercício 4  - Funções - 1
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita em cima de uma variável que contenha um caracter pré-determinado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas função, para exibir o resultado no console

def cabeçalho():
    perg = input('Digite com qual caractere deseja criar seu cabeçalho: [#/$/=]: ')
    if perg == '#':
        print('\n','#'*20,'Isso é um cabeçalho','#'*20)
    elif perg == '$':
        print('\n','$'*20,'Isso é um cabeçalho','$'*20)
    if perg == '=':
        print('\n','='*20,'Isso é um cabeçalho','='*20)
    return (perg)
def rodape():
    perg2 = input('Digite com qual caractere deseja criar seu rodape: [#/$/=]: ')
    if perg2 == '#':
        print('\n'*4,'#'*20,'Isso é um rodape','#'*20)
    elif perg2 == '$':
        print('\n'*4,'$'*20,'Isso é um rodape','$'*20)
    if perg2 == '=':
        print('\n'*4,'='*20,'Isso é um rodape','='*20)
    return (perg2)

cabeçalho()
rodape()
