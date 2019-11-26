#--- Exercício 3  - Funções - 1
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)
#--- Deve ser impresso apenas duas cadas após a vírgula

n1 = float(input('Digite o numero 1:'))
n2 = float(input('Digite o numero 2:'))
n3 = float(input('Digite o numero 3:'))

n4 = ((n1 + n2 + n3)/3)


print(round(n4,2))