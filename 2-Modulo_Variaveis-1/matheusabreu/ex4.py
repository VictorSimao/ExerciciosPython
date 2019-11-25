#--- Exercício 4  - Variáveis
#--- Imprima a tela de um itinerário de viagem
#--- O itinerário deve conter o ponto de partida e de destino
#--- O ponto de partida e de destino devem estar armazenados em variáveis
#--- Entre os dois pontos deve conter no mínimo 10 pontos de parada
#--- Cada item ponto de parada deve conter data, hora e descrição
#--- Cada ponto de parada, data, hora e descrição será uma variável.
#--- O itinerário deve conter cabeçalho com o título da viagem, que será uma variável
#--- Deve ser usado os caracteres de tabulação e quebra de linha
titulo  = 'RIO - LIMA / LIBERTADORES'
partida = 'Rio de Janeiro'
destino = 'Lima'

parada1 = 'São Paulo'
data1   = '19/11/2019'
hora1   = '19:00'
desc1   = 'Alimentação'

parada2 = 'Campo Grande'
data2   = '20/11/2019'
hora2   = '09:00'
desc2   = 'Descanso, alimentação e abastecimento'

parada3 = 'Cuiabá'
data3   = '20/11/2019'
hora3   = '21:00'
desc3   = 'Descanso e alimentação'

parada4 = 'Porto Velho'
data4   = '21/11/2019'
hora4   = '10:00'
desc4   = 'Descanso, alimentação e abastecimento'

parada5 = 'Rio Branco'
data5   = '21/11/2019'
hora5   = '20:00'
desc5   = 'Descanso e alimentação'

parada6 = 'Puerto Maldonado'
data6   = '22/11/2019'
hora6   = '10:00'
desc6   = 'Descanso, alimentação e abastecimento'

parada7 = 'Cusco'
data7   = '22/11/2019'
hora7   = '19:00'
desc7   = 'Descanso'

parada8 = 'Abancay'
data8   = '23/11/2019'
hora8   = '00:00'
desc8   = 'Abastecimento'

parada9 = 'Nazca'
data9   = '23/11/2019'
hora9   = '09:00'
desc9   = 'Descanso e alimentação'

parada10 = 'Ica'
data10   = '23/11/2019'
hora10   = '13:00'
desc10   = 'Descanso, alimentação e abastecimento'

print('#'*18, titulo, '#'*18, sep=' ')
print(f'\nPartida: {partida} \nDestino: {destino}\n')
print(f'''Parada 1: {parada1}
Data: {data1}
Hora: {hora1}
Descrição: {desc1}

Parada 2: {parada2}
Data: {data2}
Hora: {hora2}
Descrição: {desc2}

Parada 3: {parada3}
Data: {data3}
Hora: {hora3}
Descrição: {desc3}

Parada 4: {parada4}
Data: {data4}
Hora: {hora4}
Descrição: {desc4}

Parada 5: {parada5}
Data: {data5}
Hora: {hora5}
Descrição: {desc5}

Parada 6: {parada6}
Data: {data6}
Hora: {hora6}
Descrição: {desc6}

Parada 7: {parada7}
Data: {data7}
Hora: {hora7}
Descrição: {desc7}

Parada 8: {parada8}
Data: {data8}
Hora: {hora8}
Descrição: {desc8}

Parada 9: {parada9}
Data: {data9}
Hora: {hora9}
Descrição: {desc9}

Parada 10: {parada10}
Data: {data10}
Hora: {hora10}
Descrição: {desc10}
''')
print('\n', '#'*61, sep='')