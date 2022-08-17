print("animal 1")
nome_1 = input("nome: ")
idade_1 = int(input("idade: "))
print("animal 2")
nome_2 = input("nome: ")
idade_2 = int(input("idade: "))
print("animal 3")
nome_3 = input("nome: ")
idade_3 = int(input("idade: "))

if idade_1>idade_2>idade_3:
    print(nome_1)
elif idade_1>idade_3>idade_2:
    print(nome_1)
elif idade_2>idade_1>idade_3:
    print (nome_2)
elif idade_2>idade_3>idade_1:
    print(nome_2)
elif idade_3>idade_1>idade_2:
    print(nome_3)
elif idade_3>idade_2>idade_1:
    print(nome_3)
else:
    print("tem pelomenos 2 iguais")