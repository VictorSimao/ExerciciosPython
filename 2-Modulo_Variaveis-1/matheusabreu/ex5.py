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
nome1 = 'ABEV3'
tipo1 = 'ON'
cot1  = 17.45
min1  = 17.31
max1  = 17.61

nome2 = 'PETR4'
tipo2 = 'PN'
cot2  = 29.30
min2  = 29.27
max2  = 30.10

nome3 = 'PETR3'
tipo3 = 'ON'
cot3  = 31.71
min3  = 31.59
max3  = 32.51

nome4 = 'VALE3'
tipo4 = 'ON'
cot4  = 47.00
min4  = 46.96
max4  = 47.58

nome5 = 'CIEL3'
tipo5 = 'ON'
cot5  = 7.89
min5  = 7.88
max5  = 8.19

print('#'*60, '\n', sep='')
print(f'AÇÃO 1 \nNome: {nome1} \nTipo: {tipo1} \nCotação Atual: {cot1:.2f} \nCotação Min: {min1:.2f} \nCotação Max: {max1:.2f}\n')
print(f'AÇÃO 2 \nNome: {nome2} \nTipo: {tipo2} \nCotação Atual: {cot2:.2f} \nCotação Min: {min2:.2f} \nCotação Max: {max2:.2f}\n')
print(f'AÇÃO 3 \nNome: {nome3} \nTipo: {tipo3} \nCotação Atual: {cot3:.2f} \nCotação Min: {min3:.2f} \nCotação Max: {max3:.2f}\n')
print(f'AÇÃO 4 \nNome: {nome4} \nTipo: {tipo4} \nCotação Atual: {cot4:.2f} \nCotação Min: {min4:.2f} \nCotação Max: {max4:.2f}\n')
print(f'AÇÃO 5 \nNome: {nome5} \nTipo: {tipo5} \nCotação Atual: {cot5:.2f} \nCotação Min: {min5:.2f} \nCotação Max: {max5:.2f}\n')
print('#'*60, sep='')