#--- Exercício 4 - Impressão de dados com a função Print
#--- Imprima textos que simulem a tela inicial de um sistema de compra de bebidas
#--- Nesta tela deve ter um cabeçalho, um menu e um rodapé
#--- O menu deve ter as opções: 
#---   1 - Listar bebidas alcoolicas
#---   2 - Listar bebidas não alcoolicas
#---   3 - Visualizar Pedido
#---   4 - Sair

nal={1:'Sukita',2:'Guaraná Antartica',3:'Soda',4:'Pepsi'}
al={11:'Brahma',12:'Skol',13:'Original',14:'Stella Artois'}
lista=[]
print('\n'*1,'='*51)
print('*'*20,'MERCADOTECH','*'*20)
i=0
while i!=5:
    print('(1)LISTAR BEBIDAS ALCOÓLICAS.\n(2)LISTAR BEBIDAS ALCOÓLICAS.\n(3)INSERIR.\n(4)VIZUALIZAR PEDIDO\n(5)SAIR.','\n'*1,'='*51)
    i=int(input('Digite a opção: '))
    if i==1:
        print('Todas as bebidas alcoólicas',al.values())
    elif i==2:    
        print('Todas as bebidas não alcoólicas', nal.values())
    elif i==3: 
        print('PRODUTOS DISPONIVEIS: \nSukita,','Guaraná Antartica,','Soda,','Pepsi,','Brahma,','Skol,','Original,','Stella Artoisa,\n')  
        lista.append(input('Digite o nome das bebidas da lista acima que deseja adiquirir: ')),lista.append(input('Digite a quantidade dessa bebida: ')) 
    elif i==4:
        print(lista)       
    elif i==5:
        print('Saindo...')
    else:
        print('*'*15,'Opção incorreta, tente novamente!!!!!!','*'*15,'\n\n')    
      

print('\n'*1,'='*51,'\n'*1,'='*51)
    
