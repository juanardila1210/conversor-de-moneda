menu= """
Bienvenido al conversor de monedas hecho por mi

Para mi es un placer tenerte en mi primera aplicacion de Python
proximamente tambien tendremos aplicaciones en C+

Este statement lo esta haciendo Juan Ardila, que es el creador principal de este codigo 

1-Pesos Colombianos
2-Pesos Argentinos 
3-Pesos Mexicanos
4-Euro
5-Moneda Japonesa

Elige una opcion:
"""
def operacion(x):
    dinero=round(monto/x,2)
    print("Tu dinero en dolares es",dinero,"US")   
opcion=int(input(menu))   
monto=float(input("Escribe tu cantidad de dinero:"))
if opcion ==1:
    operacion(3800)
elif opcion ==2:
    operacion(65)
elif opcion ==3:
    operacion(24)
elif opcion==4:
    operacion(0.83)
elif opcion==5:
    operacion(108)
else:
    print("Ingrese una opcion de moneda correcta")
