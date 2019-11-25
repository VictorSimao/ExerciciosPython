def calculo_previ(salario):
    if(salario > 0 and salario <= 1000.00):
        previ = salario * 0.01
    elif (salario >= 1000.01 and salario <=3000.00 ):
        previ = salario * 0.015
    elif (salario >= 3000.01 and salario <=6000.00 ):
        previ = salario * 0.02    
    elif (salario > 6000.01):
        previ = salario * 0.025   
    return previ