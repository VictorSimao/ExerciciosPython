#--- Exercício 5  - Print -2
#--- Crie uma variável string com seu nome completo
#--- Crie uma variável com o endereço de seu perfil no linkedin
#--- Crie uma variável com o endereço de seu perfil no github
#--- Faça a impressão das variáveis simulando um perfil
#--- Utilize f-string para concatenação das strings
#--- Imprima um cabeçalho e um rodapé utilizando multiplicação de strings
#--- Imprima espaçamentos utilizando tabulação e quebra de linha

nome = input('Digite seu nome completo')
linkedin=input('Seu perfil linkedin')
github=input('Seu perfil github')

print('='*50,'\n'*2)
print(f'Nome {nome} \nPerfil linkedin {linkedin} \nPerfil github {github}')
print('\n'*2,'='*50)