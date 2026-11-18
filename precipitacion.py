import csv
from datetime import date, datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt


def leer_precipitaciones(ruta_csv: str) -> tuple[list[date], list[float]]:
    fechas: list[date] = []
    precipitaciones: list[float] = []

    with open(ruta_csv, "r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.reader(archivo)
        next(lector, None)  # Omitir el encabezado

        for numero_fila, fila in enumerate(lector, start=2):
            if not fila:
                continue
            if len(fila) != 2:
                raise ValueError(
                    f"La fila {numero_fila} debe tener dos columnas: fecha y precipitación."
                )

            texto_fecha, texto_precipitacion = (valor.strip() for valor in fila)
            try:
                try:
                    fecha = date.fromisoformat(texto_fecha)
                except ValueError:
                    fecha = datetime.strptime(texto_fecha, "%d/%m/%Y").date()
                precipitacion = float(texto_precipitacion)
            except ValueError as error:
                raise ValueError(
                    f"Datos no válidos en la fila {numero_fila}: {error}"
                ) from error

            fechas.append(fecha)
            precipitaciones.append(precipitacion)

    return fechas, precipitaciones


def mostrar_resultados(fechas: list[date], precipitaciones: list[float]) -> None:
    if not fechas:
        print("El archivo no contiene datos de precipitación.")
        return

    print("Días con al menos 20 mm de precipitación:")
    dias_lluviosos = [
        fecha
        for fecha, cantidad in zip(fechas, precipitaciones)
        if cantidad >= 20
    ]
    if dias_lluviosos:
        for fecha in dias_lluviosos:
            print(fecha.strftime("%d/%m/%Y"))
    else:
        print("No se registraron días con al menos 20 mm.")

    maxima = max(precipitaciones)
    fechas_maximas = [
        fecha
        for fecha, cantidad in zip(fechas, precipitaciones)
        if cantidad == maxima
    ]
    print(f"\nPrecipitación máxima diaria: {maxima:g} mm")
    print("Fecha(s) en que se alcanzó:")
    for fecha in fechas_maximas:
        print(fecha.strftime("%d/%m/%Y"))

    figura, eje = plt.subplots(figsize=(12, 6))
    eje.bar(fechas, precipitaciones, color="tab:blue")
    eje.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%Y"))
    eje.set_title("Precipitación diaria")
    eje.set_xlabel("Fecha")
    eje.set_ylabel("Precipitación (mm)")
    eje.grid(axis="y", linestyle=":", alpha=0.6)
    figura.autofmt_xdate(rotation=45)
    figura.tight_layout()
    plt.show()


def main() -> None:
    ruta_csv = input("Ruta del archivo CSV de precipitaciones: ").strip()
    try:
        fechas, precipitaciones = leer_precipitaciones(ruta_csv)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta_csv}")
        return
    except ValueError as error:
        print(f"Error al leer el archivo: {error}")
        return

    mostrar_resultados(fechas, precipitaciones)


if __name__ == "__main__":
    main()
