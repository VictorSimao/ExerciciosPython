#--- Exercício 4  - Funções - 1
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita em cima de uma variável que contenha um caracter pré-determinado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas função, para exibir o resultado no consolecab = ('-') * 50

cab = ('-') *20
rod =('*') *20
empresa = 'H B S I S'

def c(cab):
    resultadoc: cab * 20
    return resultadoc
def r(rod):
    resultador: rod * 20 
    return resultador

resultadoc = (cab)
resultador = (rod)

print(f'{resultadoc}\n{resultadoc}\n{resultador}\n{empresa}\n{resultador}\n{resultadoc}\n{resultadoc}\n')