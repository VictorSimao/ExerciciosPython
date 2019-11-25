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

print('\n'*3)
print('\t' 'Cadastro dos Funcionários')
print('\t','='*50,'\n'*3)

Cadastrar_funcionario = 1
Listar_funcionario  = 2
Editar_funcionario = 3
Deletar_funcionario = 4
Sair = ('5')

print('{} Cadastrar Funcionário: '.format(Cadastrar_funcionario))
print('{} Listar Funcionário: '.format(Listar_funcionario))
print('{} Editar Funcionário: '.format(Editar_funcionario))
print('{} Deletar Funcinário: '.format(Deletar_funcionario))
print('{} Sair: '.format(Sair))

print('\n'*3, '\t', '='*50)



print('\n'*3)
print('\t','Contato para dúvidas e infoarcões: (47) 3636/7070')






