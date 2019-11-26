def vezes(n1,n2):
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro numero: '))
    n3 = n1*n2
    return print(f'{n1} x {n2} = {n3}')

def potencia(n1,n2):
    n1 = int(input('Digite um numero:'))
    n2 = int(input('Digite o expoente:'))
    n3 = (n1**n2)
    return print("{} elevada a {}: {}".format(n1,n2,n3))


def cabecalho(n1,n2):
    n1 = input('Digite o nome do sistema:')
    n2 = input('Digite o caracter que será multiplicado para fazer a linha de cabeçalho:')
    print(n2*80)
    print(n1)
    print(n2*80)
    return print(f'{cabecalho(n2,n1)}')


def imposto(salario):
    salario = float(input('Digite seu salario:'))
    if salario < 1000.00:
        n7 = (salario*0.01)
    elif salario < 3000.00:
        n7 = (salario*0.015) 
    elif salario < 6000.00:
        n7 = (salario*0.02)
    else:
        n7 = (salario*0.025)

    return print(f'Sua contribuiçao é de: {n7}')

def sair():
    return '0-Usuário realizou o logoff'
    
def cadastrar():
   return '1-Cadastro de usuários'

def listar():
   return '2-Lista de usuários cadastrados'


    


    