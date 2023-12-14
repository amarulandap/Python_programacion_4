"""Programa para calcular el precio de una pizza."""

# Variables de entrada:
# tamaño de la pizza.
# cantidad de ingredientes adicionales.

# Constantes:
# precios de la pizza $25000     $38000      $52000
# precio de cada ingrediente adicional $4500

# Salidas:
# valor a pagar.

from ValidacionDatos import ValidarEntero

def costoAdicionales():                                # Función para calcular el costo de los ingredientes adicionales.

    precioIngredienteAdicional = 4500                  # Precio de cada ingrediente.
    cantidadAdicionales = ValidarEntero("Cantidad de ingredientes adicionales: ")   # Cantidad de adicionales.
    totalAdicionales = precioIngredienteAdicional * cantidadAdicionales             # Calculamos el costo.

    return totalAdicionales


while True:
    print("Menú de opciones.")                                      # Menú de opciones principal.
    print("1. Pizza pequeña.")
    print("2. Pizza mediana.")
    print("3. Pizza grande.")
    print("4. Salir.")

    opcion = ValidarEntero("Seleccione el tamaño de la Pizza: ")    # Almacenamos la opción ingresada por el usuario.

    if opcion == 1:
        costoPizzaPequeña = 25000                                   # Ingresamos el costo de cada tamaño de la pizza.
        adicionales = costoAdicionales()                            # Llamamos la función para calcular el costo de los adicionales.

        valorAPagar = costoPizzaPequeña + adicionales               # Calculamos el costo total


    elif opcion == 2:
        costoPizzamediana = 38000
        adicionales = costoAdicionales()

        valorAPagar = costoPizzamediana + adicionales

    elif opcion == 3:
        costoPizzaGrande = 52000
        adicionales = costoAdicionales()

        valorAPagar = costoPizzaGrande + adicionales

    elif opcion == 4:                                               # Opción para salir del programa.
        break

    else:                                                           # Se garantiza que al ingresar una opción numérica incorrecta se siga ejecutando el programa.
        continue

    print("Valor a pagar: $", valorAPagar)                           # Imprimimos al total a pagar.