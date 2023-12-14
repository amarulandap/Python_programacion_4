'''Libreria de funciones para calcular áreas y volumenes de algunas figuras geométricas.'''

from math import *

# Área de un cuadrado.
def areaCuadrado(lado):

    return pow(lado, 2)             # Retornamos el área de la figura.

# Área del rectángulo.
def areaRectangulo(base, altura):

    return base * altura

# Área del triángulo.
def areaTriangulo(base, altura):

    return (base * altura) / 2

# Área del paralelogramo.
def areaParalelogramo(base, altura):

    return base * altura

# Área del circulo.
def areaCirculo(radio):

    return pi * pow(radio, 2)

# Área del trapecio.
def areaTrapecio(base1, base2, altura):

    return ((base1 * base2) * altura) / 2

# Volumen del cono.
def volumenCono(radio, altura):

    return pi * altura * pow(radio, 2)          # Retornamos el volumen de la figura.

# Volumen de la pirámide.
def volumenPiramide(areaBase, altura):

    return (areaBase * altura) / 3

# Volumen del cilindro.
def volumenCilindro(radio, altura):

    return pi * pow(radio, 2) * altura

# Volumen de la esfera.
def volumenEsfera(radio):

    return 4 * (pi * pow(radio, 3)) / 3

# Volumen del prisma.
def volumenPrisma(areaBase, altura):

    return areaBase * altura

# Volumen del octoedro.
def volumenOctoedro(lado1, lado2, lado3):

    return lado1 * lado2 * lado3

