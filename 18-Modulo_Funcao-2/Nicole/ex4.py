#--- Exercício 4 - Funções - 2
#--- Crie uma função que realize o cálculo de contribuição do funcionário para a previdência da empresa
#--- O cálculo deve ser feito de acordo com a faixa salarial:
#---    De R$ 0000.00 Até R$ 1000.00 -> 1.0%
#---    De R$ 1000.01 Até R$ 3000.00 -> 1.5%
#---    De R$ 3000.01 Até R$ 6000.00 -> 2.0%
#---    Acima de R$ 6000.01 -> 2.5%
#--- A função deve receber o valor do salário
#--- A função deve fazer o cálculo de acordo com as regras de faixa salárial e atribuir o resultado em uma variável
#--- O resultado deve ser impresso pela função juntamente com uma frase e utilizando f-string
#--- Deve ser realizada a leitura do salário fora da função e armazenada em uma variável
#--- Chamar a função e passar a variável do salário criada durante a leitura do console

def salario(salario1):
    if salario1 >= 0000.00 and salario1<=1000.00:
        contri1=salario1*0.01
        print(f'A contribuicao será de {contri1}, e seu salario será {salario1-contri1}')

    elif salario1 >= 1000.01 and salario1<=3000.00:
        contri2=salario1*0.015
        print(f'A contribuicao será de {contri2}, e seu salario será {salario1-contri2}')

    elif salario1 >= 3000.01 and salario1<=6000.00:
        contri3=salario1*0.02
        print(f'A contribuicao será de {contri3}, e seu salario será {salario1-contri3}')

    elif salario1 >= 6000.01:
        contri4=salario1*0.025
        print(f'A contribuicao será de {contri4}, e seu salario será {salario1-contri4}')
    


s1=float(input('Digite seu salario: '))
salario(s1)