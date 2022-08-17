#leitura dos dados inseridos pelo usuario

numero_1 = int(input("numero 1"))
numero_2 = int(input("numero 2"))

#determinacao do maior numero

if numero_1 > numero_2:
    print(numero_1, "eh o maior numero")
elif numero_2 > numero_1:
    print(numero_2, "eh o maior numero")
else:
    print("eles sao iguais")