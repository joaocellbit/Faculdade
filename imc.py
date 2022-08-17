from re import I


i = 0
while(i<3):
    nome = input("nome: ")
    peso = float(input("peso em kg: "))
    altura = float(input("altura em m: "))

    imc = peso/altura**2

    print (nome, "tem um imc de: ", imc)
    i = i + 1