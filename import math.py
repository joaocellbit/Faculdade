from email.mime import base
import math


n = int(input("numero de figuras:"))
for i in range(n):
    print("qual tipo de figura: 1 = triangulo, 2= retangulo, 3 = circulo")
    tipo = int(input())
    def triangulo(x,y):
        return x*y/2
    def retangulo(x,y):
        return x*y
    def circulo(r):
        return math.pi*r
    if tipo == 3:
        raio = float(input("raio:"))
        area = circulo(raio)
        print(area)
    elif tipo == 2:
        ladoA = float(input("lado A"))
        ladoB = float(input("lado B"))
        area = retangulo(ladoA,ladoB)
        print(area)
    else:
        ladoA = float(input("altura"))
        ladoB = float(input("base"))
        area = triangulo(ladoA,ladoB)
        print(area)