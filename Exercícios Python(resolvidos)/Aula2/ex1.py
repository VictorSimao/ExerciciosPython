#--- Exercicio 1  - Variávies e impressão com interpolacão de string
#--- Crie 5 variávies para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Os dados devem ser impressos utilizando a funcao format()
#--- Deve ser usado apenas uma vez a função print(), porem os dados devem ser apresentados um em cada linha
#--- O salario deve ser de tipo flutuante e na impressão deve apesentar apenas duas casas após a vírgula

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
cpf = input('Digite seu CPF: ')
rg = input('Digite seu RG: ')
salario = float(input('Digite seu slário: R$ '))

print(f'\nSeu nome é {nome}\nSeu sobrenome é {sobrenome}\nSeu número de CPF é {cpf}\nSeu número de RG é {rg}\nSeu salário é {salario:.2f}')