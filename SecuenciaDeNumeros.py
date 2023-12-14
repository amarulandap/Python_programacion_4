"""1. Crear una función que entregue el n-ésimo término de una secuencia."""

from ValidacionDatos import *

def imprimirArreglo(arreglo):                               # Imprimir la lista.

    for i in(arreglo):
        print(i, end=" ")

def generarSecuencia(numero):

    secuencia = [1, 1, 1]                                    # Lista para almacenar los términos de la secuencia.

    while (len(secuencia) < numero):
        secuencia.append(secuencia[len(secuencia) - 3] + secuencia[len(secuencia) - 2] + secuencia[len(secuencia) - 1])

    imprimirArreglo(secuencia)

numero = ValidarEntero("Ingrese el número para generar la secuencia: ")
generarSecuencia(numero)

