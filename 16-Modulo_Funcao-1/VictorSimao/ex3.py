#--- Exercício 3  - Funções - 1
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)
#--- Deve ser impresso apenas duas cadas após a vírgula

def media():
    n1= float(input('Digite 1 numero: '))
    n2= float(input('Digite 2 numero: '))
    n3= float(input('Digite 3 numero: '))
    media = (n1+n2+n3)/3
    print(f'Media entre os numeros: {media}')

media()