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
op1 = 1
op2 = 2
op3 = 3
op4 = 4
op5 = 5

print('*' * 50, '\n' * 3)
print('{} - Cadastro funcionario\n{} - Listar funcionarios\n{} - Editar funcionario\n{} - Deletar funcionario\n{} - Sair'.format(op1,op2,op3,op4,op5))
print('\n' * 3, '*' * 50)