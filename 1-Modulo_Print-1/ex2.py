#--- Exercício 2 - Impressão de dados com a função Print
#--- Imprima textos que simulem o menu de uma aplicação
#--- A aplicação será de cadastro de pessoas
#--- O menu deve conter as opções de Cadastrar, Alterar, Listar e Sair
#--- Cada opção deve vir acompanhada de um número
#--- Cada opção deve ser impressa em uma linha diferente

print('~'*25)
print('Escolha uma Opcao de Cadastro')
print('1 - Cadastrar novo')
print('2 - Alterar Cadastro')
print('3 - Listar Pessoas')
print('4 - Sair')
print('~'*25)
op = int(input('Digite a Opcao: '))
print(f'Opcao escolhida: {op}')
print('~'*25)
