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


# guarda las líneas en un archivo
#with open("combinaciones.txt", "w") as f:
#    for c in combinations(range(14), 6):
#        f.write(" ".join(map(str, c)) + "\n")


todas6 = list(combinations(range(14), 6))

trios_usados6 = set()
seleccionadas6 = []

for comb6 in todas6:

    trios6 = set(combinations(comb6, 3))

    if trios6.isdisjoint(trios_usados6):
        seleccionadas6.append(comb6)
        trios_usados6.update(trios6)

print(seleccionadas6)
print()


todas7 = list(combinations(range(14), 7))

trios_usados7 = set()
seleccionadas7 = []

for comb7 in todas7:

    trios7 = set(combinations(comb7, 4))

    if trios7.isdisjoint(trios_usados7):
        seleccionadas7.append(comb7)
        trios_usados7.update(trios7)

print(seleccionadas7)