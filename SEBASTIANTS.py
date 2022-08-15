usuario="SEBASTIAN"
codigo=264998
C=0
I=3

while C < 3:
    A = input("Ingrese su usuario: ")
    B = int(input("Ingrese su código: "))
    if A == usuario:
        if B == codigo:
            print("Ingreso correctamente")
            break
        else:
            I-=1
            print("Intentelo de nuevo. Le queda(n)",I,"intento(s)")
            C+=1
    else:
        I-=1
        print("Intentelo de nuevo. Le queda(n)",I,"intento(s)")
        C+=1
if C == 3:
    print("Tarjeta retenida")
