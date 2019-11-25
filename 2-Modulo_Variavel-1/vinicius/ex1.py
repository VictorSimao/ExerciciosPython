#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante

nome = input('\nDigite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
cpf = int(input('Digite seu cpf'))
rg = int(input('Digite seu rg: '))
salario = float(input('Digite seu salario: '))

print(f'\nNome: {nome} {sobrenome} \nCpf: {cpf} \nRg: {rg} \nSalario: {salario}')