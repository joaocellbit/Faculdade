for i in range(30):
    def media(ap1,ap2,ac):
        media_final = ap1*0.4+ap2*0.4+ac*0.2
        return media_final
    nota_ap1 = float(input("nota ap1:"))
    nota_ap2 = float(input("nota ap2:"))
    nota_ac = float(input("nota ac:"))
    aulas = int(input("numero de aulas:"))
    faltas = int(input("numero de faltas:"))
    def menor_nota():
        menor = nota_ap1
        if nota_ap2 < menor:
            menor = nota_ap2
            return menor
        return menor
    def maior_nota():
        maior = nota_ap1
        if nota_ap2>nota_ap1:
            maior = nota_ap2
            return maior
        return maior
    maior = maior_nota()
    menor_nota1 = menor_nota()
    def AS(x):
        if x < 7:
            nota_as = float(input("nota AS:"))
            return nota_as
        return x

    nota_as = AS(menor_nota1)
    menor = nota_as
    print(maior,menor,nota_ac)
    media_final = media(maior,menor,nota_ac)
    print(media_final)
    def porcentagem_falta():
        porcentagem = (faltas/aulas)*100
        return porcentagem
    porcentagem = porcentagem_falta()
    print("porcentagem de faltas: ",porcentagem,"%")
    if porcentagem>=25 or media_final<7:
        print("reprovado")
    else:
        print("aprovado")
