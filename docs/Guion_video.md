# Guion del video - Actividad 2

Duración objetivo: 7 a 8 minutos. Grabar en 1920 x 1080, cerrar notificaciones y aumentar el tamaño de letra.

## 1. Presentación (0:00-0:35)

**Pantalla:** portada del informe.

“Hola, mi nombre es Nelson Andrés Ramírez Gutiérrez. Presento la Actividad 2 del curso Inteligencia artificial. El proyecto es un sistema basado en reglas que recomienda rutas dentro de un modelo académico simplificado de TransMilenio.”

## 2. Problema y alcance (0:35-1:15)

“El usuario selecciona una estación de origen y otra de destino. El sistema consulta una base de conocimiento, aplica reglas y utiliza búsqueda heurística. Los tiempos y coordenadas son didácticos y no representan la operación en tiempo real.”

## 3. Base de conocimiento (1:15-2:10)

**Pantalla:** `src/base_conocimiento.py`.

“Las estaciones se representan como nodos. Cada registro indica troncal, posición y tipo. Las conexiones son aristas con un costo estimado. La función construir_red convierte los hechos en un grafo no dirigido.”

## 4. Reglas lógicas (2:10-3:10)

**Pantalla:** `src/reglas.py`.

“El motor contiene cinco reglas: estación válida, movimiento permitido, identificación de transbordos, validación de consultas y validación de todos los pasos de una ruta.”

## 5. A* y Dijkstra (3:10-4:20)

**Pantalla:** `src/busqueda.py`.

“A estrella evalúa cada nodo con f de n igual a g de n más h de n. G es el costo acumulado y H la estimación al destino. Dijkstra funciona como referencia para comprobar el costo mínimo.”

## 6. Ejecución (4:20-6:15)

```powershell
python -m src.main
```

Consultar `Portal Norte` a `Portal El Dorado`. Después cerrar `Calle 76` y consultar `Portal Norte` a `Calle 63`. Finalmente intentar `Estacion inventada`.

## 7. Pruebas (6:15-7:10)

```powershell
python -m unittest discover -s tests -v
```

“Las siete pruebas revisan rutas, igualdad entre algoritmos, cierres, ausencia de ruta, datos inválidos y transbordos. Todas deben finalizar con OK.”

## 8. Repositorio y cierre (7:10-7:50)

“El repositorio contiene código, instrucciones, pruebas, informe y guion. En conclusión, reglas y búsqueda heurística permiten explicar las decisiones y adaptar la ruta cuando cambia el estado de una estación.”

