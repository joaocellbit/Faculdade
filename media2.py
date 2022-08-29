i=0
soma = 0
numeros_50 = 0
while i<30:
    print("numero",i+1,":")
    numero = float(input())
    if numero >50:
        soma += numero
        numeros_50 += 1
    i += 1
print("a media dos numeros maiores q 50:",soma/numeros_50)
