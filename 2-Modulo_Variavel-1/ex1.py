#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante

nome = input('\nDigite o nome: ')
sobrnome = input('Digite o sobrenome: ')
cpf = int(input('Digite o cpf: '))
rg = int(input('Digite o rg: '))
salario = float(input('Digite o salario: '))

print(f'\nNome{nome} {sobrnome} \nCpf: {cpf} \nRg: {rg} \nSalario: {salario}')