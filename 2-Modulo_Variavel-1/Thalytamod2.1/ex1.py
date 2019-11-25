#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante

nome = input('Nome:')
sobrenome = input('Sobrenome:')
cpf = input('CPF:')
rg = input('Registro Geral:')
salario = float(input('Salario: '))

print (f'Nome:{nome} \nSobrenome: {sobrenome} \nCPF: {cpf} \nRG: {rg} \nSalario: {salario}')