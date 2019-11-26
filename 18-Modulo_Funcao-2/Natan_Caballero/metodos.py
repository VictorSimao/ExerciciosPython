# print('='*50, '\n')
# print('\n', '='*50)

def vezes(n1, n2):
    r = n1 * n2
    return print(f'O resultado da multiplicação entre {n1} e {n2} é {r}')

def potencia(n1,n2):
    r = n1 ** n2
    print(f'O resultado da exponenciação é {r}')

def cabecalho(empresa, caracter):
    print(caracter*50, '\n')
    print
    print('\n', caracter*50)

def imposto(salario):
    if salario < 1000.00:
        n = (salario*0.01)
    elif salario < 3000.00:
        n = (salario*0.015) 
    elif salario < 6000.00:
        n = (salario*0.02)
    else:
        n = (salario*0.025)
    return n