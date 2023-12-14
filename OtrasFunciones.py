"""1. Expresiones lambda se pueden usar para la construcción de funciones de una sola línea tipo polinomio."""

from math import *
from random import randint
from ValidacionDatos import *

pot = lambda x,y : pow(x, y)                # Me permiten reemplazar las funciones de una sola linea.
resultado1 = pot(10, 3)
print("resultado = ",resultado1)


""""2. Función recurrente."""

def adivinarNumero(intento):
    numero = randint(1, 6)              # Simulamos el lanzamiento de un dado.
    numeroUsuario = ValidarEntero("Ingrese un número entre 1 y 6: ")

    if numeroUsuario == numero:
        print("Felicitaciones, acertaste: ",numero)
    else:
        print("Fallaste, intenta de nuevo.")
        intento += 1
        adivinarNumero(intento)

adivinarNumero(1)


"""3. Generar una secuencia de cubos."""
def generarCubos():
    limiteSuperior = ValidarEntero("Ingrese el límite superior: ")          # Número hasta el cual se generarán los cubos.

    for i in range (1, limiteSuperior + 1):             # Creamos un ciclo entre 0 y el límite superior.
        print(pow(i, 3), end=" , ")                 # Imprimimos el cubo de cada número natural.

generarCubos()





