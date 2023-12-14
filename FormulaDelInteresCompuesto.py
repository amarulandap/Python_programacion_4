"""Programa para trabanar con la formula del interés compuesto"""

# Valor acumulado.
# Valor de cada depósito mensual.
# cantidad de depositos mensuales.
# tasa de interés mensual.

# pedir al usuario que seleccione una opción.
# pedir que ingrese las variables conocidas y necesarias en cada caso.
# calcular la contidad solicitada.
# mostrar en pantalla el resultado.

from math import *
from ValidacionDatos import *

while True:
    mensaje = "Seleccione una opción: "
    print(mensaje)
    print("\t1. Calcular valor acumulado.")
    print("\t2. Calcular el valor del deposito mensual.")
    print("\t3. Calcular la cantidad de depositos mensuales.")
    print("\t4. Salir.")

    opcion = ValidarEntero(mensaje)                         # Almacenar la opción seleccionada.

    if opcion == 1:                                         # Calcular el valor acumulado
        depositoMensual = ValidarEntero("Depósito mensual = $ ")
        cantidadDepositos = ValidarEntero("Cantidad de depósitos = ")
        tasaInteres = ValidarReal("Tasa de intéres mensual = ")

        tasaInteres *= (0.01 / 12)

        valorAcumulado = depositoMensual * ((pow((1 + tasaInteres), cantidadDepositos) - 1) / tasaInteres)

        print("Valor acumulado = $",format(valorAcumulado, ".3f"))

    elif opcion == 2:                                       # Calcular el depósito mensual.
        valorAcumulado = ValidarEntero("Valor acumulado = $ ")
        cantidadDepositos = ValidarEntero("Cantidad de depósitos = ")
        tasaInteres = ValidarReal("Tasa de intéres mensual = ")

        tasaInteres *= (0.01 / 12)

        depositoMensual = (tasaInteres * valorAcumulado) * (pow((1 + tasaInteres), cantidadDepositos) - 1)

        print("Depósito mensual = $",format(depositoMensual, ".3f"))

    elif opcion == 3:                                       # Calcular la cantidad de depósitos.
        valorAcumulado = ValidarEntero("Valor acumulado = $ ")
        depositoMensual = ValidarEntero("Depósito mensual = $ ")
        tasaInteres = ValidarReal("Tasa de intéres mensual = ")

        tasaInteres *= (0.01 / 12)

        cantidadDepositos = log10((valorAcumulado * tasaInteres / depositoMensual) + 1) / log10(1 + tasaInteres)
        
        print("Cantidad de depósitos = ",format(cantidadDepositos, ".3f"))
        
    elif opcion == 4:
        break

    else:
        continue