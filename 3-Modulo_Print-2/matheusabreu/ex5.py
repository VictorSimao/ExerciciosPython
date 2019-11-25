#--- Exercício 5  - Print -2
#--- Crie uma variável string com seu nome completo
#--- Crie uma variável com o endereço de seu perfil no linkedin
#--- Crie uma variável com o endereço de seu perfil no github
#--- Faça a impressão das variáveis simulando um perfil
#--- Utilize f-string para concatenação das strings
#--- Imprima um cabeçalho e um rodapé utilizando multiplicação de strings
#--- Imprima espaçamentos utilizando tabulação e quebra de linha

nome_comp = 'Matheus Abreu'
linkedin  = 'https://www.linkedin.com/in/matheuspsabreu'
github    = 'https://github.com/abreumatheus'

print('#'*55, '\n', sep='')
print(f'PERFIL \nNome: {nome_comp} \nLinkedIn: {linkedin} \nGithub: {github}')
print('\n', '#'*55, sep='')