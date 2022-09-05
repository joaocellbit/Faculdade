import math


n = int(input("numero de figuras:"))
import math
for i in range(n):
    print("qual tipo de figura: 1 = triangulo, 2= retangulo, 3 = circulo")
    tipo = int(input)
    def triangulo(x,y):
        return x*y/2
    def retangulo(x,y):
        return x*y
    def circulo(r):
        return math.pi*r
