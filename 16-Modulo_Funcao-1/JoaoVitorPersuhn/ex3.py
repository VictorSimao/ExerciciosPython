#--- Exercício 3  - Funções - 1
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)
#--- Deve ser impresso apenas duas cadas após a vírgula

def calculaMedia(n1 : float, n2 : float, n3 : float):
    return (n1 + n2 + n3) / 3

def leNumeros():
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    n3 = float(input('Digite o terceiro valor: '))
    resultado = calculaMedia(n1, n2, n3)
    print(f'A media entre os numeros {n1:.2f}, {n2:.2f}, {n3:.2f} é {resultado:.2f}')

leNumeros()