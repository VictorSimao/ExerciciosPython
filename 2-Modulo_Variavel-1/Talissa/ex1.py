#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante


nome = input('Digite o seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
cpf = input('Digite o seu CPF: ')
rg = input('Digite o seu RG: ')
salario = float(input('Digite o seu salário: '))

print(f'\nNome: {nome} \nSobrenome: {sobrenome} \nCPF: {cpf}\nRG: {rg} \nSalario: {salario}')