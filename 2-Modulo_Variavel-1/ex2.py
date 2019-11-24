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

cadastra = 1
lista = 2
edita = 3
deleta = 4
encerra = 5

print('-'*50, '\n\n\n\t{} - Cadastrar Funcionário.\n\t{} - Listar Funcionários.\n\t{} - Editar Dados.\n\t{} - Deletar Funcionário.\n\t{} - Encerrar Programa.\n\n\n'.format(cadastra , lista , edita , deleta , encerra), '-'*50)