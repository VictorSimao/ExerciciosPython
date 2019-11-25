#--- Exercício 5 - Funções - 1
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console e armazene em uma variável
#--- Realize o calculo da raiz e armazene em uma segunda variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)

def calcularRaiz(radicando, indice):
    return (radicando ** (1/indice))

if __name__ == "__main__":
    radicando = float(input("Insira o radicando: "))
    indice = float(input("Insira o indice: "))

    raiz = calcularRaiz(radicando, indice)

    print(f'A raiz {indice}º de {radicando} é {raiz}')