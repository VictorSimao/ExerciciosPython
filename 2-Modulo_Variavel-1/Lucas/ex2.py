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

print('='*50,'\n'*3)
print('1-Cadastrar funcionario \n2-Listar funcionários \n3-Editar funcionário \n4-Deletar funcionário \n5-Sair')
op=int(input('O que deseja fazer?'))
print(f'Você escolheu a opção {op}')
print('\n'*3,'='*50)