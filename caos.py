quantidade = int(input("quantidade de animais: "))
i = 0
idadeMaior = 0
nomeMaior = ""
while(i<quantidade):
    nome_1 = input("nome: ")
    idade_1 = int(input("idade: "))
    if idade_1 > idadeMaior:
        idadeMaior = idade_1
        nomeMaior = nome_1
    i = i+1
print(nomeMaior)
