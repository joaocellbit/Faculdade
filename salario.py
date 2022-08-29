salario_1 = float(input("salario1..."))
salario_2 = float(input("salario2..."))
salario_3 = float(input("salario3..."))
menor_salario_liquido = 1000000
i=0
salario_final1 = 0
salario_final2 = 0
salario_final3 = 0
if salario_1 >= 500:

    salario_final1 = salario_1*0.85
   
else:
    salario_final1 = salario_1
if salario_2 >= 500:
    salario_final2 = salario_2*0.85
   
else:
    salario_final2 = salario_2
if salario_1 >= 500:
    salario_final3 = salario_3*0.85
  
    
else:
        salario_final3 = salario_3
if salario_final1 < menor_salario_liquido:
        menor_salario_liquido = salario_final1    
if salario_final2 < menor_salario_liquido:
        menor_salario_liquido = salario_final2
if salario_final3 < menor_salario_liquido:
        menor_salario_liquido = salario_final3

print("salario liquido 1:",salario_final1)
print("salario liquido 2:", salario_final2)
print("salario liquido 3:", salario_final3)
print("soma dos 3 salarios:", salario_final1+salario_final2+salario_final3)
print("menor salario:", menor_salario_liquido)