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

cabecalho = 'PAPÉIS BOVESPA'
print(cabecalho,'\n','\t','='*50)

nome = 'Nome: JBS ON'
tipo = 'Tipo: Ações'
cotacao_atual = 'CotaÇão Atual: 27.84'
valor_minimo = 'Valor Mínimo: 25.41'
valor_maximo = 'Valor Máximo: 27.86'
print('\t', nome, '\n','\t', tipo, '\n','\t', cotacao_atual, '\n','\t', valor_minimo, '\n','\t', valor_maximo, '\n')
nome1 = 'Nome: BRF FOODS ON'
tipo1 = 'Tipo: Ações'
cotacao_atual1 = 'CotaÇão Atual: 36.11'
valor_minimo1 = 'Valor Mínimo: 33.91'
valor_maximo1 = 'Valor Máximo: 36.19'
print('\t', nome1, '\n','\t', tipo1, '\n','\t', cotacao_atual1, '\n','\t', valor_minimo1, '\n','\t', valor_maximo1, '\n')
nome2 = 'Nome: MARFRIG ON'
tipo2 = 'Tipo: Ações'
cotacao_atual2 = 'CotaÇão Atual: 11.26'
valor_minimo2 = 'Valor Mínimo: 10.80'
valor_maximo2 = 'Valor Máximo: 11.37'
print('\t', nome2, '\n','\t', tipo2, '\n','\t', cotacao_atual2, '\n','\t', valor_minimo2, '\n','\t', valor_maximo2, '\n')
nome3 = 'Nome: QUALICORP ON'
tipo3 = 'Tipo: Ações'
cotacao_atual3 = 'CotaÇão Atual: 36.75'
valor_minimo3 = 'Valor Mínimo: 34.99'
valor_maximo3 = 'Valor Máximo: 37.05'
print('\t', nome3, '\n','\t', tipo3, '\n','\t', cotacao_atual3, '\n','\t', valor_minimo3, '\n','\t', valor_maximo3, '\n')
nome4 = 'Nome: CIELO ON'
tipo4 = 'Tipo: Ações'
cotacao_atual4 = 'CotaÇão Atual: 7.82'
valor_minimo4 = 'Valor Mínimo: 7.48'
valor_maximo4 = 'Valor Máximo: 7.89'
print('\t', nome4, '\n','\t', tipo4, '\n','\t', cotacao_atual4, '\n','\t', valor_minimo4, '\n','\t', valor_maximo4, '\n')

rodape = 'VALORES SUJEITOS A ALTERAÇÃO'
print('\t','='*50,'\n', rodape)