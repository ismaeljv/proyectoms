from itertools import combinations
from collections import Counter
import random

ALEATORIEDAD = 32 # VALOR 0 SIGNIFICA SIEMPRE ALEATORIO, VALOR 1 UNA SÍ Y OTRA NO, VALOR 2 UNA SÍ Y DOS NO, ETC.

def devuelve_linea_aleatoria(aleatoria, fichero="combinaciones.txt"):
    print("Valor de aleatoria:", aleatoria)
    if aleatoria >= ALEATORIEDAD:
        with open(fichero, "r", encoding="utf-8") as f:
            lineas = f.readlines()
            
        return random.choice(lineas).strip()
    
    with open("combinaciones.txt", "r", encoding="utf-8") as f:
        primera_linea = f.readline().strip()
    
    return primera_linea

def cuenta_lineas(fichero="combinaciones.txt"):
    with open(fichero, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)

def elimina_coincidencias(linea_aleatoria, coincidencias,
                           fichero="combinaciones.txt"):

    if isinstance(linea_aleatoria, str):
        numeros = set(map(int, linea_aleatoria.split()))
    else:
        numeros = set(linea_aleatoria)

    lineas_validas = []

    with open(fichero, "r", encoding="utf-8") as f:
        for linea in f:
            combinacion = set(map(int, linea.split()))
            comunes = len(numeros & combinacion)

            if comunes < coincidencias:
                lineas_validas.append(linea)

    with open(fichero, "w", encoding="utf-8") as f:
        f.writelines(lineas_validas)

    return len(lineas_validas)


def analizar_repeticiones(elegidas):
    resultados = {}

    # Analizamos pares, tríos, cuartetos... hasta el tamaño de la combinación
    for tamaño in range(2, 8):
        contador = Counter()

        for linea in elegidas:
            # Convertimos la línea a conjunto/lista de enteros
            if isinstance(linea, str):
                numeros = list(map(int, linea.split()))
            else:
                numeros = list(linea)

            # Generamos las combinaciones de ese tamaño
            for grupo in combinations(numeros, tamaño):
                contador[grupo] += 1

        resultados[tamaño] = contador

    return resultados

def buscar_no_aparecidos(elegidas, tamaño):
    # Todos los grupos posibles de ese tamaño entre 1 y 14
    todos = set(combinations(range(1, 15), tamaño))

    # Grupos que aparecen en las combinaciones elegidas
    aparecidos = set()

    for linea in elegidas:
        if isinstance(linea, str):
            numeros = list(map(int, linea.split()))
        else:
            numeros = list(linea)

        for grupo in combinations(numeros, tamaño):
            aparecidos.add(grupo)

    # Los que nunca han aparecido
    no_aparecidos = todos - aparecidos

    return sorted(no_aparecidos)


combinaciones = combinations(range(1, 15), 7)

# Guardarlas en un fichero de texto
with open("combinaciones.txt", "w", encoding="utf-8") as fichero:
    for combinacion in combinaciones:
        linea = " ".join(map(str, combinacion))
        fichero.write(linea + "\n")

print("Fichero generado: combinaciones.txt")
print("Número de combinaciones generadas:", cuenta_lineas("combinaciones.txt"))

coincidencias = 1
aleatoria = ALEATORIEDAD
elegidas = []
while len(elegidas) < 32:
    coincidencias += 1
    print("Empezamos con coincidencias = ", coincidencias)
    for ele in elegidas:
        restantes = elimina_coincidencias(ele, coincidencias)
        print("Combinaciones restantes con coincidencias anteriores:", restantes)

    while cuenta_lineas("combinaciones.txt") > 0 and len(elegidas) < 32:
        
        linea_al = devuelve_linea_aleatoria(aleatoria)
        if aleatoria >= ALEATORIEDAD:
            aleatoria = 0
        else:
            aleatoria += 1
        print(linea_al)
        elegidas.append(linea_al)
        restantes = elimina_coincidencias(linea_al, coincidencias)

        print("Combinaciones restantes:", restantes)
    # regeneramos el fichero con todas las combinaciones posibles
    combinaciones = combinations(range(1, 15), 7)
    with open("combinaciones.txt", "w", encoding="utf-8") as fichero:
        for combinacion in combinaciones:
            linea = " ".join(map(str, combinacion))
            fichero.write(linea + "\n")

print("Combinaciones elegidas:", elegidas)

print("Analizando repeticiones en las combinaciones elegidas...")
resultados = analizar_repeticiones(elegidas)
print("Resultados del análisis de repeticiones:")
for tamaño, contador in resultados.items():
    print(f"Tamaño {tamaño}:")
    for grupo, cantidad in contador.items():
        print(f"  {grupo}: {cantidad} veces")



pares_no_aparecidos = buscar_no_aparecidos(elegidas, 2)

print("Pares que no han aparecido:", len(pares_no_aparecidos))

for par in pares_no_aparecidos:
    print(par)


trios_no_aparecidos = buscar_no_aparecidos(elegidas, 3)

print("Tríos que no han aparecido:", len(trios_no_aparecidos))

for trio in trios_no_aparecidos:
    print(trio)