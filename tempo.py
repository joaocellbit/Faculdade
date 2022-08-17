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



