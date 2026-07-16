import random
from collections import defaultdict

# =========================================================
# CONFIGURACIÓN
# =========================================================

NUM_APUESTAS = 32

DISTANCIA_MIN = 4
DISTANCIA_MAX = 7

TOLERANCIA = 0

DEBUG_CADA = 1000

MAX_INTENTOS = 2000

# =========================================================
# APUESTA BASE
# =========================================================

#base= ['1','2','1','2','2','1','1','1','1','1','2','1','2','2']
base = ['1','2','1','2','2','1','1','1','X','1','2','1','2','2']



# =========================================================
# RESTRICCIONES
# =========================================================

"""restricciones = [
    {'1':22, 'X':5, '2':5},
    {'1':8, 'X':8, '2':16},
    {'1':21, 'X':6, '2':5},
    {'1':9, 'X':10, '2':13},
    {'1':8, 'X':8, '2':16},
    {'1':18, 'X':8, '2':6},
    {'1':22, 'X':5, '2':5},
    {'1':18, 'X':7, '2':7},
    {'1':11, 'X':11, '2':10},
    {'1':17, 'X':8, '2':7},
    {'1':9, 'X':8, '2':15},
    {'1':22, 'X':6, '2':4},
    {'1':7, 'X':7, '2':18},
    {'1':10, 'X':8, '2':14},
]

restricciones = [
    {'1':24, 'X':4, '2':4},
    {'1':8, 'X':8, '2':16},
    {'1':20, 'X':6, '2':6},
    {'1':9, 'X':10, '2':13},
    {'1':8, 'X':8, '2':16},
    {'1':17, 'X':8, '2':7},
    {'1':23, 'X':5, '2':4},
    {'1':18, 'X':7, '2':7},
    {'1':11, 'X':11, '2':10},
    {'1':17, 'X':8, '2':7},
    {'1':8, 'X':8, '2':16},
    {'1':22, 'X':6, '2':4},
    {'1':7, 'X':6, '2':19},
    {'1':10, 'X':9, '2':13},
]"""

restricciones = [
    {'1':23, 'X':5, '2':4},
    {'1':8, 'X':8, '2':16},
    {'1':21, 'X':6, '2':5},
    {'1':9, 'X':10, '2':13},
    {'1':8, 'X':8, '2':16},
    {'1':18, 'X':8, '2':6},
    {'1':22, 'X':6, '2':4},
    {'1':18, 'X':7, '2':7},
    {'1':11, 'X':12, '2':9},
    {'1':18, 'X':8, '2':6},
    {'1':8, 'X':8, '2':16},
    {'1':22, 'X':6, '2':4},
    {'1':7, 'X':6, '2':19},
    {'1':9, 'X':9, '2':14},
]

# =========================================================
# PREPARACIÓN
# =========================================================

signos = ['1', 'X', '2']

usados = []

for r in restricciones:
    usados.append({
        '1': 0,
        'X': 0,
        '2': 0
    })

apuestas = []

historico_posiciones = []

rechazos_sin_opciones = 0
rechazos_distancia = 0

# =========================================================
# FUNCIONES
# =========================================================

def distancia(a, b):

    return sum(
        x != y
        for x, y in zip(a, b)
    )


def posiciones_distintas(a, b):

    return set(
        i
        for i in range(len(a))
        if a[i] != b[i]
    )


def score_separacion(posiciones):

    """
    Cuanto mayor, más distinta respecto
    a apuestas anteriores
    """

    if not historico_posiciones:
        return 999999

    total = 0

    for h in historico_posiciones:

        total += len(
            posiciones.symmetric_difference(h)
        )

    return total


def restricciones_ok(usados, restricciones):

    for i in range(14):

        for signo in signos:

            objetivo = restricciones[i][signo]
            real = usados[i][signo]

            if abs(real - objetivo) > TOLERANCIA:
                return False

    return True


def generar_candidata():

    global rechazos_sin_opciones

    apuesta = base.copy()

    # distancia aleatoria 6-7
    distancia_objetivo = random.randint(
        DISTANCIA_MIN,
        DISTANCIA_MAX
    )

    posiciones = random.sample(
        range(14),
        distancia_objetivo
    )

    for pos in posiciones:

        disponibles = []

        for signo in signos:

            # no repetir signo base
            if signo == base[pos]:
                continue

            # respetar restricciones + tolerancia
            if usados[pos][signo] < (
                restricciones[pos][signo]
                + TOLERANCIA
            ):

                disponibles.append(signo)

        if not disponibles:

            rechazos_sin_opciones += 1
            return None

        # =====================================
        # selección ponderada inteligente
        # =====================================

        weights = []

        for s in disponibles:

            restante = (
                restricciones[pos][s]
                - usados[pos][s]
            )

            weights.append(max(restante, 1))

        elegido = random.choices(
            disponibles,
            weights=weights,
            k=1
        )[0]

        apuesta[pos] = elegido

    return apuesta


# =========================================================
# INFORMACIÓN PREVIA
# =========================================================

print()
print("=" * 60)
print("CAPACIDAD DE CAMBIO")
print("=" * 60)

capacidad_total = 0

for i in range(14):

    capacidad = 0

    for signo in signos:

        if signo != base[i]:

            capacidad += restricciones[i][signo]

    capacidad_total += capacidad

    print(
        f"Partido {i+1:02d}: "
        f"{capacidad}"
    )

print()
print("Capacidad total:", capacidad_total)

print(
    "Cambios necesarios aprox:",
    NUM_APUESTAS * (
        (DISTANCIA_MIN + DISTANCIA_MAX) / 2
    )
)

print("=" * 60)
print()

# =========================================================
# GENERACIÓN
# =========================================================

intentos = 0

while (
    len(apuestas) < NUM_APUESTAS
    and intentos < MAX_INTENTOS
):

    intentos += 1

    mejor = None
    mejor_score = -1

    # múltiples candidatas
    for _ in range(300):

        candidata = generar_candidata()

        if candidata is None:
            continue

        d = distancia(base, candidata)

        if not (
            DISTANCIA_MIN <= d <= DISTANCIA_MAX
        ):

            rechazos_distancia += 1
            continue

        posiciones = posiciones_distintas(
            base,
            candidata
        )

        score = score_separacion(
            posiciones
        )

        if score > mejor_score:

            mejor = candidata
            mejor_score = score

    # =====================================
    # DEBUG
    # =====================================

    if intentos % DEBUG_CADA == 0:

        print()
        print("=" * 60)
        print(f"Intentos: {intentos}")
        print(
            f"Apuestas: "
            f"{len(apuestas)}/{NUM_APUESTAS}"
        )
        print(
            f"Rechazos sin opciones: "
            f"{rechazos_sin_opciones}"
        )
        print(
            f"Rechazos distancia: "
            f"{rechazos_distancia}"
        )

        print()

        print("Uso actual:")

        for i in range(14):

            print(
                f"{i+1:02d} | "
                f"1={usados[i]['1']:2d}/"
                f"{restricciones[i]['1']:2d}  "
                f"X={usados[i]['X']:2d}/"
                f"{restricciones[i]['X']:2d}  "
                f"2={usados[i]['2']:2d}/"
                f"{restricciones[i]['2']:2d}"
            )

        print("=" * 60)

    if mejor is None:
        continue

    # =====================================
    # REGISTRAR APUESTA
    # =====================================

    apuestas.append(mejor)

    posiciones = posiciones_distintas(
        base,
        mejor
    )

    historico_posiciones.append(
        posiciones
    )

    for i in range(14):

        signo = mejor[i]

        usados[i][signo] += 1

    print()
    print(
        f"APUESTA {len(apuestas)}"
    )

    print(
        f"Distancia: "
        f"{distancia(base, mejor)}"
    )

    print(
        f"Score separación: "
        f"{mejor_score}"
    )

    print(
        f"Posiciones cambiadas: "
        f"{sorted(list(posiciones))}"
    )

    print(mejor)

# =========================================================
# RESULTADOS
# =========================================================

print()
print("#" * 60)
print("RESULTADO FINAL")
print("#" * 60)
print()

print(
    f"Apuestas generadas: "
    f"{len(apuestas)}"
)

print(
    f"Intentos totales: "
    f"{intentos}"
)

print()

for i, a in enumerate(apuestas, start=1):

    print(f"{i}: {a}")

# =========================================================
# VALIDACIÓN
# =========================================================

print()
print("#" * 60)
print("VALIDACIÓN")
print("#" * 60)
print()

ok = restricciones_ok(
    usados,
    restricciones
)

print(
    "VALIDACIÓN GLOBAL:",
    "OK" if ok else "NO OK"
)

print()

for i in range(14):

    conteo = defaultdict(int)

    for a in apuestas:

        conteo[a[i]] += 1

    print(
        f"Partido {i+1:02d}: "
        f"1={conteo['1']:2d}/"
        f"{restricciones[i]['1']:2d}   "
        f"X={conteo['X']:2d}/"
        f"{restricciones[i]['X']:2d}   "
        f"2={conteo['2']:2d}/"
        f"{restricciones[i]['2']:2d}"
    )

