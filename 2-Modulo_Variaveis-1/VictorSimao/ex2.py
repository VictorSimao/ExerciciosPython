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

print('='*46)
print('Cervejaria AMBEV / HBSIS - Blumenau - 17/11/19')
print('='*46)
print('\n'*3)
print('='*20,'MENU','='*20)
print(' '*12,f'Cadastrar Funcionario - 1')
print(' '*12,f'Listar Funcionarios - 2')
print(' '*12,f'Editar Funcionarios - 3')
print(' '*12,f'Deletar Funcionario - 4')
print(' '*12,f'Sair - 5')
menu=int(input(f'             Digite a opção: '))
print('='*46)
print('\n'*3)
print('='*46,)
print('         que a força esteja com voce')
print('='*46)