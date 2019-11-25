#--- Exercício 4  - Print -2
#--- Crie uma variável e atribua uma string com o seu nome
#--- Crie uma variável de nome linkedin e atribua um valor booleano 
#--- Crie uma variável de nome instagran e atribua um valor booleano 
#--- Crie uma variável de nome facebook e atribua um valor booleano 
#--- Crie uma variável de nome telegram e atribua um valor booleano 
#--- Imprima as cinco variáveis juntamente com uma frase dizendo se possui conta nas mídias citadas 
#--- Para impressão utilize f-string

print('='*50, '\n')

linkedin = bool('tem')
instagram = bool('')
facebook = bool('tem')
telegram = bool('')

if linkedin:
    print('Você possui linkedin')
else:
    print('Você não possui linkedin')

if instagram:
    print('Você possui instagram')
else:
    print('Você não possui instagram')

if facebook:
    print('Você possui facebook')
else:
    print('Você não possui facebook')

if telegram:
    print('Você possui telegram')
else:
    print('Você não possui telegram')


print('\n', '='*50)