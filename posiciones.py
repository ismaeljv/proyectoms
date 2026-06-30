import random
from collections import defaultdict
from itertools import combinations

# =========================================================
# Parámetros
# =========================================================

N = 14
K = 7
NUM_BLOCKS = 16

MAX_PAIR_REP = 5
MAX_QUAD_REP = 1

ATTEMPTS_PER_BLOCK = 20000
GLOBAL_RESTARTS = 200

# =========================================================

ALL = list(range(1, N + 1))

# =========================================================

def build():

    pair_count = defaultdict(int)
    triple_count = defaultdict(int)
    quad_count = defaultdict(int)

    blocks = []

    # -----------------------------------------------------

    def valid(block):

        # cuartetos
        for q in combinations(block, 4):
            if quad_count[q] >= MAX_QUAD_REP:
                return False

        # pares
        for p in combinations(block, 2):
            if pair_count[p] >= MAX_PAIR_REP:
                return False

        return True

    # -----------------------------------------------------

    def score(block):

        s = 0

        # premiar tríos nuevos
        new_triples = 0

        for t in combinations(block, 3):

            c = triple_count[t]

            if c == 0:
                new_triples += 1

            s += c * 5

        # penalizar pares repetidos
        for p in combinations(block, 2):
            s += pair_count[p] * 15

        # ligera aleatoriedad
        s += random.random() * 3

        # queremos minimizar
        s -= new_triples * 10

        return s

    # -----------------------------------------------------

    def register(block):

        for p in combinations(block, 2):
            pair_count[p] += 1

        for t in combinations(block, 3):
            triple_count[t] += 1

        for q in combinations(block, 4):
            quad_count[q] += 1

    # =====================================================
    # Construcción
    # =====================================================

    for idx in range(NUM_BLOCKS):

        best = None
        best_score = 10**9

        for _ in range(ATTEMPTS_PER_BLOCK):

            cand = tuple(sorted(random.sample(ALL, K)))

            if cand in blocks:
                continue

            if not valid(cand):
                continue

            s = score(cand)

            if s < best_score:
                best_score = s
                best = cand

        if best is None:
            return None

        blocks.append(best)
        register(best)

        print(f"{idx+1:2d}: {best}   score={best_score:.2f}")

    return blocks, pair_count, triple_count, quad_count

# =========================================================
# Reinicios globales
# =========================================================

result = None

for restart in range(GLOBAL_RESTARTS):

    print(f"\n=== intento global {restart+1} ===")

    result = build()

    if result is not None:
        break

if result is None:
    raise Exception("No se encontró solución")

blocks, pair_count, triple_count, quad_count = result

# =========================================================
# Estadísticas
# =========================================================

print("\n==========================")
print("ESTADÍSTICAS")
print("==========================")

print("pares distintos:", len(pair_count))
print("máx par:", max(pair_count.values()))

print("tríos distintos:", len(triple_count))
print("máx trío:", max(triple_count.values()))

print("cuartetos distintos:", len(quad_count))
print("máx cuarteto:", max(quad_count.values()))

# =========================================================
# Aleatorización visual final
# =========================================================

print("\n==========================")
print("RESULTADO FINAL")
print("==========================")

# permutación global de etiquetas
perm = ALL[:]
random.shuffle(perm)

mapping = {
    i + 1: perm[i]
    for i in range(N)
}

final_blocks = []

for b in blocks:

    nb = sorted(mapping[x] for x in b)

    # desorden interno visual
    random.shuffle(nb)

    final_blocks.append(nb)

# desordenar orden de bloques
random.shuffle(final_blocks)

for i, b in enumerate(final_blocks, 1):
    print(f"{i:2d}: {b}")