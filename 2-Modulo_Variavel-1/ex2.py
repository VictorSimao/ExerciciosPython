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


print('~'*50)
print('~'*2,' '*20,'~'*2,' '*20,'~'*2)
print('~'*50,'\n'*3)
print(f'        Escolha uma Opcao de Cadastro\n')
print(f'            1' + '- Cadastrar novo')
print(f'            2' + '- Alterar Cadastro')
print(f'            3' + '- Listar Pessoas')
print(f'            4' + '- Sair\n')
op = int(input('            Digite a Opcao: '))
print(f'\n            Opcao escolhida: {op}')
print('\n'*3)
print('~'*50)
print('~'*2,' '*20,'~'*2,' '*20,'~'*2)
print('~'*50)


