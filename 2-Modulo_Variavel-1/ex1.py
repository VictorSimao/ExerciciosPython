#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante


Nome = input('Digite o nome:')
Sobrenome = input('Digite o Sobrenome:')
Cpf = input('Digite o cpf:')
Rg = input('Digite o rg:')
Salário = float(input('Digite o Salario:'))

print(f'Funcionario: {Nome}{Sobrenome}\nCPF:{Cpf}\nRG:{Rg}\nSalario: R${Salário:.2f}')

