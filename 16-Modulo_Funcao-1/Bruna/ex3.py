#--- Exercício 3  - Funções - 1
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)
#--- Deve ser impresso apenas duas cadas após a vírgula

v1 = ''
v2 = ''
v3 = ''

def media (v1,v2,v3):
    v1 = float(input('Digite numero 1: '))
    v2 = float(input('Digite numero 2: '))
    v3 = float(input('Digite numero 3: '))
    media = (v1 + v2 + v3) / 3
    return media

media = media(v1,v2,v3)

print(f'A média de v1 + v2 + v2 é {media :.2f}')