#--- Exercício 3  - Print -2
#--- Crie uma variável e atribua uma string com o nome de um cargo
#--- Crie uma variável e atribua um float com o salário
#--- Imprima as duas variáveis juntamente com uma frase utilizando a função format()

cargo = input("\nDigite seu cargo: ")
sal = float(input("Digite seu salario: "))

print(f'\nCargo: {cargo} \nSalario: {sal:0.2f}\n')