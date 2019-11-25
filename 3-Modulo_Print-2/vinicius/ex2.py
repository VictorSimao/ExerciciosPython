#--- Exercício 2  - Print -2
#--- Crie uma variável e atribua uma string com seu nome completo
#--- Crie uma variável e atribua um valor de ponto flutuante com sua altura
#--- Imprima as duas variáveis juntamente com uma frase utilizando f-string

nome = input("\nDigite seu nome completo: ")
alt = float(input("Digite sua altura: "))

print(f'\nNome completo: {nome} \nAltura: {alt:0.2f}\n')