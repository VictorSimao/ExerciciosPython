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

print ('\t''='*10,'\n'*3)
print ('\t''SISTEMA CADASTRO DE FUNCIONÁRIOS')
print ('\n'*3)
print ('MENU')
Cadastrar_funcionário = 1
Listar_funcionário = 2
Editar_funcionário = 3
Deletar_funcionário = 4
SAIR = 5
print ('{} Cadastrar o funcionário'.format(Cadastrar_funcionário)) 
print ('{} Listar'.format(Listar_funcionário)) 
print ('{} Editar informação'.format(Editar_funcionário)) 
print ('{} Deletar'.format(Deletar_funcionário)) 
print ('{} SAIR'.format(SAIR))
print ('\n'*3)

print ('\t''='*10,'\n'*3)
