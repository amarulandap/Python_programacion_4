"""Programa para hallar los números primos en un rango determinado"""

# Pedir el límite inferior.
# Pedir el límite superior.
# Crear un ciclo para validar que números dentro del rango son primos.
# Llamar la función para encontrar los números primos.

from ValidacionDatos import ValidarEntero

# Crear la función que valide si el número es primo o no.
def validarPrimo(numero):

    contadorDivisores = 0                  # Contar el total de divisores del número.
    for i in range(2, numero):             # Encontrar los divisores del número.
        if numero % i == 0:
            contadorDivisores += 1

    if contadorDivisores > 0:              # valido si hay un número diferente a la unidad y al número ingresado que lo divida.
        return False
    else:
        return True

limiteInferior = ValidarEntero("Ingrese el límite inferior: ")
limiteSuperior = ValidarEntero("Ingrese el límite superior: ")

for i in range(limiteInferior, limiteSuperior + 1):     # Probar cada uno de los números dentro del rango indicado.
    if validarPrimo(i):                                 # Llamo la función para validar cada número.
        print(i, end = " , ")


