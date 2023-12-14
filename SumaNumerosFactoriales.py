"""Programa para calcular la suma de los primeros K números factoriales"""

# 1. Generar un número aleatorio entre 1 y 10.
# 2. Llamar la función para que calcule el factorial de todos los números entre 1 y el número generado.
# 3. Realizar la sumatoria de todos los factoriales.
# 4. Mostrar en pantalla la suma.

from random import randint

def factorialNumero(numero):

    fact = 1                            # Almacenar el factorial de cada número.
    contador = 1                        # Control del ciclo.

    while contador <= numero:
        fact *= contador
        contador += 1

    return fact

numeroGenerado = randint(1, 10)        # Generamos un número aleatoriemente.

sumaFactoriales = 0                          # Acumular la suma de los factoriales.

contador1 = 1
while contador1 <= numeroGenerado:           # Llamar la función con cada uno de los números enteros, hasta llegar la valor Generado.
    sumaFactoriales += factorialNumero(contador1)
    contador1 += 1

print(" El número generado es: ", numeroGenerado,"\n",
      "La suma de los factoriales es: ",sumaFactoriales)