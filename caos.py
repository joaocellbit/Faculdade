quantidade = int(input("quantidade de animais: "))
i = 0
idadeMaior = 0
nomeMaior = ""
while(i<quantidade):
    print('Nome do animal', i+1, ':')
    nome_1 = input()
    print("idade do animal ", i+1, ":")
    idade_1 = int(input())
    if idade_1 > idadeMaior:
        idadeMaior = idade_1
        nomeMaior = nome_1
    i = i+1
print(nomeMaior, "eh o mais velho")
