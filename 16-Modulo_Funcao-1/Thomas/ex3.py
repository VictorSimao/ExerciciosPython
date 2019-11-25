#--- Exercício 3  - Funções - 1
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)
#--- Deve ser impresso apenas duas cadas após a vírgula

import ex2

def calcularMedia(num1, num2, num3):
    media = (num1 + num2 + num3) / 3
    return media


if __name__ == "__main__":
    num1 = ex2.lerNumero()
    num2 = ex2.lerNumero()
    num3 = ex2.lerNumero()

    media = round(calcularMedia(num1, num2, num3), 2)

    print(f'A media é {media}')