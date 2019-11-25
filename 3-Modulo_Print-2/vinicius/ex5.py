#--- Exercício 5  - Print -2
#--- Crie uma variável string com seu nome completo
#--- Crie uma variável com o endereço de seu perfil no linkedin
#--- Crie uma variável com o endereço de seu perfil no github
#--- Faça a impressão das variáveis simulando um perfil
#--- Utilize f-string para concatenação das strings
#--- Imprima um cabeçalho e um rodapé utilizando multiplicação de strings
#--- Imprima espaçamentos utilizando tabulação e quebra de linha

nome = input('\nDigite seu nome: ')

op = int(input(f'\nDigite qual link voce quer ver o {nome}: \n1- linkedin \n2- github \nOpção: '))

if op == 1:
    print('\nhttps://github.com/ViniciusNitzke')

if op == 2:
    print('\nhttps://www.linkedin.com/feed/')