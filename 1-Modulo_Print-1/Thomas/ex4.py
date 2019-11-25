#--- Exercício 4 - Impressão de dados com a função Print
#--- Imprima textos que simulem a tela inicial de um sistema de compra de bebidas
#--- Nesta tela deve ter um cabeçalho, um menu e um rodapé
#--- O menu deve ter as opções: 
#---   1 - Listar bebidas alcoolicas
#---   2 - Listar bebidas não alcoolicas
#---   3 - Visualizar Pedido
#---   4 - Sair

print('=' * 50)
print(f'1 - Listar bebidas alcoolicas\n2 - Listar bebidas não alcoolicas\n3 - Visualizar Pedido\n4 - Sair')
print('=' * 50)
opcao = int(input("Insira uma das opcoes a cima: "))

if opcao == 1:
    print("Listar bebidas alcoolicas")

elif opcao == 2:
    print("Listar bebidas não alcoolicas")

elif opcao == 3:
    print("Visualizar Pedido")

else:
    print("Sair")

