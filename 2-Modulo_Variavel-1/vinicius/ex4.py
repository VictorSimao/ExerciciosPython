#--- Exercício 4  - Variáveis
#--- Imprima a tela de um itinerário de viagem
#--- O itinerário deve conter o ponto de partida e de destino
#--- O ponto de partida e de destino devem estar armazenados em variáveis
#--- Entre os dois pontos deve conter no mínimo 10 pontos de parada
#--- Cada item ponto de parada deve conter data, hora e descrição
#--- Cada ponto de parada, data, hora e descrição será uma variável.
#--- O itinerário deve conter cabeçalho com o título da viagem, que será uma variável
#--- Deve ser usado os caracteres de tabulação e quebra de linha

partida = input('\nDigite o ponto de partida: ')
destino = input('Digite o ponto de destino: ')

for i in range(1,3):
    paradas = []
    data = []
    hora = []
    desc = []
    paradas = input(f'Digite o {i}º ponto de parada: ')
    data = input(f'Digite a DATA do {i}º ponto de parada: ')
    hora = input(f'Digite a HORA da {i}ª parada: ')
    desc = input(f'Digite uma DESCRIÇÂO da {i}ª parada: ')

for sss in i:
    print('*'*50)
    print(f'\nPartida: {partida} \nDestino: {destino} \nData: {data[i]} \nHora: {hora[i]} \nDescrição: {desc[i]}')
    print('*'*50)