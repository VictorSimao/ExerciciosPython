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

print('--'*40)

cabecalho = ('I B O V E S P A    25/11/2019')
papel1 = ('AMBEV - ABEV3\nTipo: Ordinária\nValor Minimo: $ 17,94\nValor Maximo: $ 18,29')
papel2 = ('PETROBRÁS - PETR3\nTipo: Ordinária\nValor Minimo: $ 32,22\nValor Maximo: $ 32,57')
papel3 = ('ELETROBRAS - ELET3 \nTipo: Ordinária\nValor Minimo: $ 35,69\nValor Maximo: $ 36,66')
papel4 = ('Cia Vale Rio Doce - VALE3\nTipo: Ordinária\nValor Minimo: $ 48,55\nValor Maximo: $ 50,03')
papel5 = ('CIELO SA - CIEL3\nTipo: Ordinária\nValor Minimo: $ 7,88\nValor Maximo: $ 8,19')
print(f'\n{cabecalho}\n\nFolha 1: {papel1}\n\nFolha 2: {papel2}\n\nFolha 3: {papel3}\n\nFolha 4: {papel4}\n\nFolha 5: {papel5}\n')

print('--'*40)