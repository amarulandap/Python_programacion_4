"""Modulo para probar las funciones creadas para resolver los ejercicios."""

from ValidacionDatos import *
from CantidadDivisores import *
from ConvertirCoordenadas import *

while True:                             # Hallar el número entre 1 y 100 con mayor cantidad de divisores.

    print("\n","Menú de opciones: ","\n",
          "\t 1. Número entre 1 y 100 con mas divisores enteros.","\n",
          "\t 2. Convertir cartesianas a polares.", "\n"
          "\t 3. Convertir polares a cartesianas.", "\n"
          "\t 4. Salir.")


    opcion = ValidarEntero("Seleccione una opción: ")

    if opcion == 1:
        masDivisores()

    elif opcion == 2:                                            # Convertir cartesianas a polares.
        coordenadaX = ValidarReal("Ingrese la coordenada X: ")  # Ingresar la coordenada x.
        coordenadaY = ValidarReal("Ingrese la coordenada Y: ")  # Ingresar la coordenada y.

        (polarR, polarT) = polar(coordenadaX, coordenadaY)      # Conversión a polares.
        print("r = ",format(polarR, ".3f"),"\n"                                
              "t = ",format(polarT, ".3f"), "radianes")

    elif opcion == 3:                                          # Convertir polares a cartesianas.
        R = ValidarReal("Ingrese la coordenada r: ")            # Ingresar la coordenada r.
        T = ValidarReal("Ingrese la coordenada t: ")            # Ingresar la coordenada t.

        (X, Y) = cartesiana(R, T)                               # Conversión a cartesianas.
        print("x = ",format(X, ".3f"),"\n"
              "y = ",format(Y, ".3f"))

    elif opcion == 4:                                          # Interrumpe la ejecución del ciclo.
        break

    else:
        continue
