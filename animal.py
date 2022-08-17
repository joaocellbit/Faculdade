print("animal 1")
nome_1 = input("nome: ")
idade_1 = int(input("idade: "))

MaiorIdade = idade_1
MaiorNome = nome_1

print("animal 2")
nome_2 = input("nome: ")
idade_2 = int(input("idade: "))

if idade_2 > MaiorIdade:
    MaiorIdade = idade_2
    MaiorNome = nome_2

print("animal 3")
nome_3 = input("nome: ")
idade_3 = int(input("idade: "))

if idade_3 > MaiorIdade:
    MaiorIdade = idade_3
    MaiorNome = nome_3
    
print("o", MaiorNome, "eh o mais velho")
