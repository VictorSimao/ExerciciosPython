#--- Exercício 3  - Funções - 1
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)
#--- Deve ser impresso apenas duas cadas após a vírgula

n1 = float(input('Informe o Primeiro Numero'))
n2 = float(input('Infore o Segundo Numero'))
n3 = float(input('informe o terceiro Numero'))

def media(n1,n2,n3):
    media = (n2+n2+n3)/3
    return media

print(f'A media do Aluno foi de {round(media(n1,n2,n3),2)} ')