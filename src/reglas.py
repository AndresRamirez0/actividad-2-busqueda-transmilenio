"""Motor de reglas para validar hechos y movimientos."""

from src.base_conocimiento import ESTACIONES, RED


def estacion_valida(nombre, cerradas=frozenset()):
    """R1: una estacion se puede usar si existe y no esta cerrada."""
    return nombre in ESTACIONES and nombre not in cerradas


def puede_viajar(origen, destino, cerradas=frozenset()):
    """R2: hay movimiento si ambas estaciones estan habilitadas y conectadas."""
    return (estacion_valida(origen, cerradas)
            and estacion_valida(destino, cerradas)
            and destino in RED[origen])


def es_transbordo(estacion):
    """R3: los nodos declarados como transbordo permiten cambiar de troncal."""
    return ESTACIONES.get(estacion, {}).get("tipo") == "transbordo"


def validar_consulta(origen, destino, cerradas=frozenset()):
    """R4: valida los datos antes de ejecutar una busqueda."""
    if origen not in ESTACIONES:
        raise ValueError(f"La estacion de origen '{origen}' no existe.")
    if destino not in ESTACIONES:
        raise ValueError(f"La estacion de destino '{destino}' no existe.")
    if origen == destino:
        raise ValueError("El origen y el destino deben ser diferentes.")
    if origen in cerradas:
        raise ValueError(f"La estacion de origen '{origen}' esta cerrada.")
    if destino in cerradas:
        raise ValueError(f"La estacion de destino '{destino}' esta cerrada.")


def ruta_valida(ruta, cerradas=frozenset()):
    """R5: toda pareja consecutiva debe cumplir la regla de movimiento."""
    return bool(ruta) and all(
        puede_viajar(actual, siguiente, cerradas)
        for actual, siguiente in zip(ruta, ruta[1:])
    )

