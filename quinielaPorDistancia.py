from itertools import combinations, product
import random

# ==========================================================
# CONFIGURACIÓN
# ==========================================================

DISTANCIA = 7

BASE = ['1','1','1','2','1','1','1','1','1','2','2','1','1','1']

SIGNOS = ['1', 'X', '2']

# ==========================================================
# FUNCIONES
# ==========================================================

def distancia(a, b):
    return sum(x != y for x, y in zip(a, b))


def generar_distancia(base, d):
    """
    Genera todas las combinaciones a distancia exacta d
    respecto a la combinación base.
    """
    n = len(base)

    for posiciones in combinations(range(n), d):

        opciones = []
        for i in posiciones:
            opciones.append([s for s in SIGNOS if s != base[i]])

        for cambios in product(*opciones):

            nueva = base.copy()

            for i, pos in enumerate(posiciones):
                nueva[pos] = cambios[i]

            yield nueva


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

print('  1    2    3    4    5    6    7    8    9    10   11   12   13   14')

apuestas = [BASE]

print(BASE)

# Todos los candidatos a distancia DISTANCIA de la base
candidatos = list(generar_distancia(BASE, DISTANCIA))

# Mezcla aleatoria para que el resultado cambie en cada ejecución
random.shuffle(candidatos)

while candidatos:

    candidato = candidatos.pop()

    # Debe estar a DISTANCIA de TODAS las apuestas aceptadas
    if all(distancia(candidato, a) == DISTANCIA for a in apuestas):

        apuestas.append(candidato)
        print(candidato)

        # Eliminar candidatos que ya nunca podrán ser válidos
        candidatos = [
            c for c in candidatos
            if distancia(c, candidato) == DISTANCIA
        ]

print()
print(f"Total apuestas generadas: {len(apuestas)}")