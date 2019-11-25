#--- Exercício 5  - Print -2
#--- Crie uma variável string com seu nome completo
#--- Crie uma variável com o endereço de seu perfil no linkedin
#--- Crie uma variável com o endereço de seu perfil no github
#--- Faça a impressão das variáveis simulando um perfil
#--- Utilize f-string para concatenação das strings
#--- Imprima um cabeçalho e um rodapé utilizando multiplicação de strings
#--- Imprima espaçamentos utilizando tabulação e quebra de linha
linha = '='*50
nome = 'Matheus Schuetz de Aviz'
linkedin = 'https://www.linkedin.com/in/matheus-schuetz-de-aviz-532bb0188/'
git = 'https://github.com/matheusschuetz'

print(f'{linha}\n{nome}\n{linha}\n Perfis:\nLinkedin:{linkedin}\nGithub:{git}\n{linha}')