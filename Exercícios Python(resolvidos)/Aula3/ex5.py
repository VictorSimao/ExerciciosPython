#--- Exercicio 5  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia o salário de uma pessoa
#--- Use o método 50-20-10-20 - https://www.jaseimevirar.com/blog/como-voce-organiza-seu-orcamento-mensal/
#--- Informe os percentuais e valores que a pessoa deve utilizar em cada categoria
#--- Deve ser utilizado a função format e os caracteres de tabulação e quebra de linha para cada categoria
#50% gastos, 20% investimentos a longo prazo, 10% investimentos a curto prazo, 20% livre

salario = float(input('Digite seu salário: '))

salario50 = salario*0.5
salario20 = salario*0.2
salario10 = salario*0.1
salario20_2 = salario*0.2

print(f'''\nValor do salário: {salario:.2f}\n50% ({salario50:.2f}) para gastos;
20% ({salario20:.2f}) para investimentos a longo prazo;\n10% ({salario10:.2f} para investimentos;
20% ({salario20_2:.2f}) são livres.''')