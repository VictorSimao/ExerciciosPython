#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante


nome = input('Digite seu nome: ')
sobrenome = input('Sobrenome: ')
cpf = int(input('Digite seu CPF: '))
rg = int(input('Digite seu RG: '))
salario = float(input('Seu salário: R$ '))

print(f'\nNome: {nome} \nSobrenome: {sobrenome} \nCPF: {cpf} \nRG: {rg} Salário: R$ {salario} ')
