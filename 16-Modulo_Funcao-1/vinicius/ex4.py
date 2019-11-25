#--- Exercício 4  - Funções - 1
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita em cima de uma variável que contenha um caracter pré-determinado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas função, para exibir o resultado no console
def raiz():
    raiz = int(input('Escolha \n1- Raiz quadrada \n2- Raiz cubica \nOpção: '))
    num = float(input('Digite um numero para ser calculado: '))
    calc = 0
    if raiz == 1:
        calc = (num ** 0.5)
        print(f'A raiz quadrada de {num} = {calc}')
    elif raiz == 2:
        calc = (num ** 1/3)
        print(f'A raiz cubica de {num} = {calc}')
    else: 
        print('Opção incorreta!')
    return calc

mengao = raiz()