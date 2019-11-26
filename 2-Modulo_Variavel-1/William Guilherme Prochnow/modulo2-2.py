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

print('='*50)
print('\n'*3)
funcionario1 = input('Cadastre o fucionário1:')
funcionario2 = input('Cadastre o fucionário2:')
funcionario3 = input('Cadastre o fucionário3:')
editar = 'Editar Funcinário'
deletar = 'Deletar funcinário'
sair = 'sair'
print('\n'*3)
print('='*50)
print(f'\tFuncionário1:{funcionario1}\n\tFuncionário2:{funcionario2}\n\tFuncionário3:{funcionario3}')
print(editar)
print(deletar)
print(sair)