#--- Exercício 5  - Print -2
#--- Crie uma variável string com seu nome completo
#--- Crie uma variável com o endereço de seu perfil no linkedin
#--- Crie uma variável com o endereço de seu perfil no github
#--- Faça a impressão das variáveis simulando um perfil
#--- Utilize f-string para concatenação das strings
#--- Imprima um cabeçalho e um rodapé utilizando multiplicação de strings
#--- Imprima espaçamentos utilizando tabulação e quebra de linha

nome='Victor D Simão'
idade=int(31)
linkedin='https://www.linkedin.com/in/victordiogosimao/'
github='https://github.com/VictorSimao'

print('='*46,)
print('Rede Social Padawan Proway - Blumenau - 11/2019')
print('='*46)
print('')
print('     Bem Vindo - Rede Social de Links')
print('')
print('='*20,'DADOS','='*20)
print(f'Nome: {nome}\nIdade: {idade} anos')
print('='*46)
print('='*20,'LINKS','='*20)
print(f'Linkedin:\n{linkedin}\nGithub:\n{github}')
print('='*46)
print('='*46,)
print('         que a força esteja com voce')
print('='*46)