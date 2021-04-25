menu= """
Bienvenido al conversor de monedas hecho por mi

Para realizar este proyecto, necesité de un colaborador llamado Sebastian Lopez, que es muy inteligente, y de mi hermano Juan Jose

Para mi es un placer tenerte en mi primera aplicacion de Python
proximamente tambien tendremos aplicaciones en C++

Este statement lo esta haciendo Juan Ardila, que es el creador principal de este codigo 

1-Pesos Colombianos :)
2-Pesos Argentinos 
3-Pesos Mexicanos
4-Euro
5-Moneda Japonesa
6-Sol Peruano 
7-Libra esterlina 
8-Rupias

Yo soy sebastián lopez, el segundo al mando de este curso

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
elif opcion==6:
    operacion(4)
elif opcion==7:
    operacion(0.8)
elif opcion==8:
    operacion(75)
else:
    print("Ingrese una opción de moneda correcta")
