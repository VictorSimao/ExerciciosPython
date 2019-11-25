#--- Exercício 3  - Funções - 1
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)
#--- Deve ser impresso apenas duas cadas após a vírgula

n1=float(input('Digite o primeiro número: '))
n2=float(input('Digite o segundo número: '))
n3=float(input('Digite o terceiro número: '))
media=(n1+n2+n3)/3
print(f'A média das notas {n1:.2f}, {n2:.2f} e {n3:.2f} é {media:.2f}')