import math
import unittest

from src.busqueda import buscar_a_estrella, buscar_dijkstra
from src.reglas import es_transbordo, ruta_valida


class PruebasSistemaRutas(unittest.TestCase):
    def test_ruta_directa(self):
        resultado = buscar_a_estrella("Portal Norte", "Calle 100")
        self.assertEqual(resultado.costo, 22)
        self.assertTrue(ruta_valida(resultado.ruta))

    def test_a_estrella_coincide_con_dijkstra(self):
        a_estrella = buscar_a_estrella("Portal Norte", "Portal El Dorado")
        dijkstra = buscar_dijkstra("Portal Norte", "Portal El Dorado")
        self.assertEqual(a_estrella.costo, dijkstra.costo)
        self.assertEqual(a_estrella.ruta, dijkstra.ruta)

    def test_cierre_utiliza_enlace_alternativo(self):
        resultado = buscar_a_estrella("Portal Norte", "Calle 63", {"Calle 76"})
        self.assertNotIn("Calle 76", resultado.ruta)
        self.assertTrue(ruta_valida(resultado.ruta, {"Calle 76"}))

    def test_cierre_interrumpe_ruta(self):
        resultado = buscar_a_estrella("Portal Norte", "Portal El Dorado", {"Calle 26"})
        self.assertEqual(resultado.ruta, [])
        self.assertTrue(math.isinf(resultado.costo))

    def test_estacion_inexistente(self):
        with self.assertRaisesRegex(ValueError, "no existe"):
            buscar_a_estrella("Estacion inventada", "Calle 100")

    def test_mismo_origen_y_destino(self):
        with self.assertRaisesRegex(ValueError, "diferentes"):
            buscar_a_estrella("Calle 100", "Calle 100")

    def test_regla_transbordo(self):
        self.assertTrue(es_transbordo("Calle 26"))
        self.assertFalse(es_transbordo("Marly"))


if __name__ == "__main__":
    unittest.main()

