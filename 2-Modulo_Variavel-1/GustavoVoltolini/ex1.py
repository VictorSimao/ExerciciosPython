#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante

nome = input('Nome:')
sobrenome = input('Sobrenome:')
cpf = input('Cpf:')
rg = input('Rg:')
sal = float(input('Salario bruto:'))

print (f'Nome:{nome}\nSobrenome:{sobrenome}\nCpf:{cpf}\nRg:{rg}\nSalario{sal:2.2f}')

