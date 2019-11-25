#--- Exercicio 2  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia os dados de um cliente
#--- Cliente: Nome, Sobrenome, ano de nascimento
#--- Exiba uma mensagem de boas vindas para o cliente
#--- Exiba um menu: Produtos alcoolicos e Produtos não alcoolicos, Sair
#--- Caso o cliente seja menor de idade o item 'produtos alcoolicos' não deve ser exibido
#--- Leia a opção digitada e crie uma tela para cada opção

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
ano = int(input('Digite seu ano de nascimento: '))

print('\nSEJA BEM VINDO!!!')

nascimento = 2019-ano

if nascimento>=18:
    opcao1 = int(input('\nMENU:\n1 - Produtos Alcoólicos\n2 - Não alcoólicos\n3 - Sair\n\nDigite o número desejado: '))
    if opcao1 == 1:
        print('\nProdutos Alcoólicos:\nAntartica\nBohemia\nBrahma\nBudweiser\nCorona\nSkol')
    elif opcao1 == 2:
        print('\nProdutos Não Alcoólicos:\nGuarana Antárctica\nH2O!\nPepsi\nSukita')
    elif opcao1 == 3:
        print('\nPrograma Encerrado')
    else:
        print('ERROR 404')
else:
    opcao2 = int(input('\nMENU:\n1 - Produtos Não Alcoólicos\n2 - Sair\n\nDigite o número desejado: '))
    if opcao2 == 1:
        print('\nProdutos Não Alcoólicos:\nGuarana Antárctica\nH2O!\nPepsi\nSukita')
    elif opcao2 == 2:
        print('\nPrograma Encerrado')
    else:
        print('ERROR 404')