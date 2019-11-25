#--- Exercício 2 - Impressão de dados com a função Print
#--- Imprima textos que simulem o menu de uma aplicação
#--- A aplicação será de cadastro de pessoas
#--- O menu deve conter as opções de Cadastrar, Alterar, Listar e Sair
#--- Cada opção deve vir acompanhada de um número
#--- Cada opção deve ser impressa em uma linha diferente

print(f'1 - Cadastrar\n2 - Alterar\n3 - Listar\n4 - Sair')

opcao = int(input("Insira uma das opcoes a cima: "))

if opcao == 1:
    print("Cadastrar")

elif opcao == 2:
    print("Alterar")

elif opcao == 3:
    print("Listar")

else:
    print("Sair")