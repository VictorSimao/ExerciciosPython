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

print('='*80,'\n'*3)
op_1 =  1 
op_2 =  2 
op_3 =  3 
op_4 =  4 
op_5 =  5 
print(f'{op_1}: Cadastrar funcionario:\n{op_2}: Listar funcionario\n{op_3}: Editar funcionario\n{op_4}: Deletar funcionario\n{op_5}: Sair')
print('\n'*3,'='*80)