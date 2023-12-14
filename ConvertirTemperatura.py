"""Programa para convertir grados centigrados a fahrenheit y viceversa"""

# temperatura en centigrados.
# temperatura en fahrenheit.
# opcion seleccionada por el usuario.

# pedir que se elija una opción del menú.
# pedir el valor de la temperatura.
# realizar la conversión de la temperatura.
# mostrar el resultado en pantalla.

from ValidacionDatos import *

while True:
    mensaje = "Elija una opción: "
    print(mensaje)
    print("\t1. Convertir centigrados a fahrenheit.")
    print("\t2. Convertir fahrenheit a centigrados.")
    print("\t3. Salir.")

    opcion = ValidarEntero(mensaje)             # Almacenamos la opción seleccionada por el usuario.

    if opcion == 1:                             # Realizamos la conversión de °C a °F.
        centigrados = ValidarReal("°C = ")
        fahrenheit = (centigrados * 9 / 5) + 32
        print("°F = ", format(fahrenheit, ".3f"))
    elif opcion == 2:                           # Realizamos la conversión de °F a °C.
        fahrenheit = ValidarReal("°F = ")
        centigrados = (fahrenheit - 32) * 5 / 9
        print("°C =", format(centigrados, ".3f"))
    elif opcion == 3:
        break
    else:
        continue



