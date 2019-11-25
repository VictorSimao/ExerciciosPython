#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante

Nome = input('Digite o seu nome: ')
Sobrenome = input('Digite o seu sobrenome: ')
CPF = input('Digite o seu CPF: ')
RG = input('Digite o seu RG: ')
Salario = float(input('Informe o seu Salário: R$  '))

print(f'Nome: {Nome} \nSobrenome: {Sobrenome} \nCPF: {CPF} \nRG: {RG} \nSalário: {Salario:.2f}')