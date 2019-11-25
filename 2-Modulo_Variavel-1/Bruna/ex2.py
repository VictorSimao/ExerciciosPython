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

print('='*100, '\n'*3)

Nome = input('Digite o seu nome: ')
Sobrenome = input('Digite o seu sobrenome: ')
CPF = input('Digite o seu CPF: ')
RG = input('Digite o seu RG: ')
Salario = float(input('Informe o seu Salário: R$  '))

print(f'Nome: {Nome} \nSobrenome: {Sobrenome} \nCPF: {CPF} \nRG: {RG} \nSalário: {Salario:.2f}')
print('\n'*3,'--'*50)