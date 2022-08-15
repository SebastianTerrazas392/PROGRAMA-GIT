#Variables:
H_Trabajadas = 500
codigo = "72756105"
#Código
Nom = input("Inserte su nombre: ")
print("Bienvenido", Nom, "al portal de consultas")
ID_profesor = input("Ingrese el número de código: ")
if ID_profesor == codigo:
    print("Horas trabajadas:", H_Trabajadas)
    sueldo = H_Trabajadas * 20
    AFP=(sueldo * 10)/100
    Quinta=(sueldo * 8)/100
    Sa = input("Ingrese el seguro de salud: ")
    if Sa == "ESSALUD":
        Sa_D=(sueldo * 11)/100
    elif Sa == "EPS":
        Sa_D=(sueldo * 15)/100
    else: 
        print("Ingreso un valor incorrecto")
        breakpoint
    sueldo_b= sueldo - AFP - Quinta - Sa_D
    print(
        """
    +--------------------------------------+
    | Boleta Idat                          |
    +--------------------------------------+
    | Ingresos: """, sueldo,"""
    | Descueto del AFP:""",AFP,"""
    | Descuento de su seguro de salud:""",Sa_D,"""
    | Renta de quinta:""",Quinta,"""
    | --------------------------------------
    | Sueldo neto:""",sueldo_b,"""
    +--------------------------------------+
    """)
else: 
    print("Código incorrecto, vuelvalo a intentar")
