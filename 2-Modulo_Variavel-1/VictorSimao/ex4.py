#--- Exercício 4  - Variáveis
#--- Imprima a tela de um itinerário de viagem
#--- O itinerário deve conter o ponto de partida e de destino
#--- O ponto de partida e de destino devem estar armazenados em variáveis
#--- Entre os dois pontos deve conter no mínimo 10 pontos de parada
#--- Cada item ponto de parada deve conter data, hora e descrição
#--- Cada ponto de parada, data, hora e descrição será uma variável.
#--- O itinerário deve conter cabeçalho com o título da viagem, que será uma variável
#--- Deve ser usado os caracteres de tabulação e quebra de linha

origem= 'Blumenau - SC'
destino= 'Hotel Boa Vista'

parada0 = {'Descrição':'Saida de casa', 'Data':'26/11/2019', 'Hora':'06:00'}
parada1 = {'Descrição':'Posto Gasolina - Cafe da manhã', 'Data':'26/11/2019', 'Hora':'08:30'}
parada2 = {'Descrição':'Almoço Churrascaria Porcão', 'Data':'26/11/2019', 'Hora':'12:30'}
parada3 = {'Descrição':'Mirante Serra Mantiqueira', 'Data':'26/11/2019', 'Hora':'14:30'}
parada4 = {'Descrição':'Chegada Hotel', 'Data':'26/11/2019', 'Hora':'16:00'}


print(f'Origem: {origem}\n')

print(f'{parada0}\n')
print(f'{parada1}\n')
print(f'{parada2}\n')
print(f'{parada3}\n')
print(f'{parada4}\n')

print(f'Destino: {destino}\n')