def equacao():
    import math
    from main import main
    print("coloque os valores da equacao")
    A = int(input("A:"))
    B = int(input("B:"))
    C = int(input("C:"))
    delta = B**2 - 4*A*C
    calculo_positivo = (-B+(delta)**0.5)/(2*A)
    calculo_negativo = (-B-(delta)**0.5)/(2*A)
    print("Raiz 1:", calculo_positivo, "Raiz 2:", calculo_negativo)
    main()