#--- Exercício 4  - Funções - 1
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita em cima de uma variável que contenha um caracter pré-determinado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas função, para exibir o resultado no console

def cbc ():
    carac = input('Digite o caracter:') 
    print (f'{carac}'*50+ '\n\n' + f"{carac}" * 50)

def cbc2 ():
    carac2 = input('Digite o caracter:')
    print (f'{carac2}'*50 + '\n\n' + f'{carac2}'*50)

cbc()
cbc2()

