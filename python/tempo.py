def tempos():
  print("coloque os dias")
  dias = int(input(""))
  print("coloque as horas")
  horas = int(input(""))
  print("coloque os minutos")
  minutos = int(input(""))
  hora = 24
  minuto = 60
  minutos_calculados = (dias)*(hora)*(minuto)
  print("total de minutos:")
  print(minutos_calculados + horas*60 + minutos)  


