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
print('@'*20,'BOLSA DE VALOR SP','@'*20)
for a in range(1,6):
    print(f'\nDados da Bolsa de valores Papel ({a})')
    n1=input('Digite o nome: ')
    n2=input('Digite o Tipo: ')
    n3=float(input('Digite a Cotação atual: '))
    n4= float(input('Valor minimo do dia: '))
    n5= float(input('Valor maximo do dia: '))
print('\t'*3,'@'*20,'BOLSA DE VALOR SP','@'*20,'--24/11/2019 15:40')


