"""Reproducción del hecho: el catálogo de recursos de fran-miu-micelio
tiene 0 válidos de 23.294 entradas.

Fuente: Jaime393/fran-miu-micelio, nutrientes/catalogo_recursos.json,
cabeza 686627f7 (2026-08-30), 7.128.560 B, blob SHA 60cded701f40.
Descargado y contado por programa 2026-11-09 ~17:11 -05.

El script NUNCA imprime los campos nombre ni valor de las entradas:
solo cuenta. Los valores de las entradas no se leen ni se reproducen.
"""

import hashlib
import json
import sys
import urllib.request
from collections import Counter

URL = ("https://raw.githubusercontent.com/Jaime393/fran-miu-micelio/"
       "686627f74970a9de36efde3ec02fa50a7426ec09/"
       "nutrientes/catalogo_recursos.json")
RUTA_POR_DEFECTO = "/tmp/catalogo_recursos.json"
TAMANO_ESPERADO = 7128560
SHA256_ESPERADO = ("73cb56c873e5bfebe525f1765df8d475412fc5c94c321aa1c"
                   "450a5d63cfc43c3")
TOTAL_ESPERADO = 23294
VALIDOS_ESPERADO = 0
INVALIDOS_ESPERADO = 40
PENDIENTES_ESPERADO = 23254


def sha256_de(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def obtener(ruta):
    """Devuelve la ruta del archivo verificado (descarga si hace falta)."""
    try:
        with open(ruta, "rb") as f:
            tamano = f.seek(0, 2)
        if tamano == TAMANO_ESPERADO and sha256_de(ruta) == SHA256_ESPERADO:
            return ruta, "local verificado"
    except OSError:
        pass
    urllib.request.urlretrieve(URL, ruta)
    return ruta, "descargado"


def contar(path):
    """Cuenta el catálogo. Solo agregados; nunca nombre ni valor."""
    with open(path, encoding="utf-8") as f:
        datos = json.load(f)
    recursos = datos["recursos"]
    por_estado = Counter(r["estado"] for r in recursos)
    ok_falso = sum(1 for r in recursos if r["detalle"].get("ok") is False)
    ok_verdadero = sum(1 for r in recursos if r["detalle"].get("ok") is True)
    return {
        "cabecera_total": datos["total"],
        "cabecera_validos": datos["validos"],
        "cabecera_invalidos": datos["invalidos"],
        "cabecera_pendientes": datos["pendientes"],
        "entradas": len(recursos),
        "por_estado": dict(por_estado),
        "detalle_ok_falso": ok_falso,
        "detalle_ok_verdadero": ok_verdadero,
        "timestamp": datos["timestamp"],
    }


def comprobar(c):
    """Lista de discrepancias; vacía si TODO COINCIDE."""
    fallos = []
    if c["entradas"] != TOTAL_ESPERADO:
        fallos.append(f"entradas {c['entradas']} != {TOTAL_ESPERADO}")
    if c["cabecera_total"] != TOTAL_ESPERADO:
        fallos.append(f"cabecera total {c['cabecera_total']} != {TOTAL_ESPERADO}")
    if c["cabecera_validos"] != VALIDOS_ESPERADO:
        fallos.append(f"cabecera validos {c['cabecera_validos']} != {VALIDOS_ESPERADO}")
    if c["cabecera_invalidos"] != INVALIDOS_ESPERADO:
        fallos.append(f"cabecera invalidos {c['cabecera_invalidos']} != {INVALIDOS_ESPERADO}")
    if c["cabecera_pendientes"] != PENDIENTES_ESPERADO:
        fallos.append(f"cabecera pendientes {c['cabecera_pendientes']} != {PENDIENTES_ESPERADO}")
    suma = (c["cabecera_validos"] + c["cabecera_invalidos"]
            + c["cabecera_pendientes"])
    if suma != TOTAL_ESPERADO:
        fallos.append(f"suma cabecera {suma} != {TOTAL_ESPERADO}")
    if sum(c["por_estado"].values()) != TOTAL_ESPERADO:
        fallos.append("la suma por estado no da el total")
    if "VALIDO" in c["por_estado"]:
        fallos.append(f"hay {c['por_estado']['VALIDO']} entradas VALIDO")
    if c["detalle_ok_verdadero"] != 0:
        fallos.append(f"hay {c['detalle_ok_verdadero']} detalle.ok True")
    if c["detalle_ok_falso"] != TOTAL_ESPERADO:
        fallos.append(f"detalle.ok False {c['detalle_ok_falso']} != {TOTAL_ESPERADO}")
    return fallos


def informe(c):
    lineas = [
        f"timestamp: {c['timestamp']}",
        f"entradas: {c['entradas']}",
        (f"cabecera: total {c['cabecera_total']}, validos "
         f"{c['cabecera_validos']}, invalidos {c['cabecera_invalidos']}, "
         f"pendientes {c['cabecera_pendientes']}"),
        f"por estado: {c['por_estado']}",
        (f"detalle.ok: False {c['detalle_ok_falso']}, "
         f"True {c['detalle_ok_verdadero']}"),
    ]
    return "\n".join(lineas)


def main(argv):
    ruta = argv[1] if len(argv) > 1 else RUTA_POR_DEFECTO
    ruta, origen = obtener(ruta)
    print(f"archivo: {ruta} ({origen})")
    c = contar(ruta)
    print(informe(c))
    fallos = comprobar(c)
    if fallos:
        print("DISCREPANCIAS:")
        for f in fallos:
            print(f"  - {f}")
        return 1
    print("TODO COINCIDE")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
