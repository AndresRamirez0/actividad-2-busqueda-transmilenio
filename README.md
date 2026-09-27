# Sistema inteligente de rutas de TransMilenio

Proyecto académico de la Actividad 2 del curso Inteligencia artificial. El sistema representa una red simplificada de TransMilenio mediante una base de conocimiento, aplica reglas lógicas y utiliza el algoritmo A* para recomendar una ruta de costo mínimo.

> **Alcance:** los tiempos, coordenadas y conexiones forman un modelo didáctico. No sustituyen la información oficial ni describen el estado de la operación en tiempo real.

## Funcionalidades

- Base de conocimiento de 25 estaciones, conexiones, costos y tipos de estación.
- Cinco reglas para validar estaciones, movimientos, transbordos, consultas y rutas.
- Búsqueda heurística A* y comparación con Dijkstra.
- Simulación de cierres, rutas alternativas y datos inválidos.
- Siete pruebas automatizadas.

## Requisitos y ejecución

Se requiere Python 3.10 o posterior. El programa y las pruebas no necesitan paquetes externos.

```powershell
python -m src.main
python -m unittest discover -s tests -v
```

Las estaciones pueden seleccionarse por el número mostrado en pantalla o por su
nombre. Los nombres no distinguen entre mayúsculas y minúsculas.

## Estructura

```text
src/                         Código fuente
tests/test_sistema.py        Pruebas automatizadas
docs/                        Informe y guion del video
entrega/                     PDF final con enlaces
```

## Modelo de conocimiento

El grafo es no dirigido: las estaciones son nodos y las conexiones son aristas con un costo estimado en minutos. Las reglas determinan si una estación está habilitada, si un movimiento es posible, si un nodo es de transbordo, si la consulta es válida y si todos los pasos de una ruta son legales.

A* ordena los nodos según `f(n) = g(n) + h(n)`: `g(n)` es el costo acumulado y `h(n)` es una distancia euclidiana admisible entre posiciones didácticas. Dijkstra sirve como referencia sin heurística.

## Autor

Nelson Andrés Ramírez Gutiérrez  
Corporación Universitaria Iberoamericana  
Curso: Inteligencia artificial - 24082026_C1_202634  
Docente: Sandra Bautista  
Bogotá, 2026

