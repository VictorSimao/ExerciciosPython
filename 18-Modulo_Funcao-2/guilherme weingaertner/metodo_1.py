def vezes(n1,n2):
    n3 = n1*n2
    return n3

def potencia(n1,n2):
    return(n1**n2)


def cabecalho(n1,n2):
    print(n2*80)
    print(n1)
    print(n2*80)
    return cabecalho

def imposto(salario):
    if salario < 1000.00:
        n7 = (salario*0.01)
    elif salario < 3000.00:
        n7 = (salario*0.015) 
    elif salario < 6000.00:
        n7 = (salario*0.02)
    else:
        n7 = (salario*0.025)

    return n7

def sair():
    return print('0-Usuário realizou o logoff')
    
def cadastrar():
   return print('1-Cadastro de usuários')

def listar():
   return print('2-Lista de usuários cadastrados')


    


    