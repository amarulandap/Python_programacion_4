from ValidacionDatos import *
from math import pow

""" 1. validar si un número es perfecto"""

# Función para validar si el número es perfecto.
def validarPerfecto(arreglo, numero):

    sumaDivisores = 0                           # Variable para almacenar la suma de los divisores.
    for i in(arreglo):
        sumaDivisores += i

    if numero == (sumaDivisores - numero):
        print("el número ",numero," es un número perfecto.")

# Función para hallar los divisores del número.
def divisores(numero):

    divisoresNumero = [ ]                       # Lista para almacenar los divisores del número.
    for i in range (1, numero + 1):
        if numero % i == 0:                     # Validamos si el valor de i es divisor del número.
            divisoresNumero.append(i)

    validarPerfecto(divisoresNumero, numero)    # Llamamos la función para validar si el número es perfecto.

for i in range(1, 1001):
    divisores(i)


"""2. Función para validar si el cuadrado de un número n es igual a la suma de los primeros n números impares. """

# Función para hallar los n números impares.
def numerosImpares(numero1):                     # Número1 es el número ingresado desde el teclado.

    numerosImpares = [ ]                         # Lista para almacenar los numero1 primeros números impares entre 1 y 100.
    for i in range (1, 101):
        if i % 2 != 0 and len(numerosImpares) < numero1:              # Validamos si el número es impar.
            numerosImpares.append(i)

    return numerosImpares

while True:
    numero1 = ValidarEntero("\nIngrese un número mayor que 1: ")      # Ingresar un número mayor que 1.

    if numero1 < 1:
        continue
    else:
        sumaImpares = 0
        impares = numerosImpares(numero1)         # Hallamos los números impares desde 1 hasta el número ingresado por el usuario.

        for i in (impares):
            sumaImpares += i                                           # Sumamos los números impares hallados.

        if sumaImpares == pow(numero1, 2):                             # Validamos si se cumple la condición de igualdad.
            print(numero1,"^2 = ", pow(numero1, 2))
            print("La suma de los impares es = ",sumaImpares)
            print("Son iguales.")
        else:
            print(numero1,"^2 = ", pow(numero1, 2))
            print("La suma de los impares es = ",sumaImpares)
            print("Son diferentes.")

        break



