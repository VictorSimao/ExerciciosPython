#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante

nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
cpf = input("CPF: ")
rg = int(input("RG: "))
salario = float(input("Salario: "))

print(f'\nNome: {nome}\nSobrenome: {sobrenome}\nCPF: {cpf}\nRG: {rg}\nSalario: {salario}')