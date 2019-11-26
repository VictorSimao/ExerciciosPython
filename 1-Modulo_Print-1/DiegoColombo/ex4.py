#--- Exercício 4 - Impressão de dados com a função Print
#--- Imprima textos que simulem a tela inicial de um sistema de compra de bebidas
#--- Nesta tela deve ter um cabeçalho, um menu e um rodapé
#--- O menu deve ter as opções: 
#---   1 - Listar bebidas alcoolicas
#---   2 - Listar bebidas não alcoolicas
#---   3 - Visualizar Pedido
#---   4 - Sair


print('-=-'*50)
print('\n')

n1 = 'Budweiser'
n2 = 'Patagonia'
n3 = 'Pepsi'
n4 = 'Gatorade'
print('\nBebidas Alcoólicas: ')
print(f'{n1} , {n2}')
print('\n')
des1 = input('Qual você deseja: ')
print('Quantidade:')
quant1 = int(input(''))
print(f'Seu pedido: {quant1} {des1} ')

print('\nBebidas Não Alcoólicas: ')
print(f'{n3}, {n4}')
print('\n')
des2 = input('Qual você deseja:')
print('Quantidade:')
quant2 = input('')
print(f'Seu pedido: {quant2} {des2} ')
print('\n')
print('Sair')
print('\n')
print('-=-'*50)