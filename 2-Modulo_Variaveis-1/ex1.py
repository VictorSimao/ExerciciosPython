#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante
nome = input('Digite o nome do funcionário: ')
sobrenome = input('Digite o sobrenome do funcionário: ')
cpf = input('Digite o CPF do funcionário: ')
rg = input('Digite o RG do funcionário: ')
salario = float(input('Digite o salário do funcionário: '))

print(f'Nome: {nome} \nSobrenome: {sobrenome} \nCPF: {cpf} \nRG: {rg} \nSalário: {salario:.2f}')