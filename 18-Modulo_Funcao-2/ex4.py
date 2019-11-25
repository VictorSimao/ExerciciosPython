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

def previ (sl):
    if sl <=  1000:
        sl = (sl*0.01)
    elif sl >= 1001 and sl <= 3000:
        sl = (sl*0.015)
    elif sl >= 3000.01 and sl <= 6000:
        sl = (sl*0.020)
    else:
        sl =  (sl*0.025)
    return sl

sl = float(input('informe seu salário'))
print(f'O total de descontos do seu salário é de {previ(sl):.2f}')


previ(sl)