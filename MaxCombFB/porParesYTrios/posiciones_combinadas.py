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

"""
todas6 = list(combinations(range(14), 6))
print("Elementos de todas6: " , len(todas6))
trios_usados6 = set()
seleccionadas6 = []

for comb6 in todas6:

    trios6 = set(combinations(comb6, 3))

    if trios6.isdisjoint(trios_usados6):
        seleccionadas6.append(comb6)
        trios_usados6.update(trios6)

print(seleccionadas6)
print()
"""

todas7 = list(combinations(range(14), 7))
print("Elementos de todas7: " , len(todas7))
grupo1_usados = set()
seleccionadas7 = []

for comb7 in todas7:

    grupo1 = set(combinations(comb7, 1))

    if grupo1.isdisjoint(grupo1_usados):
        seleccionadas7.append(comb7)
        grupo1_usados.update(grupo1)

print(seleccionadas7)

todas7 = list(combinations(range(14), 7))
grupo2_usados = set()

for item_grupo1 in grupo1_usados:
    if item_grupo1[0] in comb7:
        grupo2 = set(combinations(comb7, 2))
        grupo2_usados.update(grupo2)


for comb7 in todas7:
    grupo2 = set(combinations(comb7, 2))

    if grupo2.isdisjoint(grupo2_usados):
        seleccionadas7.append(comb7)
        grupo2_usados.update(grupo2)
print(seleccionadas7)