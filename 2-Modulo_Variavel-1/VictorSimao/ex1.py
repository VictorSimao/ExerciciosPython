#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante

nome=input('Digite o nome: ')
sobrenome=input('Digite o sobrenome: ')
cpf=input('Digite o CPF: ')
rg=input('Digite o RG: ')
salario=float(input('Digite o Salario: '))

print('\n'*100)

print(f'Nome {nome}\nSobrenome {sobrenome}\nCPF {cpf}\nRG {rg}\nSalario {salario:.2f}')