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
n1 = 'BVMF'
n2 = 'AAPL34'
n3 = 'BIDI4'
n4 = 'OIBR4'
n5 = 'PETR4'

t1 = 'Varejo'
t2 = 'Tecnologia'
t3 = 'Banco'
t4 = 'Telefonia'
t5 = 'Petrolifera'

ca1 = 3659.19
ca2 = 110.16
ca3 = 14.99
ca4 = 1.32
ca5 = 29.98

vm1 = 3649.54
vm2 = 53.80
vm3 = 5.67
vm4 = 1.04
vm5 = 20.42

vma1 = 3659.19
vma2 = 112.99
vma3 = 24,59
vma4 = 1.92
vma5 = 31.23

print('*' * 50, '\n')
print(f'Nome: {n1} , Tipo: {t1} , Cotação Atual: {ca1} , Menor valor: {vm1} , Maior valor: {vma1}\n')
print(f'Nome: {n2} , Tipo: {t2} , Cotação Atual: {ca2} , Menor valor: {vm2} , Maior valor: {vma2}\n')
print(f'Nome: {n3} , Tipo: {t3} , Cotação Atual: {ca3} , Menor valor: {vm3} , Maior valor: {vma3}\n')
print(f'Nome: {n4} , Tipo: {t4} , Cotação Atual: {ca4} , Menor valor: {vm4} , Maior valor: {vma4}\n')
print(f'Nome: {n5} , Tipo: {t5} , Cotação Atual: {ca5} , Menor valor: {vm5} , Maior valor: {vma5}\n')
print('*' * 50)