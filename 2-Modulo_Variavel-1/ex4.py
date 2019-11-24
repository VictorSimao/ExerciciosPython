#--- Exercício 4  - Variáveis
#--- Imprima a tela de um itinerário de viagem
#--- O itinerário deve conter o ponto de partida e de destino
#--- O ponto de partida e de destino devem estar armazenados em variáveis
#--- Entre os dois pontos deve conter no mínimo 10 pontos de parada
#--- Cada item ponto de parada deve conter data, hora e descrição
#--- Cada ponto de parada, data, hora e descrição será uma variável.
#--- O itinerário deve conter cabeçalho com o título da viagem, que será uma variável
#--- Deve ser usado os caracteres de tabulação e quebra de linha

viagem = 'INDAIAL/BLUMENAU'
pp = '| 16-11-2019 | 12:00 | Terminal Rodiviário de Indaial'
pd = '| 16-11-2019 | 12:55 | Terminal da Proeb'
p1 = '| 16-11-2019 | 12:05 | a'
p2 = '| 16-11-2019 | 12:10 | b'
p3 = '| 16-11-2019 | 12:15 | c'
p4 = '| 16-11-2019 | 12:20 | d'
p5 = '| 16-11-2019 | 12:25 | e'
p6 = '| 16-11-2019 | 12:30 | f'
p7 = '| 16-11-2019 | 12:35 | g'
p8 = '| 16-11-2019 | 12:40 | h'
p9 = '| 16-11-2019 | 12:45 | i'
p10 = '| 16-11-2019 | 12:50 | j'

print('-'*30 , viagem , '-'*30 , '\n\n\n')
print('\tSaída: {}\n\tPonto 1: {}\n\tPonto 2: {}\n\tPonto 3: {}\n\tPonto 4: {}\n\tPonto 5: {}\n\tPonto 6: {}\n\tPonto 7: {}\n\tPonto 8: {}\n\tPonto 9: {}\n\tPonto 10: {}\n\tChegada: {}'.format(pp,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,pd))
print('-'*80)