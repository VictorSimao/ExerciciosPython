#--- Exercício 3  - Funções - 1
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)
#--- Deve ser impresso apenas duas cadas após a vírgula

def numeros(num1,num2,num3):
    media = (num1 + num2 + num3) / 3
    return print (f'\nNumero 1 = {num1}\nNumero 2 = {num2}\nNumero 3 = {num3}\nMedia = {media}')

num1 = float(input('Numero 1:'))
num2 = float(input('Numero 2:'))
num3 = float(input('Numero 3:'))

numeros(num1,num2,num3)
