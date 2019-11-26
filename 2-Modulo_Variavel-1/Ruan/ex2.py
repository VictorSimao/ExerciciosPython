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


print('\t','CADASTRO DE FUNCIONÁRIOS','\n')
print('\t','='*50,'\n'*3)

Cadastrar_funcionario = '1'
Listar_funcionario = '2'
Editar_funcionario = '3'
Deletar_funcionario = '4'
Sair = '5'
print(f'{Cadastrar_funcionario} = Cadastrar Funcionario')
print(f'{Listar_funcionario} = Listar Funcionario')
print(f'{Editar_funcionario} = Editar Funcionario')
print(f'{Deletar_funcionario} = Deeltar Funcionario')
print(f'{Sair} = Sair')

print('\n'*3,'PARA REVISÃO DE DADOS, ENTRE EM CONTATO (47) 3563-7107','\t')

print('\n'*3,'\t','='*50)

