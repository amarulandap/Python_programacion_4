"""Modulo que contiene todas las funciones necesarias para resolver los ejercicios."""

from ValidacionDatos import *

# Función que cuenta la cantidad de divisores enteros que tiene un número entero dado.
def conteoDivisores(numero):                # Recibe el número para hallar sus divisores.

    cuentaDivisores = 0                     # Inicializamos la variable para acumular el número de divisores.
    for i in range (1, numero  + 1):        # Dividimos el número por todos los números naturales entre 1 y el mismo.
        if numero % i == 0:
            cuentaDivisores += 1            # Acumulamos sus divisores.

    return cuentaDivisores                  # Retornamos el número de divisores.


# Función que determina que número entre 1 y 100 tiene mas divisores enteros.
def masDivisores():

    cantidadDivisores = [ ]                 # Lista para almacenar la cantidad de divisores de cada número entre 1 y 100.
    for i in range(1,101):
        divisores = conteoDivisores(i)      # Almacenar la cantidad retornada por la función de conteo.
        cantidadDivisores.append(divisores)

    mayor = cantidadDivisores[0]
    for j in range(1,len(cantidadDivisores)):
        if cantidadDivisores[j] > mayor:
            mayor = cantidadDivisores[j]     # Me indica que cantidad de divisores es la mayor.

    mayoresDivisores = [ ]                   # Almacenamos los números que tienen mayor cantidad de divisores (60, 72, 84, 90, 96).
    for i in range (len(cantidadDivisores)):
        if cantidadDivisores[i] == mayor:
            mayoresDivisores.append(i+1)

    print("Mayor cantidad de divisores es: ",mayor)
    for i in (mayoresDivisores):
        print(i, end=" ")

masDivisores()




