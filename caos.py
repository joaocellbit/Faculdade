quantidade = int(input())
i = 0

while(i<quantidade):
    nome_1 = input("nome: ")
    idade_1 = int(input("idade: "))
    if i == 0:
        nomeMaior = nome_1
        idadeMaior = idade_1
    if idade_1 > idadeMaior:
        idadeMaior = idade_1
        nomeMaior = nome_1
    i = i+1
print(nomeMaior)