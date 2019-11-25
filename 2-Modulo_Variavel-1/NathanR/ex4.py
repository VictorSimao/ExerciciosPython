#--- Exercício 4  - Variáveis
#--- Imprima a tela de um itinerário de viagem
#--- O itinerário deve conter o ponto de partida e de destino
#--- O ponto de partida e de destino devem estar armazenados em variáveis
#--- Entre os dois pontos deve conter no mínimo 10 pontos de parada
#--- Cada item ponto de parada deve conter data, hora e descrição
#--- Cada ponto de parada, data, hora e descrição será uma variável.
#--- O itinerário deve conter cabeçalho com o título da viagem, que será uma variável
#--- Deve ser usado os caracteres de tabulação e quebra de linha

print('=='*50, '\n'*2)
print('EXCURSÃO PARA SÃO PAULO 18/11/2019')


ponto_partida = 'Blumenau'
destino = 'São Paulo'
data = '18/11/2019'
h1 = '09:00'
h2 = '10;00'
h3 = '11:00'
h4 = '12:00'
h5 = '13:00'
h6 = '14:00'
h7 = '15:00'
h8 = '16:00'
h9 = '17:00'
h10 = '18:00'
desc1 = 'Museus, shows, exposições, esportes, fonte de água, lago, construções de Niemeyer.'
desc2 = 'Monumento às Bandeiras, Obelisco, assembleia local.'
desc3 = 'Área onde imigrantes japoneses se estabeleceram no início do século XX.'
desc4 = 'Uma das cinco maiores catedrais neogóticas/marco zero.'
desc5 = 'Templo histórico que acomodou o Papa Bento XVI em 2007'
desc6 = 'Um dos edifícios mais altos de São Paulo que tem um magnífico mirante 360º no topo.'
desc7 = 'Teatro Municipal, Galeria de Rock, Igreja de Nossa Senhora do Rosário dos Homens Pretos.'
desc8 = 'Estação da Luz, Parque da Luz e museu de arte do estado.'
desc9 = 'Uma infinidade de frutas, nozes, vinhos, queijos, cervejas, comida, etc.'
desc10 = 'A área comercial mais popular do Brasil.'

print(f'Ponto de partida: {ponto_partida}')
print(f'Destino: {destino}','\n')
print('Pontos de parada: ')
print(f'1- Parque Ibirapuera: Data: {data} Hora: {h1} Descrição: {desc1}')
print(f'2- Monumento às Bandeiras, Praça Armando de Salles Oliveira Vila Mariana: Data: {data} Hora: {h2} Descrição: {desc2}')
print(f'3- Feira da Liberdade, Praça da Liberdade Liberdade: Data: {data} Hora: {h3} Descrição: {desc3}')
print(f'4- Catedral da Sé de São Paulo: Data: {data} Hora: {h4} Descrição: {desc4}')
print(f'5- Mosteiro De São Bento, Largo De São Bento: Data: {data} Hora: {h5} Descrição: {desc5}')
print(f'6- Farol Santander: Data: {data} Hora: {h6} Descrição: {desc6}')
print(f'7- Theatro Municipal De São Paulo: Data: {data} Hora: {h7} Descrição: {desc7}')
print(f'8- Estação da Luz, Praça da Luz: Data: {data} Hora: {h8} Descrição: {desc8}')
print(f'9- Mercado Municipal de São Paulo: Data: {data} Hora: {h9} Descrição: {desc9}')
print(f'10- Shopping 25 de Março, Rua 25 de Março: Data: {data} Hora: {h10} Descrição: {desc10}')

print('\n'*2,'=='*50)