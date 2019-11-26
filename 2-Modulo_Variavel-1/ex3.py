#--- Exercício 3  - Variáveis
#--- Imprima dois parágrafos do último livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- As informações do Livro serão: 
#---    Título
#---    Edição
#---    Autor
#---    Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro



titulo = 'Cosmos'
edicao = 'Edição: 1'
autor = 'Carl Sagan - Neil deGrasse Tyson'
datapub = '6 de novembro de 2017'
cap = 'VI - Historias de Viajantes - Pg 165'

print('''\n\n\n     Tanto o campo magnético de Saturno como o de Júpiter
captam e aceleram as partículas carregadas do vento solar.
Quando uma partícula dessas salta de um pólo magnético a outro,
deve atravessar o plano equatorial de Saturno. Se houver uma
partícula do anel no caminho, o próton ou elétron é absorvido por
esta pequena bola de neve. Como resultado, em ambos os
planetas os anéis limpam os cinturões radioativos, que existem
somente interna e externamente aos anéis. Uma lua próxima de
Júpiter ou Saturno traga as partículas do cinturão, sendo uma das
novas luas de Saturno descoberta desta forma: a Pioneer 11
descobriu uma falha inesperada nos cinturões radioativos, causada
pela varredura das partículas carregadas por uma lua não
conhecida anteriormente.
     O vento solar desliza no sistema solar exterior bem além da
órbita de Saturno. Quando a Voyager chegar a Urano e às órbitas
de Netuno e Plutão, se os instrumentos ainda estiverem
funcionando, certamente sentirão a sua presença, o vento entre os
mundos, o topo da atmosfera do Sol levado ao domínio das
estrelas. A duas ou três vezes a distância do Sol a Plutão, a
pressão dos prótons e elétrons se torna maior que a exercida lá
pelo vento solar. Aquele local, chamado heliopausa, é uma
definição da fronteira externa do Império do Sol. Mas a espaçonave
Voyager mergulhará e penetrará na heliopausa em algum momento
na metade do século XXI, deslizando no oceano do espaço, nunca
penetrando em outro sistema solar, destinada a vagar pela
eternidade entre as linhas estelares e a completar a primeira
circunavegação do centro massivo da Via-láctea, daqui a algumas
centenas de milhões de anos. Aventuramo-nos em viagens épicas.''')

print(f'\nTitulo: {titulo}, Autor: {autor}\nEdição: {edicao}, Data de Publicação: {datapub} ')
print(f'Capitulo: {cap}')


