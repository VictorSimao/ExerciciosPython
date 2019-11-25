#--- Exercício 4  - Variáveis
#--- Imprima a tela de um itinerário de viagem
#--- O itinerário deve conter o ponto de partida e de destino
#--- O ponto de partida e de destino devem estar armazenados em variáveis
#--- Entre os dois pontos deve conter no mínimo 10 pontos de parada
#--- Cada item ponto de parada deve conter data, hora e descrição
#--- Cada ponto de parada, data, hora e descrição será uma variável.
#--- O itinerário deve conter cabeçalho com o título da viagem, que será uma variável
#--- Deve ser usado os caracteres de tabulação e quebra de linha

partida = "Blumenau - SC"
destino = "Pomerode - SC"
paradas = []

for i in range(0,10):
    parada = {"data": '', "hora": '', "descricao": ''}
    parada["data"] = str(f'{i + 1}/01/1899')
    parada["hora"] = str(f'{i + 2}:15')
    parada["descricao"] = str(f'Parada numero {i + 1}')
    paradas.append(parada)


print('=' * 50)
print(f'Partida: {partida} --> Destino: {destino}')
for parada in paradas:
    print(f'Data: {parada["data"]} - Hora: {parada["hora"]} - Descrição: {parada["descricao"]}\n')

print('=' * 50)