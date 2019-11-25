#--- Exercício 3  - Funções - 1
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)
#--- Deve ser impresso apenas duas cadas após a vírgula

def numeros ():
    n1=float(input('Digite o primeiro numero: '))
    n2=float(input('Digite o segundo numero: '))
    n3=float(input('Digite o terceiro numero: '))
    media=(n1+n2+n3)/3
    print(f'A media dos numeros {n1}, {n2} e {n3} sera {media:.3}')

numeros()