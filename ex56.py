somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ""
totalmulher = 0

for p in range(1,5):
    print("==== nome da {} ===".format(p))
    nome = str(input("Diga nome :")).strip()
    idade = int(input("Diga a idade :"))
    sexo = str(input(" Sexo [M/F] :")).strip()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome

    if sexo in "Mm" and idade > maioridadehomem:
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totalmulher += 1

mediaidade = somaidade / 4
print("A media das idades e de {} anos".format(mediaidade))
print("o homem mais velho tem {} anos e se chama {}".format(maioridadehomem, nomevelho))
print("São tantas {} mulheres com menos de 20 anos".format(totalmulher))