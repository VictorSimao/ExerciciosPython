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

print('='*135)
for i in range(1,6):
    nome = input(f'\nDigite o nome do papel {i}: ')
    tipo = input('Digite o tipo: ')
    cotacaoatual = input('Digite a cotação atual: ')
    valormin = input('Digite o valor minímo do dia: ')
    valormax = input('Digite o valor máximo do dia: ')
    print(' ')
print('='*135)