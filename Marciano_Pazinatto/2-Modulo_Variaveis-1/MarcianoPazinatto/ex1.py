#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante

nome=input('Digite o nome do Funcionário: ')
sobrenome=input('Digite o sobrenome: ')
cpf=input('Digite o cpf: ')
rg=input('Digite o RG: ')
salario=float(input('Digite o sálario do funcionário: '))
print(f'Funcionário{nome}\nseu sobrenome é {sobrenome}\nCPF nº {cpf}\nRG nº {rg}\ne salário de R${salario:.2f}')