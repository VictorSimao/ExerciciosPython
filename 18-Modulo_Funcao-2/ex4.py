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

def contribuicao_previdencia(sal):
    if(sal >= 0) and (sal <= 1000):
        contribuicao = sal * 0.01
        sal_liq = sal - contribuicao
        return print(f'Salário do funcionário: {sal:.2f}\nContribuição Necessária: {contribuicao:.2f}\nSalário Líquido: {sal_liq:.2f}')
    elif(sal >= 1000.01) and (salario <= 3000):
        contribuicao = sal * 0.015
        sal_liq = sal - contribuicao
        return print(f'Salário do funcionário: {sal:.2f}\nContribuição Necessária: {contribuicao:.2f}\nSalário Líquido: {sal_liq:.2f}')
    elif(sal >= 3000.01) and (sal <= 6000):
        contribuicao = sal * 0.02
        sal_liq = sal - contribuicao
        return print(f'Salário do funcionário: {sal:.2f}\nContribuição Necessária: {contribuicao:.2f}\nSalário Líquido: {sal_liq:.2f}')
    elif(sal > 6000.01):
        contribuicao = sal * 0.025
        sal_liq = sal - contribuicao
        return print(f'Salário do funcionário: {sal:.2f}\nContribuição Necessária: {contribuicao:.2f}\nSalário Líquido: {sal_liq:.2f}')

salario = float(input('Informe o seu salário\n'))

contribuicao_previdencia(salario)