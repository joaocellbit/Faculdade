#informacao da idade
idade = int(input("idade: "))
#logica das idades
if idade <= 10:
    print("crianca")
elif 18 > idade:
    print("adolecente")
else:
    print("adulto")
i = 0
while(i<3):
    nome = input("nome: ")
    peso = float(input("peso em kg: "))
    altura = float(input("altura em m: "))

    imc = peso/altura**2

    print (nome, "tem um imc de: ", imc)
    i = i + 1
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
def areas():
  print("tamanho do lado")
  lado = int(input(""))
  print("tamanho da altura")
  altura = int(input(""))
  area = lado*altura
  print(area)
  from main import main
  main()
def equacao():
    import math
    
    print("coloque os valores da equacao")
    A = int(input("A:"))
    B = int(input("B:"))
    C = int(input("C:"))
    delta = B**2 - 4*A*C
    calculo_positivo = (-B+(delta)**0.5)/(2*A)
    calculo_negativo = (-B-(delta)**0.5)/(2*A)
    print("Raiz 1:", calculo_positivo, "Raiz 2:", calculo_negativo)
    from main import main
    main()
def gasolinas():
  print("quantos litros tem no tanque?")
  tanque = int(input(""))
  print("qual o consumo do carro?")
  consumo = float(input(""))
  print("total de KM:")
  print((tanque)*consumo)
  from main import main
  main()

def medias():
  print("nota ap1:")
  ap1 = float(input(""))
  print("nota ap2:")
  ap2 = float(input(""))
  print("nota ac:")
  ac = float(input(""))
  media_final = ap1*0.4+ap2*0.4+ac*0.2
  print(media_final)
  if media_final >= 7:
    print("aprovado")
  else:
    print("Reprovado")
  from main import main
  main()
  
def perimetros():
  print("coloque o perimetro")
  perimetro = int(input(""))
  print("distancia percorrida")
  distancia = int(input(""))
  print("total de voltas")
  print(distancia/perimetro)
  from main import main
  main()
import imp
from multiprocessing.connection import wait


def tempos():
  print("coloque os dias")
  dias = int(input(""))
  print("coloque as horas")
  horas = int(input(""))
  print("coloque os minutos")
  minutos = int(input(""))
  print("coloque os segundos")
  segundos = int(input(""))
  hora = 24
  minuto = 60
  segundo = 60
  segundos_calculados = segundos
  minutos_calculados = minutos 
  horas_calculadas = horas 
  dia_calculado = dias 
  if segundos_calculados >= 60:
    segundos_finais = segundos_calculados/60
    minutos_calculados = minutos_calculados + int(segundos_finais)
    segundos_calculados = segundos_finais -1
  if minutos_calculados >= 60:
    minutos_finais = minutos_calculados/60
    horas_calculadas = horas_calculadas + int(minutos_finais)
    minutos_calculados = minutos_finais -1
  if horas_calculadas >= 24:
    horas_finais = horas_calculadas/24
    dia_calculado = dia_calculado + int(horas_finais) 
    horas_calculadas = horas_finais -1
  print("tempo total:")
  print(dia_calculado, 'dias,')
  print(horas_calculadas, 'horas')
  print(minutos_calculados, 'minutos')
  print(segundos_calculados, 'segundos')
  from main import main
  main()
