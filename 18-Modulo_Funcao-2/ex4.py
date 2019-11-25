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

def calcula_contribuicao_previdencia(salario):
    if(salario >= 0) and (salario <= 1000):
        contribuicao_previdencia = salario * 0.01
        salario_liquido = salario - contribuicao_previdencia
        return(f'Salário do funcionário: {salario:.2f}\nContribuição Necessária: {contribuicao_previdencia:.2f}\nSalário Líquido: {salario_liquido:.2f}')
    elif(salario >= 1000.01) and (salario <= 3000):
        contribuicao_previdencia = salario * 0.015
        salario_liquido = salario - contribuicao_previdencia
        return(contribuicao_previdencia)
    elif(salario >= 3000.01) and (salario <= 6000):
        contribuicao_previdencia = salario * 0.02
        salario_liquido = salario - contribuicao_previdencia
        return(contribuicao_previdencia)
    elif(salario > 6000.01):
        contribuicao_previdencia = salario * 0.025
        salario_liquido = salario - contribuicao_previdencia
        return(contribuicao_previdencia)

salario = float(input('Informe o seu salário\n'))

print(calcula_contribuicao_previdencia(salario))