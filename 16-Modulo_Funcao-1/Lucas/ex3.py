#--- Exercício 3  - Funções - 1
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)
#--- Deve ser impresso apenas duas cadas após a vírgula

def media():
    n1= int(input('Digite um numero'))
    n2= int(input('Digite um numero'))
    n3= int(input('Digite um numero'))
    n4=(n1+n2+n3)/3
    return print(f'A média é {n4:.2f}')
media()