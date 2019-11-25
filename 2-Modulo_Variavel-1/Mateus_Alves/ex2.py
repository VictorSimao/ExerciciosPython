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

print('=-='*30,'\n'*3)

nome = input('Insita o nome do funcionário: ')
sobrenome = input('Insita o sobrenome do funcionário: ')
cpf = int(input('Insita o CPF do funcionário: '))
rg = int(input('Insita o RG do funcionário: '))
salario = float(input('Insita o salário do funcionário: '))

print('\nNome: {}\nSobrenome: {}\nCPF: {}\nRG: {}\nSalário: {}\n'.format(nome,sobrenome,cpf,rg,salario))

print('\n'*3,'=-='*30)