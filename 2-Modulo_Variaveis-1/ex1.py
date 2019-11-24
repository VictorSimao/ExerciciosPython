#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante

Nome = input('Digite o seu nome: ')
Sobrenome =input('Digite seu Sobrenome: ')
Cpf = int(input('Digite seU CPF: '))
Rg = int(input('Digite seu RG: '))
Salario = float(input('Digite seu salário: '))


print(f'\n Nome do funicionario: {Nome} \n Sobrenome: {Sobrenome} \n CPF: {Cpf} \n RG: {Rg} \n Salario: R$:{Salario:.2f}')