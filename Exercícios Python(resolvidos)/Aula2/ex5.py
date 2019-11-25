#--- Exercicio 5  - Variávies e impressão com interpolacão de string
#--- Imprima os dados de 5 papeis cotatos na bolsa de valors de SP
#--- Os dados dos papeis devem estar em variáveis
#--- Papel: Nome, Tipo, Cotação Atual e Valores Min e Max do dia
#--- A tela deve conter cabeçalho e rodapé

print('='*135)
for i in range(1,6):
    nome = input(f'\nDigite o nome do papel {i}: ')
    tipo = input('Digite o tipo: ')
    cotacaoatual = input('Digite a cotação atual: ')
    valormin = input('Digite os valores minímos do dia: ')
    valormax = input('Digite os valores máximos do dia: ')
    print(' ')
print('='*135)
