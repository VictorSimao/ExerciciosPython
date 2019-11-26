#--- Exercício 4  - Funções - 1
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita em cima de uma variável que contenha um caracter pré-determinado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas função, para exibir o resultado no console

n1 =0

def printo(n1):
    n1 = input('Digite o nome para o cabeçalho: ')
    print(' ','='*80,'\n'*2)
    print(' ',(n1+' ')*20)
    return 

def rodape():
    print('\n'*2,'='*80)
    return 

printo(n1),rodape()
    

    
