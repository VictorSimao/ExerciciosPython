#--- Exercício 4  - Variáveis
#--- Imprima a tela de um itinerário de viagem
#--- O itinerário deve conter o ponto de partida e de destino
#--- O ponto de partida e de destino devem estar armazenados em variáveis
#--- Entre os dois pontos deve conter no mínimo 10 pontos de parada
#--- Cada item ponto de parada deve conter data, hora e descrição
#--- Cada ponto de parada, data, hora e descrição será uma variável.
#--- O itinerário deve conter cabeçalho com o título da viagem, que será uma variável
#--- Deve ser usado os caracteres de tabulação e quebra de linha

titulo=('Viagem até Vancouver')
print('='*20,titulo,'='*20)

p=('Local de partida: Blumenau/SC/Brasil')
p1=('1ª Parada: Aeroporto de navegantes - Horario de chegada maxima até 9:00')
p2=('2ª Parada: Voo de Aeroporto de navegantes para Aeroporto Internacional de Sao Paulo - Embarque 10:00')
p3=('3ª Parada: Aeroporto Internacional de Sao Paulo - Chegada prevista 12:00')
p4=('4ª Parada: Voo de Aeroporto Internacional de Sao Paulo para Aeroporto Intercontinental George Bush - Embarque 16:00')
p5=('5ª Parada: Aeroporto Intercontinental George Bush - Chegada prevista 02:00')
p6=('6ª Parada: Voo de Aeroporto Intercontinental George Bush para Aeroporto internacional de Vancouver  - Embarque 08:00')
p7=('7ª Parada: Aeroporto internacional de Vancouver - Chegada prevista 13:00')
p8=('8ª Parada: Onibus até Ponte Suspensa de Capilano - Chegada prevista 14:00 - Horario de saida 16:30')
p9=('9ª Parada: Onibus até Stanley Park - Chegada prevista 17:00 - Horario de saida 19:00')
p10=('10ª Parada: Onibus até Blue Horizon Hotel - Chegada prevista 20:00 ')
d=('Local de destino: Vancouver/Colúmbia Britanica/Canadá')

print(f'{p}\n{p1}\n{p2}\n{p3}\n{p4}\n{p5}\n{p6}\n{p7}\n{p8}\n{p9}\n{p10}\n{d}')
