"""Crea y muestra una matriz aleatoria con asteriscos bajo la diagonal."""

import random

import numpy as np


def main() -> None:
    """Genera una matriz cuadrada de tamaño aleatorio e imprime su triángulo."""
    # Elegir un tamaño entre 4 y 12, incluidos ambos extremos.
    n = random.randint(4, 12)

    # Usar object permite guardar enteros (ceros) y cadenas (asteriscos).
    matriz = np.zeros((n, n), dtype=object)

    # Marcar las posiciones estrictamente debajo de la diagonal principal.
    for fila in range(1, n):
        for columna in range(fila):
            matriz[fila, columna] = "*"

    # Mostrar el tamaño elegido y el contenido de la matriz.
    print(f"Matriz de {n} x {n}:")
    print(matriz)


if __name__ == "__main__":
    # Ejecutar el programa cuando se inicia este archivo directamente.
    main()
