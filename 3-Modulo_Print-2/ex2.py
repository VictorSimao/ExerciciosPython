#--- Exercício 2  - Print -2
#--- Crie uma variável e atribua uma string com seu nome completo
#--- Crie uma variável e atribua um valor de ponto flutuante com sua altura
#--- Imprima as duas variáveis juntamente com uma frase utilizando f-string

nomeCompleto= input('Digite seu nome completo: ')
altura = float(input('Digite sua altura: '))
print(f'\nOlá {nomeCompleto},Seja bem vindo!,\nSua altura: {altura:.2f}')