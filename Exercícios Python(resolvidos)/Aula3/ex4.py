#--- Exercicio 4  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que realize a autenticação de usuário
#--- Crie duas variáveis para conter o usuário e senha padrão do sistema
#--- Leia o usuário e senha informados pelo usuário via função input()
#--- Valide se usuário e senha estão corretos
#--- Caso o usuário e senha estejam corretos informe com mensagem de boas vindas
#--- Caso o usuário e senha estejam incorretos informe com mensagem de falha de login


nome = 'Keunan013'
senha = 1313131313

nomeconfirm = input('Digite seu nome de usuário: ')
senhaconfirm = int(input('Digite sua senha: '))

if nomeconfirm == nome and senhaconfirm == senha:
    print(f'\nSeja Bem Vindo {nome}!!!')
else:
    print('\nFalha de login!')