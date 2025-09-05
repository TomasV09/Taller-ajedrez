import random
def mostrar_tablero(tablero):
    for fila in tablero:
        for elemento in fila:
            print(elemento, end=" ")
        print()
    print()

def movimientos_reina(tamano, pos_reina, bloqueos=None):
    if bloqueos is None:
        bloqueos = []

    y, x = pos_reina
    tablero = [["." for _ in range(tamano)] for _ in range(tamano)]
    tablero[y][x] = "R"  

    bloqueos_set = set(bloqueos)
    for by, bx in bloqueos:
        tablero[by][bx] = "X"

    direcciones = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

    posiciones = []

    for dy, dx in direcciones:
        ny, nx = y + dy, x + dx
        while 0 <= ny < tamano and 0 <= nx < tamano:
            if (ny, nx) in bloqueos_set:
                break
            posiciones.append((ny, nx))
            ny += dy
            nx += dx

    return tablero, posiciones


tamano_tablero = int(input("Ingrese el tamaño del tablero: "))
posicion_reina = (tamano_tablero // 2, tamano_tablero // 2)
num_bloqueos = int(input("Ingrese el número de bloqueos: "))
bloqueos = []

while len(bloqueos) < num_bloqueos:
    b = (random.randint(0, tamano_tablero - 1), random.randint(0, tamano_tablero - 1))
    if b != posicion_reina and b not in bloqueos:
        bloqueos.append(b)

tablero, posiciones = movimientos_reina(tamano_tablero, posicion_reina, bloqueos)

for (ry, rx) in posiciones:
    if tablero[ry][rx] == ".":
        tablero[ry][rx] = "*"

mostrar_tablero(tablero)
print(f"La reina puede moverse a {len(posiciones)} posiciones.")