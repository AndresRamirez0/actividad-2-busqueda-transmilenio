"""Algoritmos A* y Dijkstra para buscar rutas de costo minimo."""

from dataclasses import dataclass
import heapq
import math

from src.base_conocimiento import ESTACIONES, RED
from src.reglas import puede_viajar, validar_consulta


@dataclass(frozen=True)
class ResultadoRuta:
    ruta: list[str]
    costo: int
    explorados: int
    algoritmo: str


def heuristica(actual, destino):
    """Distancia euclidiana admisible en el plano academico de estaciones."""
    x1, y1 = ESTACIONES[actual]["posicion"]
    x2, y2 = ESTACIONES[destino]["posicion"]
    # Los costos minimos por unidad son mayores o iguales a uno.
    return math.hypot(x2 - x1, y2 - y1)


def _reconstruir(anterior, destino):
    ruta = [destino]
    while ruta[-1] in anterior:
        ruta.append(anterior[ruta[-1]])
    ruta.reverse()
    return ruta


def buscar_a_estrella(origen, destino, cerradas=frozenset()):
    """Encuentra la ruta de menor costo mediante A*."""
    cerradas = frozenset(cerradas)
    validar_consulta(origen, destino, cerradas)
    frontera = [(heuristica(origen, destino), 0, origen)]
    costos = {origen: 0}
    anterior = {}
    explorados = set()

    while frontera:
        _, costo_actual, actual = heapq.heappop(frontera)
        if actual in explorados:
            continue
        explorados.add(actual)
        if actual == destino:
            return ResultadoRuta(_reconstruir(anterior, destino), costo_actual,
                                 len(explorados), "A*")
        for vecino, costo_arista in RED[actual].items():
            if not puede_viajar(actual, vecino, cerradas):
                continue
            nuevo_costo = costo_actual + costo_arista
            if nuevo_costo < costos.get(vecino, math.inf):
                costos[vecino] = nuevo_costo
                anterior[vecino] = actual
                prioridad = nuevo_costo + heuristica(vecino, destino)
                heapq.heappush(frontera, (prioridad, nuevo_costo, vecino))
    return ResultadoRuta([], math.inf, len(explorados), "A*")


def buscar_dijkstra(origen, destino, cerradas=frozenset()):
    """Algoritmo sin heuristica usado como referencia para las pruebas."""
    cerradas = frozenset(cerradas)
    validar_consulta(origen, destino, cerradas)
    frontera = [(0, origen)]
    costos = {origen: 0}
    anterior = {}
    explorados = set()
    while frontera:
        costo_actual, actual = heapq.heappop(frontera)
        if actual in explorados:
            continue
        explorados.add(actual)
        if actual == destino:
            return ResultadoRuta(_reconstruir(anterior, destino), costo_actual,
                                 len(explorados), "Dijkstra")
        for vecino, costo_arista in RED[actual].items():
            if not puede_viajar(actual, vecino, cerradas):
                continue
            nuevo_costo = costo_actual + costo_arista
            if nuevo_costo < costos.get(vecino, math.inf):
                costos[vecino] = nuevo_costo
                anterior[vecino] = actual
                heapq.heappush(frontera, (nuevo_costo, vecino))
    return ResultadoRuta([], math.inf, len(explorados), "Dijkstra")

