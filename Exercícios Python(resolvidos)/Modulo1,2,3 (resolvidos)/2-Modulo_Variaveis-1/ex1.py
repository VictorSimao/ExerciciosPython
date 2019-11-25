#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
cpf = input('Digite seu CPF: ')
rg = input('Digite seu RG: ')
salario = float(input('Digite seu slário: R$ '))

print(f'\nSeu nome é {nome}\nSeu sobrenome é {sobrenome}\nSeu número de CPF é {cpf}\nSeu número de RG é {rg}\nSeu salário é {salario:.2f}')