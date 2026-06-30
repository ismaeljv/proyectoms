from itertools import combinations, product
from pathlib import Path
import random
import os

DISTANCIA = 6
file_path = f"salida{DISTANCIA}.txt"
ruta = Path(f"{file_path}")

# combinación base (puedes cambiarla)
base = ['1','1','1','1','1','1','1','1','1','1','1','1','1','1']

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
def guardar_combinaciones(base, d, fichero=file_path):
    count = 0
    with open(fichero, "w") as f:
        for comb in generar_distancia(base, d):
            f.write(" ".join(comb) + "\n")
            count += 1

    print(f"Generadas {count} combinaciones")

def distancia(a,b):
    return sum(x != y for x,y in zip(a,b))

def parsear(linea):
    return linea.strip().split()

def guardar_lista(ruta, lineas_filtradas=[], max=0):
    if DISTANCIA == 6 and max >= 17:
        print(f"Entrando a guardar {max}")
    else:
        if DISTANCIA == 7 and max >= 12:
            print(f"Entrando a guardar {max}")
    #if not ruta.exists():
        #ruta_salida.write_text("\n".join(lineas_filtradas) + ("\n" if lineas_filtradas else ""), encoding="utf-8")
    with open(ruta, "a", encoding="utf-8") as f:
        for linea in lineas_filtradas:
            f.write(linea + "\n")



# ejecutar
if not os.path.exists(file_path):
    guardar_combinaciones(base, DISTANCIA)
else:
    print(f"El archivo {file_path} ya existe. No se generarán nuevas combinaciones.")

lineas = ruta.read_text(encoding="utf-8").splitlines()
print("lineas de lineas:", len(lineas))

maximo=0
lineas2 = []
lineas3 = []
lineas4 = []
lineas5 = []
lineas6 = []
lineas7 = []
lineas8 = []
lineas9 = []
lineas10 = []
lineas11 = []
lineas12 = []
lineas13 = []
lineas14 = []
lineas15 = []
lineas16 = []
lineas17 = []
lineas18 = []
lineas19 = []
lineas20 = []
lineas21 = []
lineas22 = []
seleccionadas = []
while lineas:
    indice = random.randrange(len(lineas))
    linea1 = parsear(lineas[indice])
    seleccionadas.append(" ".join(linea1))
    # print("Procesando:", linea)

    for linea2 in lineas:
        candidato = parsear(linea2)
        if distancia(candidato, linea1) == DISTANCIA:
            lineas2.append(candidato)
    
    if maximo < 1:
        maximo = 1
    # print("lineas de lineas2:", len(lineas2))

    while lineas2:
        linea2 = lineas2[0]
        seleccionadas.append(" ".join(linea2))
        for candidato in lineas2:
            # candidato = parsear(linea3)
            if distancia(candidato, linea2) == DISTANCIA:
                lineas3.append(candidato)
        if maximo < 2:
            maximo = 2

        while lineas3:
            linea3 = lineas3[0]
            seleccionadas.append(" ".join(linea3))
            for candidato in lineas3:
                # candidato = parsear(linea4)
                if distancia(candidato, linea3) == DISTANCIA:
                    lineas4.append(candidato)
            if maximo < 3:
                maximo = 3

            while lineas4:
                linea4 = lineas4[0]
                seleccionadas.append(" ".join(linea4))
                for candidato in lineas4:
                    # candidato = parsear(linea5)
                    if distancia(candidato, linea4) == DISTANCIA:
                        lineas5.append(candidato)
                if maximo < 4:
                    maximo = 4

                while lineas5:
                    linea5 = lineas5[0]
                    seleccionadas.append(" ".join(linea5))
                    for candidato in lineas5:
                        #candidato = parsear(linea6)
                        if distancia(candidato, linea5) == DISTANCIA:
                            lineas6.append(candidato)
                    if maximo < 5:
                        maximo = 5

                    while lineas6:
                        linea6 = lineas6[0]
                        seleccionadas.append(" ".join(linea6))
                        for candidato in lineas6:
                            # candidato = parsear(linea7)
                            if distancia(candidato, linea6) == DISTANCIA:
                                lineas7.append(candidato)
                        if maximo < 6:
                            maximo = 6
                        
                        while lineas7:
                            linea7 = lineas7[0]
                            seleccionadas.append(" ".join(linea7))
                            for candidato in lineas7:
                                # candidato = parsear(linea8)
                                if distancia(candidato, linea7) == DISTANCIA:
                                    lineas8.append(candidato)
                            if maximo < 7:
                                maximo = 7

                            while lineas8:
                                linea8 = lineas8[0]
                                seleccionadas.append(" ".join(linea8))
                                for candidato in lineas8:
                                    # candidato = parsear(linea9)
                                    if distancia(candidato, linea8) == DISTANCIA:
                                        lineas9.append(candidato)
                                if maximo < 8:
                                    maximo = 8

                                while lineas9:
                                    linea9 = lineas9[0]
                                    seleccionadas.append(" ".join(linea9))
                                    for candidato in lineas9:
                                        # candidato = parsear(linea10)
                                        if distancia(candidato, linea9) == DISTANCIA:
                                            lineas10.append(candidato)
                                    if maximo < 9:
                                        maximo = 9

                                    while lineas10:
                                        linea10 = lineas10[0]
                                        seleccionadas.append(" ".join(linea10))
                                        for candidato in lineas10:
                                            # candidato = parsear(linea11)
                                            if distancia(candidato, linea10) == DISTANCIA:
                                                lineas11.append(candidato)
                                        if maximo < 10:
                                            maximo = 10

                                        while lineas11:
                                            linea11 = lineas11[0]
                                            seleccionadas.append(" ".join(linea11))
                                            for candidato in lineas11:
                                                # candidato = parsear(linea12)
                                                if distancia(candidato, linea11) == DISTANCIA:
                                                    lineas12.append(candidato)
                                            if maximo < 11:
                                                maximo = 11

                                            while lineas12:
                                                linea12 = lineas12[0]
                                                seleccionadas.append(" ".join(linea12))
                                                for candidato in lineas12:
                                                    # candidato = parsear(linea13)
                                                    if distancia(candidato, linea12) == DISTANCIA:
                                                        lineas13.append(candidato)
                                                if maximo < 12:
                                                    maximo = 12

                                                while lineas13:
                                                    linea13 = lineas13[0]
                                                    seleccionadas.append(" ".join(linea13))
                                                    for candidato in lineas13:
                                                        # candidato = parsear(linea14)
                                                        if distancia(candidato, linea13) == DISTANCIA:
                                                            lineas14.append(candidato)
                                                    if maximo < 13:
                                                        maximo = 13

                                                    while lineas14:
                                                        linea14 = lineas14[0]
                                                        seleccionadas.append(" ".join(linea14))
                                                        for candidato in lineas14:
                                                            # candidato = parsear(linea15)
                                                            if distancia(candidato, linea14) == DISTANCIA:
                                                                lineas15.append(candidato)
                                                        if maximo < 14:
                                                            maximo = 14

                                                        while lineas15:
                                                            linea15 = lineas15[0]
                                                            seleccionadas.append(" ".join(linea15))
                                                            for candidato in lineas15:
                                                                # candidato = parsear(linea16)
                                                                if distancia(candidato, linea15) == DISTANCIA:
                                                                    lineas16.append(candidato)
                                                            if maximo < 15:
                                                                maximo = 15

                                                            while lineas16:
                                                                linea16 = lineas16[0]
                                                                seleccionadas.append(" ".join(linea16))
                                                                for candidato in lineas16:
                                                                    # candidato = parsear(linea17)
                                                                    if distancia(candidato, linea16) == DISTANCIA:
                                                                        lineas17.append(candidato)
                                                                if maximo < 16:
                                                                    maximo = 16

                                                                while lineas17:
                                                                    linea17 = lineas17[0]
                                                                    seleccionadas.append(" ".join(linea17))
                                                                    for candidato in lineas17:
                                                                        # candidato = parsear(linea18)
                                                                        if distancia(candidato, linea17) == DISTANCIA:
                                                                            lineas18.append(candidato)
                                                                    if maximo < 17:
                                                                        maximo = 17

                                                                    while lineas18:
                                                                        linea18 = lineas18[0]
                                                                        seleccionadas.append(" ".join(linea18))
                                                                        for candidato in lineas18:
                                                                            # candidato = parsear(linea19)
                                                                            if distancia(candidato, linea18) == DISTANCIA:
                                                                                lineas19.append(candidato)
                                                                        if maximo < 18:
                                                                            maximo = 18

                                                                        while lineas19:
                                                                            linea19 = lineas19[0]
                                                                            seleccionadas.append(" ".join(linea19))
                                                                            for candidato in lineas19:
                                                                                # candidato = parsear(linea20)
                                                                                if distancia(candidato, linea19) == DISTANCIA:
                                                                                    lineas20.append(candidato)
                                                                            if maximo < 19:
                                                                                maximo = 19
                                                                                
                                                                            while lineas20:
                                                                                linea20 = lineas20[0]
                                                                                seleccionadas.append(" ".join(linea20))
                                                                                for candidato in lineas20:
                                                                                    # candidato = parsear(linea21)
                                                                                    if distancia(candidato, linea20) == DISTANCIA:
                                                                                        lineas21.append(candidato)
                                                                                if maximo < 20:
                                                                                    maximo = 20
                                                                                    
                                                                             

                                                                                if maximo == 20:
                                                                                    ruta_salida = Path(f"seleccionadas{DISTANCIA}_{maximo}.txt")
                                                                                    guardar_lista(ruta_salida, seleccionadas)
                                                                                del lineas20[0]
                                                                                seleccionadas.pop()


                                                                            if maximo == 19:
                                                                                ruta_salida = Path(f"seleccionadas{DISTANCIA}_{maximo}.txt")
                                                                                guardar_lista(ruta_salida, seleccionadas)
                                                                            del lineas19[0]
                                                                            seleccionadas.pop()


                                                                        if maximo == 18:
                                                                            ruta_salida = Path(f"seleccionadas{DISTANCIA}_{maximo}.txt")
                                                                            guardar_lista(ruta_salida, seleccionadas)
                                                                        del lineas18[0]
                                                                        seleccionadas.pop()


                                                                    if maximo == 17:
                                                                        ruta_salida = Path(f"seleccionadas{DISTANCIA}_{maximo}.txt")
                                                                        guardar_lista(ruta_salida, seleccionadas)
                                                                    del lineas17[0]
                                                                    seleccionadas.pop()


                                                                if maximo == 16:
                                                                    ruta_salida = Path(f"seleccionadas{DISTANCIA}_{maximo}.txt")
                                                                    guardar_lista(ruta_salida, seleccionadas)
                                                                del lineas16[0]
                                                                seleccionadas.pop()


                                                            if maximo == 15:
                                                                ruta_salida = Path(f"seleccionadas{DISTANCIA}_{maximo}.txt")
                                                                guardar_lista(ruta_salida, seleccionadas)
                                                            del lineas15[0]
                                                            seleccionadas.pop()


                                                        if maximo == 14:
                                                            ruta_salida = Path(f"seleccionadas{DISTANCIA}_{maximo}.txt")
                                                            guardar_lista(ruta_salida, seleccionadas)
                                                        del lineas14[0]
                                                        seleccionadas.pop()


                                                    if maximo == 13:
                                                        ruta_salida = Path(f"seleccionadas{DISTANCIA}_{maximo}.txt")
                                                        guardar_lista(ruta_salida, seleccionadas)
                                                    del lineas13[0]
                                                    seleccionadas.pop()

                                                if maximo == 12:
                                                    ruta_salida = Path(f"seleccionadas{DISTANCIA}_{maximo}.txt")
                                                    guardar_lista(ruta_salida, seleccionadas)
                                                del lineas12[0]
                                                seleccionadas.pop()


                                            if maximo == 11:
                                                ruta_salida = Path(f"seleccionadas{DISTANCIA}_{maximo}.txt")
                                                guardar_lista(ruta_salida, seleccionadas)
                                            del lineas11[0]
                                            seleccionadas.pop()


                                        if maximo == 10:
                                            ruta_salida = Path(f"seleccionadas{DISTANCIA}_{maximo}.txt")
                                            guardar_lista(ruta_salida, seleccionadas)
                                        del lineas10[0]
                                        seleccionadas.pop()


                                    if maximo == 9:
                                        ruta_salida = Path(f"seleccionadas{DISTANCIA}_{maximo}.txt")
                                        guardar_lista(ruta_salida, seleccionadas)
                                    del lineas9[0]
                                    seleccionadas.pop()


                                if maximo == 8:
                                    ruta_salida = Path(f"seleccionadas{DISTANCIA}_{maximo}.txt")
                                    guardar_lista(ruta_salida, seleccionadas)
                                del lineas8[0]
                                seleccionadas.pop()

                            
                            if maximo == 7:
                                ruta_salida = Path(f"seleccionadas{DISTANCIA}_{maximo}.txt")
                                guardar_lista(ruta_salida, seleccionadas)
                            del lineas7[0]
                            seleccionadas.pop()


                        if maximo == 6:
                            ruta_salida = Path(f"seleccionadas{DISTANCIA}_{maximo}.txt")
                            guardar_lista(ruta_salida, seleccionadas)
                        del lineas6[0]
                        seleccionadas.pop()


                    if maximo == 5:
                        ruta_salida = Path(f"seleccionadas{DISTANCIA}_{maximo}.txt")
                        guardar_lista(ruta_salida, seleccionadas)
                    del lineas5[0]
                    seleccionadas.pop()


                if maximo == 4:
                    ruta_salida = Path(f"seleccionadas{DISTANCIA}_{maximo}.txt")
                    guardar_lista(ruta_salida, seleccionadas)
                del lineas4[0]
                seleccionadas.pop()

            if maximo == 3:
                ruta_salida = Path(f"seleccionadas{DISTANCIA}_{maximo}.txt")
                guardar_lista(ruta_salida, seleccionadas)
            del lineas3[0]
            seleccionadas.pop()

        if maximo == 2:
            ruta_salida = Path(f"seleccionadas{DISTANCIA}_{maximo}.txt")
            guardar_lista(ruta_salida, seleccionadas)
        del lineas2[0]
        seleccionadas.pop()

    # Eliminar la línea elegida
    del lineas[indice]
    seleccionadas.pop()
    exit(0)  # Salir después de la primera iteración para probar

    # Actualizar el fichero
    ruta.write_text(
        "\n".join(lineas) + ("\n" if lineas else ""),
        encoding="utf-8"
    )

