#--- Exercício 4 - Funções - 2
#--- Crie uma função que realize o cálculo de contribuição do funcionário para a previdência da empresa
#--- O cálculo deve ser feito de acordo com a faixa salarial:
#---    
#---    De R$ 1000.01 Até R$ 3000.00 -> 1.5%
#---    De R$ 3000.01 Até R$ 6000.00 -> 2.0%
#---    Acima de R$ 6000.01 -> 2.5%
#--- A função deve receber o valor do salário
#--- A função deve fazer o cálculo de acordo com as regras de faixa salárial e atribuir o resultado em uma variável
#--- O resultado deve ser impresso pela função juntamente com uma frase e utilizando f-string
#--- Deve ser realizada a leitura do salário fora da função e armazenada em uma variável
#--- Chamar a função e passar a variável do salário criada durante a leitura do console

def desconto():
    salario = float(input('Digite o salário: '))
    if salario <= 1000:
        desconto = salario * 0.01
    elif salario >= 1000.01 and salario <=3000:
        desconto = salario * 0.015
    elif salario >= 3000.01 and salario <=6000.00:
        desconto = salario * 0.02
    else:
        desconto = salario * 0.025
    print(f'O desconto de R${salario} é de: R${desconto}')


desconto()

     
# def faixa1(salario):
#     return (salario * 0.01)

# def faixa2(salario):
#     return (salario * 0.015)

# def faixa3(salario):
#     return (salario * 0.02)

# def faixa4(salario):
#     return (salario * 0.025)

# salario = float(input('Digite o salário: '))

# faixa1 = faixa1(salario)
# faixa2 = faixa2(salario)
# faixa3 = faixa3(salario)
# faixa4 = faixa4(salario)

# if salario <= 1000:
#     print(f'O desconto é de R$: {faixa1:.2f}')

# elif salario >= 1000.01 and salario <=3000:
#      print(f'O desconto é de R$: {faixa2:.2f}\n')

# elif salario >= 3000.01 and salario <=6000.00:
#      print(f'O desconto é de R$: {faixa2:.2f}\n')

# else:
#      print(f'O desconto é de R$: {faixa4:.2f}\n')