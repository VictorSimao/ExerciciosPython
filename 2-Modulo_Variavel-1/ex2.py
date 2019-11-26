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

op0 = '---Cadastrar fúncionários:'
op1 = '---Listar funcionário'
op2 = '---Editar funcionário'
op3 = '---Deletar funcionário'
op4 = '---sair'

print(' 0 = {} \n 1 = {} \n 2 = {} \n 3 = {} \n 4 = {}'.format(op0, op1, op2, op3, op4))
print('didgite uma opção')
g = int(input(''))
if g == 1:
    g == int(input('listar funcionário'))
elif g == 2:
    g == int(input('Editar funcionário'))
elif g == 3:
    g == int(input('Deletar funcionário'))
elif g == 4:
    g == int(input('Sair'))
else:
    print('ERRO')

print(g)

