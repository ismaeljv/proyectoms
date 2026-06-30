from itertools import combinations, product
import random
import time

# ==========================================================
# CONFIGURACIÓN
# ==========================================================

DISTANCIA = 7
NUM_INTENTOS = 10000

BASE = ('1','1','1','2','1','1','1','1','1','2','2','1','1','1')

SIGNOS = ('1', 'X', '2')

# ==========================================================
# FUNCIONES
# ==========================================================

def distancia(a, b):
    return sum(x != y for x, y in zip(a, b))


def generar_distancia(base, d):

    n = len(base)

    for posiciones in combinations(range(n), d):

        opciones = []

        for i in posiciones:
            opciones.append(
                [s for s in SIGNOS if s != base[i]]
            )

        for cambios in product(*opciones):

            nueva = list(base)

            for idx, pos in enumerate(posiciones):
                nueva[pos] = cambios[idx]

            yield tuple(nueva)

# ==========================================================
# GENERAR CANDIDATOS UNA SOLA VEZ
# ==========================================================

print("Generando candidatos...")

candidatos = list(generar_distancia(BASE, DISTANCIA))

print("Candidatos:", len(candidatos))

# ==========================================================
# BUSQUEDA VORAZ REPETIDA
# ==========================================================

inicio = time.time()

mejor_solucion = [BASE]
mejor_tam = 1

for intento in range(1, NUM_INTENTOS + 1):

    random.shuffle(candidatos)

    solucion = [BASE]

    for cand in candidatos:

        valido = True

        for apuesta in solucion:

            if distancia(cand, apuesta) != DISTANCIA:
                valido = False
                break

        if valido:
            solucion.append(cand)

    if len(solucion) > mejor_tam:

        mejor_tam = len(solucion)
        mejor_solucion = solucion.copy()

        print(
            f"[{intento}] Nuevo récord: "
            f"{mejor_tam} apuestas"
        )

    if intento % 100 == 0:

        transcurrido = time.time() - inicio

        print(
            f"Intento {intento}/{NUM_INTENTOS} "
            f" | Mejor={mejor_tam}"
            f" | {transcurrido:.1f}s"
        )

# ==========================================================
# RESULTADO
# ==========================================================

print()
print("=" * 60)
print("MEJOR SOLUCIÓN ENCONTRADA")
print("=" * 60)
print("Número apuestas:", mejor_tam)
print()

for i, apuesta in enumerate(mejor_solucion, start=1):
    print(f"{i:3d}", " ".join(apuesta))