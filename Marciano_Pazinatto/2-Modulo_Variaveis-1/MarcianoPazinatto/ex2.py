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
op1='1.......Cadastrar funcionário'
op2='2.......Listar funcionários'
op3='3.......Editar funcionário'
op4='4.......Deletar funcionário'
op5='5.......Sair'


print('*'*50,'\n'*3,'\t***OPÇÕES***\n{}\n{}\n{}\n{}\n{}'.format(op1,op2,op3,op4,op5))
print('\n'*3,'*'*50)
a=int(input('\nDigite a opção: '))
if a==1:
    print('Cadastrar Funcionários')        
elif a==2:
    print('Listar Funcionários')
elif a==3:
    print('Editar Funcionário')
elif a==4:
     print('Deletar Funcionário')
elif a==5:
    print('Saindo')    
else:
    print('opção Inválida')   
print('\n'*3,'*'*50)         
