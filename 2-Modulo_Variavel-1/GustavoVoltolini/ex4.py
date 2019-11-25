#--- Exercício 4  - Variáveis
#--- Imprima a tela de um itinerário de viagem
#--- O itinerário deve conter o ponto de partida e de destino
#--- O ponto de partida e de destino devem estar armazenados em variáveis
#--- Entre os dois pontos deve conter no mínimo 10 pontos de parada
#--- Cada item ponto de parada deve conter data, hora e descrição
#--- Cada ponto de parada, data, hora e descrição será uma variável.
#--- O itinerário deve conter cabeçalho com o título da viagem, que será uma variável
#--- Deve ser usado os caracteres de tabulação e quebra de linha

titulo = 'Viagem dos sonhos'
partida = 'Rondonia'
destino = 'Acre'
lista_parada = ['Toca do leão', '08h', 'Visita ao habitat do Leão','Chuva de iguanas','09h','Passaremos pela floresta das iguanas onde vivem varias iguanas no alto das arvores.','Campo militar','10h30min','Campo militar para controle da superpolução de dinossauros','Pesadelo na cozinha','11:30','Pausa para o almoço no restaurante pé de fogo, que se encontra aos pés de um vulcão inativo','Alpinismo sem corda','13h','Subida ao topo do vulcão, no lugar da corda nós daremos as mãos','Curso rapido','15h','Os indigenas que habitam o topo do vulcão darão um curso rapido e totalmente gratuito de voou de asa delta', 'Hora de voar','16h30min','Voaremos até o Rio dos Répteis para fazer uma aterrissagem segura na água','Cada um no seu crocodilo','16h50min','Monte no seu réptil antes que ele monte em você, seguiremos o fluxo da água até as margens do Rio Branco. ','Descanso as margens do rio', '17h40min', 'Nadaremos até as margens do Rio Branco,cuide com os carandirus na água;descansaremos enquanto alguns receberão auxilio médico de uma xamã espiritual','Chegado ao Acre!', '18h30min', 'Após esgueirarmos mata a dentro chegaremos á terra perdida conhecida como Acre, aqui nós nos despedimos(nossa empresa não se responsabiliza pela volta dos  turistas).']

a=0
b=1
c=2

print ('#'*50)
print(f'\n{titulo}\n{partida} - {destino} ')
print ('#'*50)

for i in range(0,10):
    print(f"Nome:{lista_parada[a]} - Horario:{lista_parada[b]} - {lista_parada[c]} \n")
    a += 3
    b += 3
    c += 3
