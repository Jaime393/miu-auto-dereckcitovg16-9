"""Tests del repro del catálogo 0/23.294. Solo stdlib, sin red.

Las fixtures son sintéticas, con el mismo esquema del catálogo real
(total, validos, invalidos, pendientes, recursos con estado y
detalle.ok). Ninguna fixture contiene valores reales del catálogo.
"""

import io
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import catalogo_cero_repro as repro


def entrada(estado, ok=False):
    return {"nombre": "N", "valor": "V", "tipo": "generic",
            "fuente": "F", "estado": estado,
            "detalle": {"ok": ok, "razon": "R"}}


def catalogo(total, validos, invalidos, pendientes, recursos):
    return {"timestamp": "2026-08-30T05:27:44.485926",
            "total": total, "validos": validos,
            "invalidos": invalidos, "pendientes": pendientes,
            "recursos": recursos}


def escribir(datos):
    f = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
    json.dump(datos, f)
    f.close()
    return f.name


class TestContar(unittest.TestCase):
    def test_fixture_realista_cero_validos(self):
        # Fixture a escala real: 23.254 DESCONOCIDO + 40 FALLIDO.
        recursos = ([entrada("DESCONOCIDO") for _ in range(23254)]
                    + [entrada("FALLIDO") for _ in range(40)])
        ruta = escribir(catalogo(23294, 0, 40, 23254, recursos))
        try:
            c = repro.contar(ruta)
        finally:
            os.unlink(ruta)
        self.assertEqual(c["entradas"], 23294)
        self.assertEqual(c["por_estado"], {"DESCONOCIDO": 23254,
                                           "FALLIDO": 40})
        self.assertEqual(c["detalle_ok_falso"], 23294)
        self.assertEqual(c["detalle_ok_verdadero"], 0)
        self.assertEqual(repro.comprobar(c), [])

    def test_detecta_un_valido(self):
        recursos = ([entrada("DESCONOCIDO") for _ in range(4)]
                    + [entrada("VALIDO", ok=True)])
        ruta = escribir(catalogo(5, 1, 0, 4, recursos))
        try:
            c = repro.contar(ruta)
        finally:
            os.unlink(ruta)
        fallos = repro.comprobar(c)
        self.assertTrue(any("VALIDO" in f for f in fallos))
        self.assertTrue(any("ok True" in f for f in fallos))

    def test_detecta_aritmetica_rota(self):
        recursos = [entrada("DESCONOCIDO") for _ in range(5)]
        ruta = escribir(catalogo(6, 0, 0, 5, recursos))
        try:
            c = repro.contar(ruta)
        finally:
            os.unlink(ruta)
        fallos = repro.comprobar(c)
        self.assertTrue(any("entradas 5 != 23294" in f for f in fallos))

    def test_constantes_fijadas_son_las_verificadas(self):
        self.assertIn("686627f7", repro.URL)
        self.assertIn("fran-miu-micelio", repro.URL)
        self.assertEqual(repro.TAMANO_ESPERADO, 7128560)
        self.assertEqual(
            repro.SHA256_ESPERADO,
            "73cb56c873e5bfebe525f1765df8d475412fc5c94c321aa1c"
            "450a5d63cfc43c3")
        self.assertEqual(
            (repro.TOTAL_ESPERADO, repro.VALIDOS_ESPERADO,
             repro.INVALIDOS_ESPERADO, repro.PENDIENTES_ESPERADO),
            (23294, 0, 40, 23254))

    def test_el_informe_nunca_muestra_nombre_ni_valor(self):
        recursos = [entrada("DESCONOCIDO")]
        recursos[0]["nombre"] = "NOMBRE_SECRETO_MARCADOR"
        recursos[0]["valor"] = "VALOR_SECRETO_MARCADOR"
        ruta = escribir(catalogo(1, 0, 0, 1, recursos))
        try:
            c = repro.contar(ruta)
            texto = repro.informe(c)
        finally:
            os.unlink(ruta)
        self.assertNotIn("NOMBRE_SECRETO_MARCADOR", texto)
        self.assertNotIn("VALOR_SECRETO_MARCADOR", texto)

    def test_comprobar_no_acepta_ok_verdadero(self):
        recursos = [entrada("DESCONOCIDO", ok=True)]
        ruta = escribir(catalogo(1, 0, 0, 1, recursos))
        try:
            c = repro.contar(ruta)
        finally:
            os.unlink(ruta)
        self.assertTrue(any("ok True" in f for f in repro.comprobar(c)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
