from itertools import combinations, product
from pathlib import Path
import random
import os

def parsear(linea):
    return linea.strip().split()

def elimina_elementos_compresion(linea, lista, num_elementos):
    ref = linea

    return [
        elem
        for elem in lista
        if sum(a == b for a, b in zip(ref, elem.split())) < num_elementos
    ]

def elimina_elementos(linea, lista, num_coincidencias):
    ref = linea

    resultado = []

    for elem in lista:

        coincidencias = 0

        for a, b in zip(ref, elem.split()):
            
            if a == b:
                coincidencias += 1

        if coincidencias < num_coincidencias:
            resultado.append(elem)

    return resultado


# ========================================================

#lineas = list(combinations(range(14), 6))

#with open("combinaciones.txt", "w") as f:
#    for c in combinations(range(14), 6):
#        f.write(" ".join(map(str, c)) + "\n")

lineas = [' '.join(c) for c in product('1X2', repeat=14)]

print("lineas de lineas:", len(lineas))

seleccionadas = []
contador = 0
while lineas:
    indice = random.randrange(len(lineas))
    elegida = parsear(lineas[indice])
    seleccionadas.append(" ".join(elegida))
    contador += 1
    print(contador,": " , elegida)

    lineas = elimina_elementos(elegida, lineas, 7)

    #print("lineas de lineas:", len(lineas))


