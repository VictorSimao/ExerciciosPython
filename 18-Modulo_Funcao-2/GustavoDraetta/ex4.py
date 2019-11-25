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

# --- DEFs ---
def contribucao(salario):
    # Verifica se o salario está entre dois valores (informados no enunciado) e calcula a contribuicaoa partir dos valores do enunciado
    if salario > 1000.00 and salario < 3000.00: 
        contribucao = salario * 1.5

    elif salario > 3000.00 and salario < 6000.00:
        contribucao = salario * 2

    elif salario > 6000:
            contribucao = salario * 2.5

    else: 
        contribucao = salario
    
    print(f'CONTRIBUICAO: {contribucao}') # Mostra a contribuição

    return 0

# --- ENTRADA ---
print('\n'*2, '='*50, '\n')
salario = float( input('Digite o valor do salário do funcionario: ') )

# --- PROCESSAMENTO/SAIDA ---
contribucao(salario)
print('\n'*2, '='*50, '\n')
