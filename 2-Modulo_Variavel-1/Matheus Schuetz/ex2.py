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
cadastro = 'Cadastrar Funcionario(1)'
listar = 'Listar Funcionarios(2)'
editar = 'Editar Funcionarios(3)'
deletar = 'Deletar Funcionarios(4)'
sair = 'SAIR(5)'
roda = '='*50
linhas = '\n'*3
print(f'{roda}{linhas}Sistema de Cadastramento de funcionarios{linhas}{roda}\n{cadastro}\n{listar}\n{editar}\n{deletar}\n{sair}{linhas}{roda}')