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

print('='*25,'MENU','='*25)

n1=1
n2=2
n3=3
n4=4
n5=5

print(' Cadastrar funcionario {} \n Listar funcionários {} \n Editar funcionário {}\n Deletar funcionário {}\n Sair {}'.format(n1,n2,n3,n4,n5))
print('='*56)