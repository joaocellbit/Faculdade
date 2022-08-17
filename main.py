
def main():
    print("escolha oq vc quer calcular: 1 = area, 2 = gasolina, 3 =media, 4 = perimetro, 5 = tempo, 6 = equacao")
    from ast import Str
    from area import areas
    from gasolina import gasolinas
    from media import medias
    from perimetro import perimetros
    from tempo import tempos
    from equacao import equacao
    while(True):
        escolha = input("")
        if escolha == "1":
            areas()
            break 
        elif escolha == "2":
            gasolinas()
            break
        elif escolha  == "3":
            medias()
            break
        elif escolha == "4":
            perimetros()
            break
        elif escolha == "5":
            tempos()
            break
        elif escolha == "6":
            equacao()
            break
        elif escolha == ("but you didnt have to cut me off"):
         print("But you didn't have to cut me off Make out like it never happened and that we were nothing And I don't even need your love But you treat me like a stranger and that feels so rough")
        else:
            print("coloque um dos valores")
main()