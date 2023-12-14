"""Menú para calcular los diferentes componentes de la fórmula de un sucesión"""

# suma de los términos.
# cantidad de términos.
# 1er término de la sucesión.
# último término de la sucesión.

from ValidacionDatos import ValidarEntero

while True:
    print("1. Calcular la suma de los términos.")           # Imprimir en pantalla el menú de opciones.
    print("2. Obtener la cantidad de términos.")
    print("3. Obtener el primer término.")
    print("4. Obtener el último término")
    print("5. Salir.")

    opcion = ValidarEntero("Seleccione una opción: ")       # Pedir al usuario que seleccione una opción.

    if opcion == 1:
        cantidadTerminos = ValidarEntero("\nCantidad de términos: ")    # Pedir cada una de las variables necesarias.
        primerTermino = ValidarEntero("1er término: ")
        ultimoTermino = ValidarEntero("Último término: ")

        suma = (cantidadTerminos / 2) * (primerTermino + ultimoTermino) # Calcular la variable que desea conocer el usuario.

        print("\nSuma = ",suma)                             # Imprimir en pantalla el valor de la variable.

    elif opcion == 2:
        suma = ValidarEntero("\nSuma: ")
        primerTermino = ValidarEntero("1er término: ")
        ultimoTermino = ValidarEntero("Último término: ")

        cantidadTerminos = (2 * suma) / (primerTermino + ultimoTermino)

        print("\nCantidad de términos: ",cantidadTerminos)

    elif opcion == 3:
        suma = ValidarEntero("\nSuma: ")
        cantidadTerminos = ValidarEntero("Cantidad de términos: ")
        ultimoTermino = ValidarEntero("Último término: ")

        primerTermino = (2 * suma / cantidadTerminos) - ultimoTermino

        print("\n1er término: ",primerTermino)

    elif opcion == 4:
        suma = ValidarEntero("\nSuma: ")
        cantidadTerminos = ValidarEntero("Cantidad de términos: ")
        primerTermino = ValidarEntero("1er término: ")

        ultimoTermino = (2 * suma / cantidadTerminos) - primerTermino

        print("\nÚltimo término: ",ultimoTermino)

    elif opcion == 5:                                       # Opción para salir del sistema.
        break

    else:                                                   # garantizar que se siga ejecutando el programa cuando se ingresa una opción numerica incorrecta.
        continue

