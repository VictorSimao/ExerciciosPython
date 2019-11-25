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
print('\n','='*20,'Cadastramento de Funcionarios HBSIS','='*20,'\n'*3)

n1 = 'Cadastrar Funcionario(a)'
n2 = 'Listar Funcionario(a)'
n3 = 'Editar Funcionario(a)'
n4 = 'Deletar Funcionario(a)'
n5 = '\n\t Sair'
print('&'*30)
print('\n\t Menu Principal')
print(f"\n {n1}\n{n2}\n{n3}\n{n4}\n{n5}\n\n\n")
print('\n','&'*30)
