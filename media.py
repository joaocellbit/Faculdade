
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