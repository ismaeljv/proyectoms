from itertools import combinations, product
from pathlib import Path
import os
import random

# ==========================================================
# CONFIGURACIÓN
# ==========================================================

DISTANCIA = 6

BASE = ['1','1','1','1','1','1','1','1','1','1','1','1','1','1']

SIGNOS = ['1','X','2']

FICHERO_CANDIDATOS = f"salida{DISTANCIA}.txt"
FICHERO_MAXIMO = "maximo.txt"

# ==========================================================
# FUNCIONES
# ==========================================================

def distancia(a,b):
    return sum(x != y for x,y in zip(a,b))


def parsear(linea):
    return linea.strip().split()


def generar_distancia(base, d):

    n = len(base)

    for posiciones in combinations(range(n), d):

        opciones = []

        for i in posiciones:
            opciones.append(
                [s for s in SIGNOS if s != base[i]]
            )

        for cambios in product(*opciones):

            nueva = base.copy()

            for i, pos in enumerate(posiciones):
                nueva[pos] = cambios[i]

            yield nueva


def guardar_combinaciones(base, d, fichero):

    count = 0

    with open(fichero, "w", encoding="utf8") as f:

        for comb in generar_distancia(base, d):

            f.write(" ".join(comb) + "\n")
            count += 1

    print(f"Generadas {count} combinaciones")


def leer_maximo():

    if not os.path.exists(FICHERO_MAXIMO):
        return 0

    try:
        with open(FICHERO_MAXIMO, "r") as f:
            return int(f.read().strip())
    except:
        return 0


def guardar_maximo(valor):

    with open(FICHERO_MAXIMO, "w") as f:
        f.write(str(valor))


# ==========================================================
# GENERAR CANDIDATOS SI NO EXISTEN
# ==========================================================

if not os.path.exists(FICHERO_CANDIDATOS):

    print("Generando fichero de candidatos...")
    guardar_combinaciones(
        BASE,
        DISTANCIA,
        FICHERO_CANDIDATOS
    )

# ==========================================================
# CARGAR CANDIDATOS
# ==========================================================

ruta = Path(FICHERO_CANDIDATOS)

lineas = ruta.read_text(
    encoding="utf8"
).splitlines()

if not lineas:

    print("No quedan semillas por procesar")
    exit()

print("Semillas pendientes:", len(lineas))

# ==========================================================
# ELEGIR SEMILLA ALEATORIA
# ==========================================================

indice = random.randrange(len(lineas))

semilla_linea = lineas[indice]

print()
print("Semilla elegida:")
print(semilla_linea)

# Eliminar semilla para no reutilizarla

del lineas[indice]

ruta.write_text(
    "\n".join(lineas) + ("\n" if lineas else ""),
    encoding="utf8"
)

# ==========================================================
# BUSQUEDA VORAZ
# ==========================================================

base = BASE.copy()

semilla = parsear(semilla_linea)

seleccionadas = [
    base,
    semilla
]

print()
print("Construyendo solución...")

for linea in lineas:

    candidato = parsear(linea)

    valido = True

    for apuesta in seleccionadas:

        if distancia(candidato, apuesta) != DISTANCIA:
            valido = False
            break

    if valido:
        seleccionadas.append(candidato)

print("Apuestas obtenidas:", len(seleccionadas))

# ==========================================================
# COMPROBAR RECORD
# ==========================================================

maximo = leer_maximo()

print("Récord actual:", maximo)

if len(seleccionadas) > maximo:

    nuevo_maximo = len(seleccionadas)

    print()
    print("¡¡ NUEVO RECORD !!")
    print("Anterior:", maximo)
    print("Nuevo:", nuevo_maximo)

    guardar_maximo(nuevo_maximo)

    nombre_salida = f"seleccionadas{nuevo_maximo}.txt"

    with open(nombre_salida, "w", encoding="utf8") as f:

        for apuesta in seleccionadas:
            f.write(" ".join(apuesta) + "\n")

    print("Guardado:", nombre_salida)

else:

    print()
    print("No se supera el récord")