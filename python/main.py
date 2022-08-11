
def main():
    print("escolha oq vc quer calcular: 1 = area, 2 = gasolina, 3 =media, 4 = perimetro, 5 = tempo")
    from ast import Str
    from area import areas
    from gasolina import gasolinas
    from media import medias
    from perimetro import perimetros
    from tempo import tempos
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
        else:
            print("coloque um dos valores")
main()            
            
            
        
        
