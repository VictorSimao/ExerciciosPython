#--- Exercício 2  - Funções - 1
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a soma entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

def lerNumero():
    numero = float(input("Insira um numero: "))
    return numero

def somar(num1, num2):
    soma = num1 + num2
    return soma


if __name__ == "__main__":
    num1 = lerNumero()
    num2 = lerNumero()

    soma = somar(num1, num2)

    print(f'O numero 1 inserido é {num1}, o segundo numero é {num2}. A soma é {soma}')