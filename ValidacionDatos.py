import sys

def ValidarEntero(mensaje):

    while True:
        try:
            entero = int(input(mensaje))
            return entero
        except ValueError as e:
            print("Valor erroneo, ingrese un número entero")
            # sys.exit()
            continue
        break

def ValidarReal(mensaje):

    while True:
        try:
            real = float(input(mensaje))
            return real
        except ValueError as e:
            print("Error, ingrese un número real")      # File = sys.stderr.
            # sys.exit()
            continue
        break

