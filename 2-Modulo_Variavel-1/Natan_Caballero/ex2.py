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

print('='*50, '\n'*3)

Cadastrar = int('1')
Listar = int('2')
Editar = int('3')
Deletar = int('4')
Sair = int('0')

print(f'Digite {Cadastrar} para cadastrar \nDigite {Listar} para listar \nDigite {Editar} para editar \nDigite {Deletar} para deletar \nDigite {Sair} para sair')

print('\n'*3, '='*50)
