menu= """
Bienvenido al conversor de monedas

Para mi es un placer tenerte en mi primera aplicacion de Python
proximamente tambien tendremos aplicaciones en swift

1-Pesos Bogotanos
2-Pesos Argentinos 
3-Pesos Mexicanos

Elige una opcion:
"""
def operacion(x):
    dinero=round(monto/x,2)
    print("Tu dinero en dolares es",dinero,"US")   
opcion=int(input(menu))
if opcion != 1 and opcion !=2 and opcion !=3:
    print("Escribe un valor correcto")     
else:
    monto=float(input("Escribe tu cantidad de dinero:"))
    if opcion ==1:
        operacion(3800)
    elif opcion ==2:
        operacion(65)
    elif opcion ==3:
        operacion(24) 