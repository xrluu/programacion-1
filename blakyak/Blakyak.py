import random


VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
PALOS = ["♥", "♦", "♣", "♠"]


def crear_baraja():
    """Crea una baraja estándar de 52 cartas."""
    return [(valor, palo) for palo in PALOS for valor in VALORES]


def calcular_puntuacion(mano):
    """Suma una mano tratando los ases como 1 u 11 según convenga."""
    puntos = 0
    ases = 0

    for valor, _ in mano:
        if valor == "A":
            puntos += 11
            ases += 1
        elif valor in ("J", "Q", "K"):
            puntos += 10
        else:
            puntos += int(valor)

    while puntos > 21 and ases:
        puntos -= 10
        ases -= 1
    return puntos


def es_blackjack(mano):
    return len(mano) == 2 and calcular_puntuacion(mano) == 21


def dibujar_carta(valor, palo):
    """Imprime una carta en formato ASCII."""
    print("+-------+")
    print(f"| {valor:<2}    |")
    print("|       |")
    print(f"|   {palo}   |")
    print("|       |")
    print(f"|    {valor:>2} |")
    print("+-------+")


def dibujar_carta_oculta():
    print("+-------+")
    print("|       |")
    print("|       |")
    print("|   ?   |")
    print("|       |")
    print("|       |")
    print("+-------+")


def mostrar_mano(titulo, mano, ocultar_segunda=False):
    print(f"\n{titulo}:")
    for indice, (valor, palo) in enumerate(mano):
        if ocultar_segunda and indice == 1:
            dibujar_carta_oculta()
        else:
            dibujar_carta(valor, palo)

    if ocultar_segunda:
        print(f"Puntuación visible: {calcular_puntuacion(mano[:1])}")
    else:
        print(f"Puntuación: {calcular_puntuacion(mano)}")


def pedir_apuesta(saldo):
    while True:
        entrada = input(f"\nTienes ${saldo:g}. ¿Cuánto quieres apostar?: ").strip()
        try:
            apuesta = int(entrada)
        except ValueError:
            print("Escribe una cantidad entera válida.")
            continue

        if 1 <= apuesta <= saldo:
            return apuesta
        print(f"La apuesta debe ser entre $1 y ${saldo:g}.")


def jugar_ronda(apuesta):
    baraja = crear_baraja()
    random.shuffle(baraja)

    jugador = [baraja.pop(), baraja.pop()]
    banca = [baraja.pop(), baraja.pop()]

    mostrar_mano("Tus cartas", jugador)
    mostrar_mano("Cartas de la banca", banca, ocultar_segunda=True)

    while calcular_puntuacion(jugador) < 21:
        accion = input("\n¿Quieres pedir carta o plantarte? (p/s): ").strip().lower()
        if accion in ("p", "pedir"):
            jugador.append(baraja.pop())
            mostrar_mano("Tus cartas", jugador)
        elif accion in ("s", "plantarme", "plantarse"):
            break
        else:
            print("Opción no válida. Escribe 'p' para pedir o 's' para plantarte.")

    puntuacion_jugador = calcular_puntuacion(jugador)
    if puntuacion_jugador <= 21:
        while calcular_puntuacion(banca) < 17:
            banca.append(baraja.pop())

    mostrar_mano("Tus cartas", jugador)
    mostrar_mano("Cartas de la banca", banca)

    puntuacion_banca = calcular_puntuacion(banca)
    blackjack_jugador = es_blackjack(jugador)
    blackjack_banca = es_blackjack(banca)

    if puntuacion_jugador > 21:
        print("\nTe pasaste de 21. ¡Gana la banca!")
        ganancia = -apuesta
    elif blackjack_jugador and not blackjack_banca:
        ganancia = apuesta * 1.5
        print(f"\n¡Blackjack! ¡Ganaste ${ganancia:g}!")
    elif blackjack_banca and not blackjack_jugador:
        print("\nLa banca tiene blackjack. Gana la banca.")
        ganancia = -apuesta
    elif puntuacion_banca > 21:
        print("\nLa banca se pasó de 21. ¡Ganaste!")
        ganancia = apuesta
    elif puntuacion_jugador > puntuacion_banca:
        print("\n¡Ganaste!")
        ganancia = apuesta
    elif puntuacion_jugador < puntuacion_banca:
        print("\nGana la banca.")
        ganancia = -apuesta
    else:
        print("\nEmpate.")
        ganancia = 0

    return ganancia


def main():
    print("¡Bienvenido a 21!")
    saldo = 100
    while saldo > 0:
        apuesta = pedir_apuesta(saldo)
        saldo += jugar_ronda(apuesta)
        print(f"\nTu saldo ahora es ${saldo:g}.")
        if saldo == 0:
            print("Te quedaste sin fichas.")
            break

        while True:
            respuesta = input("\n¿Quieres jugar otra ronda? (s/n): ").strip().lower()
            if respuesta in ("s", "si", "sí"):
                break
            if respuesta in ("n", "no"):
                print("¡Gracias por jugar!")
                return
            print("Respuesta no valida")

    print("¡Gracias por jugar!")


if __name__ == "__main__":
    main()

#este programa es un juego de blackjack (21) en la consola. El jugador comienza con un saldo inicial y puede apostar en cada ronda. El juego sigue las reglas estándar del blackjack, incluyendo la opción de pedir cartas o plantarse, y la banca juega automáticamente siguiendo sus propias reglas. Al final de cada ronda, se muestra el resultado y el saldo actualizado del jugador.