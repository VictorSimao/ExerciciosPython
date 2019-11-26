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


print('-=-'*50)
print('\n'*3)

func = int(input('Funcionário: '))
lis_f = int(input('Listar funcionários: '))
edit_f = int(input('Editar funcionários: '))
del_f = int(input('Deletar Funcionário: '))
  

print(f'\n\tFuncionário: {func}\n\tListar funcionários: {lis_f}\n\tEditar Funcionários: {edit_f}\n\tDeletar Funcionário: {del_f} ')
print('\n')
print('SAIR')

print('\n'*3)
print('-=-'*50)


