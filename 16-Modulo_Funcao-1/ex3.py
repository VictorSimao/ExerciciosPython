#--- Exercício 3  - Funções - 1
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)
#--- Deve ser impresso apenas duas cadas após a vírgula

def calcula_media(x , y , z):
    media = (x + y + z) / 3
    return(media)

x = float(input('Informe o primeiro número\n'))
y = float(input('Informe o segundo número\n'))
z = float(input('Informe o terceiro número\n'))

print(calcula_media(x , y , z))