"""Programa para contar el número de veces que debe ser lanzado un dado hasta que salga el número ingresado desde
el teclado."""

# 1. Pedir al usuario que ingrese un número desde el teclado.
# 2. Validar que sea un número entero entre 1 y 6.
# 3. LLamar una función que simule el lanzamiento del dado (número ingresado por el usuario).
# 4. Contar el número de lanzamientos hasta que salga el número.
# 5. Mostrar el número de lanzamientos en pantalla.

from ValidacionDatos import ValidarEntero
from random import randint

def lanzarDado(numeroIngresado):
    numeroLanzamientos = 0                              # variable para contar el número de lanzamientos del dado.

    while True:                                         # Me permite realizar varios lanzamientos hasta lograr el número.
        valorDado = randint(1, 6)

        if valorDado != numeroIngresado:                # Si el número es diferente del ingresado por el usuario se lanza de nuevo.
            numeroLanzamientos += 1
        else:
            numeroLanzamientos += 1                     # Muestra en pantalla el número de lanzamientos.
            print("El número ",numeroIngresado, "se obtuvo en el lanzamiento # ",numeroLanzamientos)
            break


while True:
    numeroIngresado = ValidarEntero("Ingrese un número entre 1 y 6: ")      # Validar que se ingresa un número entero.

    if (numeroIngresado < 1 or numeroIngresado > 6):                        # Validar que sea un número correcto.
        print("Error, ingrese un número entre 1 y 6.")
        # continue                                                          Se pide ingresar un nuevo número.
    else:
        break

lanzarDado(numeroIngresado)