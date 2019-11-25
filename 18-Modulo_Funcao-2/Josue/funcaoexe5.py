def checar(digito):
    if (digito == 0):
        retorno = ('Usuário realizou o logoff')
    elif (digito > 0 and digito < 2):
        retorno = ('Cadastro de usuários')
    elif (digito > 1 and digito < 3 ):
        retorno = ('Lista de usuários cadastrados')    
    else:
        retorno = ('Opção inválida') 
    return retorno