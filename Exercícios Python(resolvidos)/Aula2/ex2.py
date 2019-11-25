#--- Exercicio 2  - Variávies e impressão com interpolacão de string
#--- O menu deve ser impresso com a função format() para concatenar os números da opções, que devem ser números inteiros

print('='*135)
print('\n\n\nMENU DE CADASTRO DE FUNCIONÁRIOS')
print('\n1 - Cadastrar Funcionário\n2 - Alterar Cadastro de Funcionários\n3 - Listar Funcionários\n4 - Sair\n')
opcao = int(input('Digite o número da opção desejada: '))
print(f'A opção desejada foi {opcao}')
print('\n\n')
print('='*135)