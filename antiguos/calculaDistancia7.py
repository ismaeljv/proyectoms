from itertools import combinations, product

# combinación base (puedes cambiarla)
base = ['1','1','1','2','1','1','1','1','1','2','2','1','1','1']

signos = ['1','X','2']

# genera combinaciones a distancia EXACTA d
def generar_distancia(base, d):
    n = len(base)

    for posiciones in combinations(range(n), d):
        # para cada posición elegimos signo distinto
        opciones = []
        for i in posiciones:
            opciones.append([s for s in signos if s != base[i]])

        for cambios in product(*opciones):
            nueva = base.copy()
            for i, pos in enumerate(posiciones):
                nueva[pos] = cambios[i]
            yield nueva

# guardar en fichero
def guardar_combinaciones(base, d, fichero="salida.txt"):
    count = 0
    with open(fichero, "w") as f:
        for comb in generar_distancia(base, d):
            f.write(" ".join(comb) + "\n")
            count += 1

    print(f"Generadas {count} combinaciones")

# ejecutar
guardar_combinaciones(base, 7)