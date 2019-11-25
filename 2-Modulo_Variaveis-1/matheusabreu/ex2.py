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
o1 = 1
o2 = 2
o3 = 3
o4 = 4
o5 = 5

print('#'*55, '\n'*3, sep='')
print(f'MENU \n{o1} - Cadastrar funcionário \n{o2} - Listar funcionários \n{o3} - Editar funcionário \n{o4} - Deletar funcionário \n{o5} - Sair')
print('\n'*3, '#'*55, sep='')