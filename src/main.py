"""Interfaz de consola del sistema inteligente."""

from src.base_conocimiento import ESTACIONES
from src.busqueda import buscar_a_estrella


def mostrar_estaciones():
    print("\nEstaciones disponibles:")
    for numero, nombre in enumerate(ESTACIONES, 1):
        print(f"{numero:>2}. {nombre}")


def ejecutar_consulta(cerradas):
    mostrar_estaciones()
    origen = input("\nEstacion de origen: ").strip()
    destino = input("Estacion de destino: ").strip()
    try:
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
    nombre = input("\nEstacion que desea cerrar o reabrir: ").strip()
    if nombre not in ESTACIONES:
        print("La estacion indicada no existe.")
    elif nombre in cerradas:
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

