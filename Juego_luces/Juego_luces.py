import numpy as np

cantidad_luces = 8


def alternar_luces(tablero, posicion):
    for indice in (posicion - 1, posicion, posicion + 1):
        if 0 <= indice < cantidad_luces:
            tablero[indice] = 1 - tablero[indice]


def tiene_solucion(tablero):
    for movimientos in range(1 << cantidad_luces):
        prueba = tablero.copy()
        for posicion in range(cantidad_luces):
            if movimientos & (1 << posicion):
                alternar_luces(prueba, posicion)
        if np.all(prueba == 0):
            return True
    return False

#_________________________________________________________________________

#quita tableros ganados .
while True:
    luces = np.random.randint(0, 2, size=cantidad_luces)
    if np.any(luces) and tiene_solucion(luces):
        break

print("Juego de luces")
print("0 = apagada, 1 = encendida")
print("Cada elección cambia la luz elegida y sus vecinas.")

while not np.all(luces == 0):
    print("Luces:", luces)

    try:
        posicion = int(input(f"Elige una posición (1-{cantidad_luces}): ")) - 1
    except ValueError:
        print("Ingresa un número entero.")
        continue

    if posicion < 0 or posicion >= cantidad_luces:
        print(f"La posición debe estar entre 1 y {cantidad_luces}.")
        continue

    alternar_luces(luces, posicion)

print("¡Ganaste! Todas las luces están apagadas.")
print("Luces:", luces)
