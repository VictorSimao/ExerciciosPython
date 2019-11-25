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


print('='*50,'\n', 'Bem vindo', '\n'*2)

Cadastrar = ('Cadastrar funcionário')
Listar = ('Listar funcionários')
Editar = ('Editar funcionário')
Deletar = ('Deletar funcionário')
Sair = ('Sair')

print('\n'*3)
print('{}\n{}\n{}\n{}\n{}'.format(Cadastrar, Listar, Editar, Deletar, Sair))
print('\n'*3, '='*50)