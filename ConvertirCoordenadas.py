"""Modulo para convertir coordenadas cartesianas en polares y viceversa"""

from math import *
from numpy import arctan

def polar(coordenadaX, coordenadaY):

    polarR = sqrt(pow(coordenadaX, 2) + pow(coordenadaY, 2))
    polarT = arctan(coordenadaY / coordenadaX)

    return (polarR, polarT)

def cartesiana(polarR, polarT):

    coordenadaX = polarR * cos(polarT * 180 / pi)
    coordenadaY = polarR * sin(polarT * 180 / pi)

    return(coordenadaX, coordenadaY)

