#--- Exercício 5  - Variáveis
#--- Imprima os dados de 5 papéis cotados na bolsa de valores de SP
#--- Cada Papel apresentado deve possuir: 
#---    Nome 
#---    Tipo
#---    Cotação Atual
#---    Valor Mínimo do dia 
#---    Valor Máximo do dia 
#--- Os dados dos papéis devem estar em variáveis
#--- A tela deve conter cabeçalho e rodapé
#--- Deve ser usado os caracteres de tabulação e quebra de linha

papeis = []

for i in range(0,5):
    papel = {'nome': '', 'tipo': '', 'contacaoAnual': '', 'valorMinimo': '', 'valorMax': ''}
    papel['nome'] = str(f'Acao {i + 1}')
    papel['tipo'] = 'Ativo'
    papel['contacaoAnual'] = 6 * i
    papel['valorMinimo'] = 2 * i
    papel['valorMax'] = 4 * i
    papeis.append(papel)

print('=' * 50)

for papel in papeis:
    print(f"\tNome: {papel['nome']}\n\tTipo: {papel['tipo']}\n\tCotação Atual: {papel['contacaoAnual']}\n\tValor Mínimo do dia: {papel['valorMinimo']}\n\tValor Máximo do dia: {papel['valorMax']}\n")

print('=' * 50)