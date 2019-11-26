#--- Exercício 2  - Variáveis
#--- Crie um menu para um sistema de cadastro de funcionários
#--- O menu deve ser impresso com a função format()
#--- As opções devem ser variáveis do tipo inteiro
#--- As descrições das opções serão:
#---    Cadastrar funcionário
#---    Listar funcionários
#---    Editar funcionário
#---    Deletar funcionário
#---    Sair
#--- Além das opções o menu deve conter um cabeçalho e um rodapé
#--- Entre o cabeçalho e o menu e entre o menu e o rodapé deverá ter espaçamento de 3 linhas
#--- Deve ser utilizado os caracteres especiais de quebra de linha e de tabulação

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
cpf = input('Digite seu CPF: ')
rg = input('Digite seu RG: ')
salario = float(input('Digite seu slário: R$ '))
print(f'\nSeu nome é {nome}\nSeu sobrenome é {sobrenome}\nSeu número de CPF é {cpf}\nSeu número de RG é {rg}\nSeu salário é {salario:.2f}')
