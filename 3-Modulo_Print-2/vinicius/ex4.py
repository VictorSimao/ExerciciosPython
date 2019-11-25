#--- Exercício 4  - Print -2
#--- Crie uma variável e atribua uma string com o seu nome
#--- Crie uma variável de nome linkedin e atribua um valor booleano 
#--- Crie uma variável de nome instagran e atribua um valor booleano 
#--- Crie uma variável de nome facebook e atribua um valor booleano 
#--- Crie uma variável de nome telegram e atribua um valor booleano 
#--- Imprima as cinco variáveis juntamente com uma frase dizendo se possui conta nas mídias citadas 
#--- Para impressão utilize f-string

nome = input("Digite seu nome: ")
link = bool(input("Voce tem linkedin? "))
insta = bool(input("Voce tem instagram? "))
face = bool(input("Voce tem facebook? "))
tele = bool(input("Voce tem telegram? "))

if link == "s":
    possui = 'possui linkedin'
    print(f"Ele possui {possui}")
if insta == "s":
    possui = 'possui instagram'
    print(f"Ele possui {possui}")
if face == "s":
    possui = 'possui facebook'
    print(f"Ele possui {possui}")
if tele == "s":
    possui = 'possui telegram'
    print(f"Ele possui {possui}")