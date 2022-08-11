print("escolha oq vc quer calcular: 1 = area, 2 = gasolina, 3 =media, 4 = perimetro, 5 = tempo")
from ast import Str
from area import areas
from gasolina import gasolinas
from media import medias
from perimetro import perimetros
from tempo import tempos
escolha = input("")
if escolha == Str:
    print("NUMERO CARAI")
elif escolha == "2":
    gasolinas()
elif escolha  == "3":
    medias()
elif escolha == "4":
    perimetros()
elif escolha == "5":
    tempos()
elif escolha == "1":
    areas()
else:
    print("coloque um dos valores")
    
