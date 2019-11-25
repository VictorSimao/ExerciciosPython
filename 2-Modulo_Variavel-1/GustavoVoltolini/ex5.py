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

lista_papel = ['ABV3', 'NM OM', 18.19, 15.10, 20.63, 'ITAU0','NM OM',19, 15,20, 'SUB1','NM OM', 8, 10 , 12 , 'BKG8','NM OM',12,9,12, 'TIND2','NM OM',6,8,10]

a = 0
b = 1
c = 2
d = 3
e = 4

print('#'*50)  # cabeçalho
for i in range (0,5):
    print(f'Nome:{lista_papel[a]} - Tipo: {lista_papel[b]} - Cotação atual:{lista_papel[c]}\nValo min:{lista_papel[d]}\nValor max:{lista_papel[e]}')
    a += 5
    b += 5
    c += 5
    d += 5
    e += 5
print('#'*50)
