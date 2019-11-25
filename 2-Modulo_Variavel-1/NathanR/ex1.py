#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante

Nome = input('Digite o nome do funcionario: ')
Sobrenome = input('Digite o sobrenome do funcionario: ')
CPF = input('Digite o CPF do funcionario: ')
RG = input('Digite o RG do funcionario: ')
Salario = float(input('Digite o salário do funcionario: '))

print(f"Nome do funcionario: {Nome}\nSobrenome do funcionario: {Sobrenome}\nCPF do funcionario: {CPF}\nRG do funcionario: {RG}\nSalario do funcionario: {Salario:.2f}")
