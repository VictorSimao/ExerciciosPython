#--- Exercício 3  - Funções - 1
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)
#--- Deve ser impresso apenas duas cadas após a vírgula

def cal():
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite outro numero: '))
    n3 = float(input('Digite mais um numero: '))
    media = (n1 + n2 + n3) / 3
    return (media)
print(f'A media entre os numeros é : {cal():.2f}')