#--- Exercício 3  - Print -2
#--- Crie uma variável e atribua uma string com o nome de um cargo
#--- Crie uma variável e atribua um float com o salário
#--- Imprima as duas variáveis juntamente com uma frase utilizando a função format()

cargo = input('Digite o cargo: ')
salario = float(input('Digite o salario: '))
print(f'\nO cargo {cargo} tem o salario base de R${salario:.2f}')