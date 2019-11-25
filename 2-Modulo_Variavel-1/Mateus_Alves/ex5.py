#--- Exercício 5  - Variáveis
#--- Imprima os dados de 5 papéis cotados na bolsa de valores de SP
#--- Cada Papel apresentado deve possuir: 
#---    Nome 
#---    Tipo
#---    Cotação Atual
#---    Valor Mínimo do dia 
#---    Valor Máximo do dia 
#--- Os dados dos papéis devem estar em variáveis
#--- A tela deve conter cabeçalho e rodapé
#--- Deve ser usado os caracteres de tabulação e quebra de linha
nome_1 = 'Petrobras (PETR4)'
nome_2 = 'Copel (CPLE6)'
nome_3 = 'Lojas Marisa (AMAR3)'
nome_4 = 'JBS (JBSS3)'
nome_5 = 'Pine (PINE4)'
tipo_1 = 'Petróleo'
tipo_2 = 'Utilities'
tipo_3 = 'Varejo de moda'
tipo_4 = 'Carnes'
tipo_5 = 'Financeiro'
cotação_1 = 29.30
cotação_2 = 58.90
cotação_3 = 10.09
cotação_4 = 26.23
cotação_5 = 3.19
valmax1 = 30.10
valmax2 = 59.56
valmax3 = 10.09
valmax4 = 27.64
valmax5 = 3.26
valmin1 = 29.27
valmin2 = 58.41
valmin3 = 10.09
valmin4 = 26.10
valmin5 = 3.15

print('\nPapeis: \n')
print(f'Nome:{nome_1}, Tipo:{tipo_1}, Cotação:{cotação_1}, Valor Máximo do dia:{valmax1}, Valor Mínimo do dia:{valmin1}')
print(f'Nome:{nome_2}, Tipo:{tipo_2}, Cotação:{cotação_2}, Valor Máximo do dia:{valmax2}, Valor Mínimo do dia:{valmin2}')
print(f'Nome:{nome_3}, Tipo:{tipo_3}, Cotação:{cotação_3}, Valor Máximo do dia:{valmax3}, Valor Mínimo do dia:{valmin3}')
print(f'Nome:{nome_4}, Tipo:{tipo_4}, Cotação:{cotação_4}, Valor Máximo do dia:{valmax4}, Valor Mínimo do dia:{valmin4}')
print(f'Nome:{nome_5}, Tipo:{tipo_5}, Cotação:{cotação_5}, Valor Máximo do dia:{valmax5}, Valor Mínimo do dia:{valmin5}\n')
