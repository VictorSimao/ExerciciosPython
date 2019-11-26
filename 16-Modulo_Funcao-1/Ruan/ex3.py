#--- Exercício 3  - Funções - 1
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)
#--- Deve ser impresso apenas duas cadas após a vírgula


def calcular():
    n1 = float(input('digite um número: '))
    n2 = float(input('digite outro número: '))
    n3 = float(input('digite novamente outro número: '))
    n4 = n1 + n2 + n3
    média = n4 / 3
    print(f'A média entre primeiro número {n1},segundo número {n2}, terceiro número {n3} resulta em = {média}')

calcular()