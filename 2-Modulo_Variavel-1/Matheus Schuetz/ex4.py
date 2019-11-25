#--- Exercício 4  - Variáveis
#--- Imprima a tela de um itinerário de viagem
#--- O itinerário deve conter o ponto de partida e de destino
#--- O ponto de partida e de destino devem estar armazenados em variáveis
#--- Entre os dois pontos deve conter no mínimo 10 pontos de parada
#--- Cada item ponto de parada deve conter data, hora e descrição
#--- Cada ponto de parada, data, hora e descrição será uma variável.
#--- O itinerário deve conter cabeçalho com o título da viagem, que será uma variável
#--- Deve ser usado os caracteres de tabulação e quebra de linha
linhas = '='*50
partida = 'Minha casa'
destino = 'Tarumâ Office'
parada1 = '25/11/2019 7:00\nPonto de ônibus: Chegada ao ponto de ônibus geralmente vazio'
parada2 = '25/11/2019 7:05\nIgreja: Chegada na igreja católica, apenas passagem'
parada3 = '25/11/2019 7:10\nlojinha de 1,99: Chegada a lojinha do 1,99 que me roubou 10 Reais'
parada4 = '25/11/2019 7:15\nCemitério: Passando pelo cemitério de lembranças'
parada5 = '25/11/2019 7:17\nEscola Adolpho Konder: Passagem pela escola que estudo durante a noite'
parada6 = '25/11/2019 7:20\nTerminal: Chegando no terminal para prosseguir a viagem'
parada7 = '25/11/2019 7:22\nFila: Ficando alguns minutos preso em uma enorme fila'
parada8 = '25/11/2019 7:30\nSemaforo: Passando pelo semafaro que da fim a fila'
parada9 = '25/11/2019 7:35\nSaida do Onibus: O restante da viagem sera a pé'
parada10 = '25/11/2019 7:40\nChegada ao Tarumã: Chegamos em nosso destino'

print(f'{linhas}\nPartida:{partida}\tDestino:{destino}\n{parada1}\n{parada2}\n{parada3}\n{parada4}\n{parada5}\n{parada6}\n{parada7}\n{parada8}\n{parada9}\n{parada10}\n{linhas}')
