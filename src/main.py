"""Interfaz de consola del sistema inteligente."""

from src.base_conocimiento import ESTACIONES
from src.busqueda import buscar_a_estrella


def resolver_estacion(valor):
    """Convierte un numero o un nombre escrito por el usuario en una estacion."""
    entrada = valor.strip()
    nombres = list(ESTACIONES)
    if entrada.isdigit():
        indice = int(entrada) - 1
        if 0 <= indice < len(nombres):
            return nombres[indice]
        raise ValueError(f"El numero debe estar entre 1 y {len(nombres)}.")

    coincidencias = {nombre.casefold(): nombre for nombre in nombres}
    if entrada.casefold() in coincidencias:
        return coincidencias[entrada.casefold()]
    raise ValueError(f"La estacion '{entrada}' no existe.")


def mostrar_estaciones():
    print("\nEstaciones disponibles:")
    for numero, nombre in enumerate(ESTACIONES, 1):
        print(f"{numero:>2}. {nombre}")


def ejecutar_consulta(cerradas):
    mostrar_estaciones()
    try:
        origen = resolver_estacion(input("\nNumero o nombre de la estacion de origen: "))
        destino = resolver_estacion(input("Numero o nombre de la estacion de destino: "))
        resultado = buscar_a_estrella(origen, destino, cerradas)
    except ValueError as error:
        print(f"\nError: {error}")
        return
    if not resultado.ruta:
        print("\nNo existe una ruta disponible con las restricciones actuales.")
        return
    print("\nRuta recomendada:")
    print(" -> ".join(resultado.ruta))
    print(f"Costo estimado: {resultado.costo} minutos")
    print(f"Estaciones recorridas: {len(resultado.ruta)}")
    print(f"Nodos explorados por {resultado.algoritmo}: {resultado.explorados}")


def cerrar_estacion(cerradas):
    mostrar_estaciones()
    try:
        nombre = resolver_estacion(
            input("\nNumero o nombre de la estacion que desea cerrar o reabrir: ")
        )
    except ValueError as error:
        print(f"Error: {error}")
        return
    if nombre in cerradas:
        cerradas.remove(nombre)
        print(f"{nombre} fue reabierta.")
    else:
        cerradas.add(nombre)
        print(f"{nombre} fue marcada como cerrada.")


def main():
    cerradas = set()
    while True:
        print("\n=== SISTEMA INTELIGENTE DE RUTAS DE TRANSMILENIO ===")
        print("1. Consultar mejor ruta")
        print("2. Ver estaciones")
        print("3. Cerrar o reabrir una estacion")
        print("4. Ver estaciones cerradas")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            ejecutar_consulta(cerradas)
        elif opcion == "2":
            mostrar_estaciones()
        elif opcion == "3":
            cerrar_estacion(cerradas)
        elif opcion == "4":
            print("Cerradas:", ", ".join(sorted(cerradas)) or "ninguna")
        elif opcion == "5":
            print("Hasta luego.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()

