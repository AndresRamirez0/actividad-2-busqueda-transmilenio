"""Hechos de la base de conocimiento del modelo academico.

Los tiempos son estimaciones didacticas, no informacion operacional oficial.
"""

ESTACIONES = {
    "Portal Norte": {"troncal": "Autopista Norte", "posicion": (0, 19), "tipo": "portal"},
    "Toberin": {"troncal": "Autopista Norte", "posicion": (0, 17), "tipo": "estacion"},
    "Calle 146": {"troncal": "Autopista Norte", "posicion": (0, 15), "tipo": "estacion"},
    "Alcala": {"troncal": "Autopista Norte", "posicion": (0, 13), "tipo": "estacion"},
    "Prado": {"troncal": "Autopista Norte", "posicion": (0, 11), "tipo": "estacion"},
    "Calle 127": {"troncal": "Autopista Norte", "posicion": (0, 9), "tipo": "estacion"},
    "Pepe Sierra": {"troncal": "Autopista Norte", "posicion": (0, 7), "tipo": "estacion"},
    "Calle 100": {"troncal": "Autopista Norte", "posicion": (0, 5), "tipo": "estacion"},
    "Virrey": {"troncal": "Autopista Norte", "posicion": (0, 3), "tipo": "estacion"},
    "Calle 85": {"troncal": "Autopista Norte", "posicion": (0, 1), "tipo": "estacion"},
    "Heroes": {"troncal": "Caracas", "posicion": (0, -1), "tipo": "transbordo"},
    "Calle 76": {"troncal": "Caracas", "posicion": (0, -3), "tipo": "estacion"},
    "Calle 72": {"troncal": "Caracas", "posicion": (0, -5), "tipo": "estacion"},
    "Flores": {"troncal": "Caracas", "posicion": (0, -7), "tipo": "estacion"},
    "Calle 63": {"troncal": "Caracas", "posicion": (0, -9), "tipo": "estacion"},
    "Calle 57": {"troncal": "Caracas", "posicion": (0, -11), "tipo": "estacion"},
    "Marly": {"troncal": "Caracas", "posicion": (0, -13), "tipo": "estacion"},
    "Calle 45": {"troncal": "Caracas", "posicion": (0, -15), "tipo": "estacion"},
    "Calle 26": {"troncal": "Caracas", "posicion": (0, -17), "tipo": "transbordo"},
    "Centro Memoria": {"troncal": "Calle 26", "posicion": (3, -17), "tipo": "estacion"},
    "Universidad Nacional": {"troncal": "Calle 26", "posicion": (6, -17), "tipo": "estacion"},
    "Gobernacion": {"troncal": "Calle 26", "posicion": (9, -17), "tipo": "estacion"},
    "CAN": {"troncal": "Calle 26", "posicion": (12, -17), "tipo": "estacion"},
    "El Tiempo-Maloka": {"troncal": "Calle 26", "posicion": (15, -17), "tipo": "estacion"},
    "Portal El Dorado": {"troncal": "Calle 26", "posicion": (18, -17), "tipo": "portal"},
}

# Cada tupla contiene: origen, destino y minutos estimados.
CONEXIONES = [
    ("Portal Norte", "Toberin", 4), ("Toberin", "Calle 146", 3),
    ("Calle 146", "Alcala", 3), ("Alcala", "Prado", 3),
    ("Prado", "Calle 127", 3), ("Calle 127", "Pepe Sierra", 3),
    ("Pepe Sierra", "Calle 100", 3), ("Calle 100", "Virrey", 3),
    ("Virrey", "Calle 85", 3), ("Calle 85", "Heroes", 3),
    ("Heroes", "Calle 76", 3), ("Calle 76", "Calle 72", 3),
    ("Calle 72", "Flores", 3), ("Flores", "Calle 63", 3),
    ("Calle 63", "Calle 57", 3), ("Calle 57", "Marly", 3),
    ("Marly", "Calle 45", 3), ("Calle 45", "Calle 26", 4),
    ("Calle 26", "Centro Memoria", 4), ("Centro Memoria", "Universidad Nacional", 4),
    ("Universidad Nacional", "Gobernacion", 4), ("Gobernacion", "CAN", 4),
    ("CAN", "El Tiempo-Maloka", 4), ("El Tiempo-Maloka", "Portal El Dorado", 5),
    # Enlaces alternativos permiten demostrar recalculo ante cierres.
    ("Heroes", "Calle 72", 7), ("Calle 26", "Universidad Nacional", 9),
]


def construir_red():
    """Construye un grafo no dirigido a partir de los hechos de conexion."""
    red = {nombre: {} for nombre in ESTACIONES}
    for origen, destino, costo in CONEXIONES:
        red[origen][destino] = costo
        red[destino][origen] = costo
    return red


RED = construir_red()

