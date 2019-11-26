#--- Exercício 3  - Funções - 1
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)
#--- Deve ser impresso apenas duas cadas após a vírgula

def calc_media (n1, n2, n3):
    media = (n1 + n2 + n3)/3
    return round (media,2)

num1 = float(input('Digite um numero:'))
num2 = float(input('Digite um numero:'))
num3 = float(input('Digite um numero:'))
print(f'Media de {num1}, {num2} e {num3} é igual a {calc_media(num1, num2, num3)}')