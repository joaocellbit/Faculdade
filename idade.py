#informacao da idade
idade = int(input("idade: "))
#logica das idades
if idade <= 10:
    print("crianca")
elif 18 > idade > 10:
    print("adolecente")
else:
    print("adulto")
