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

print('=='*50)
n1 = 'BIDI4(Banco Inter SA)'
n2 = 'ITSA4 (Itausa Investimentos)'
n3 = 'ITUB4 (Itau Unibanco)'
n4 = 'OIBR3 (OI)'
n5 = 'MRVE3 (MRV Engenharia)'
t1 = 'Financeira'
t2 = 'Financeira'
t3 = 'Financeira'
t4 = 'Comunicação'
t5 = 'Construtora'
vmin1 = '13,56'
vmin2 = '13,42'
vmin3 = '35,16'
vmin4 = '0,98'
vmin5 = '16,36'
vmax1 = '14,9'
vmax2 = '13,66'
vmax3 = '35,79'
vmax4 = '1,02'
vmax5 = '17,45'
cot1 = '14,90'
cot2 = '13,63'
cot3 = '35,68'
cot4 = '1,00'
cot5 = '16,95'
print('\n','AÇÕES COTADAS PELA B3: ')
print(f'Ação: {n1} Tipo: {t1} Cotação atual: {cot1} Valor minimo do dia: {vmin1} Valor maximo do dia: {vmax1}')
print(f'Ação: {n2} Tipo: {t2} Cotação atual: {cot2} Valor minimo do dia: {vmin2} Valor maximo do dia: {vmax2}')
print(f'Ação: {n3} Tipo: {t3} Cotação atual: {cot3} Valor minimo do dia: {vmin3} Valor maximo do dia: {vmax3}')
print(f'Ação: {n4} Tipo: {t4} Cotação atual: {cot4} Valor minimo do dia: {vmin4} Valor maximo do dia: {vmax4}')
print(f'Ação: {n5} Tipo: {t5} Cotação atual: {cot5} Valor minimo do dia: {vmin5} Valor maximo do dia: {vmax5}\n')
print('=='*50)