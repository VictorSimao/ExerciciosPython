#--- Exercício 2 - Impressão de dados com a função Print
#--- Imprima textos que simulem o menu de uma aplicação
#--- A aplicação será de cadastro de pessoas
#--- O menu deve conter as opções de Cadastrar, Alterar, Listar e Sair
#--- Cada opção deve vir acompanhada de um número
#--- Cada opção deve ser impressa em uma linha diferente
lista=[]
print('*'*60)
print('*'*25,'CADASTRO','*'*25)
print('(1).Para Cadastrar Cliente\n\n(2).Alterar Cadastro\n\n(3).Listar Clientes\n\n(4).Sair\n')
i=0
while i!=4:
    i=int(input('Digite uma opção: '))
    if i==1:
        lista.append(input('Digite o nome: '))
    elif i==2:
        print(lista,'\nEscolha a posição que o elemento deve ser modificado iniciando em 0(zero)\n escolha uma opção:')
        j=int(input('Digite a posição: '))
        k=input('Digite o que será adicionado nesta posição')
        lista[j]=k
    elif i==3:
        print('Nomes:',lista)
    elif i==4:
        print("Saindo...")
    else:
        print('Opção inválida')    

print('*'*60)        

