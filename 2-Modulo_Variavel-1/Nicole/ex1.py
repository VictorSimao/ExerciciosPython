#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante

nome=input('Digite seu Nome: ')
sobrenome=input('Digite seu Sobrenome: ')
cpf=input('Digite seu Cpf: ')
rg=input('Digite seu Rg: ')
salario=float(input('Digite seu Salario: '))
print(f'''Nome: {nome}
Sobrenome: {sobrenome})
Cpf: {cpf}
Rg: {rg}
Salario: {salario}''')