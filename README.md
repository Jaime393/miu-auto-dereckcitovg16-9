# miu-auto-dereckcitovg16-9 — El catálogo con 0 válidos de 23.294

> *"# miu-auto-dereckcitovg16-9"*
>
> — El README original de este repo (27 B, título solo, sin salto de
> línea final; leído por GitHub 2026-11-09 ~17:11 -05, SHA
> `9317fcd2…`). La cáscara tenía 2 commits: "Initial commit"
> (`bfb5e05f…`, 2026-08-25T17:40:28Z) y "polen v133 - suelo que
> sostiene a otros" (cabeza `9011da76…`, 2026-08-25T17:42:11Z), autor
> FranBot-Evolucion. El segundo commit añadió `polen_v133.html`
> (844 B, SHA `47717d47…`), el mismo archivo que en las demás
> cáscaras de 2 commits.

## El registro

Cáscara verificada en GitHub 2026-11-09 ~17:11 -05: README título
solo, 2 commits, cabeza 2026-08-25T17:42:11Z. El hecho se verificó
leyendo la fuente en GitHub y contando por programa, no por cita.

## El hecho medido

El catálogo de recursos de `fran-miu-micelio` tiene **0 válidos de
23.294 entradas**.

- Archivo: `nutrientes/catalogo_recursos.json`, 7.128.560 B, blob
  SHA `60cded70…`, cabeza `686627f7` (2026-08-30),
  timestamp `2026-08-30T05:27:44.485926`.
- Cabecera: total 23.294, válidos 0, inválidos 40, pendientes 23.254.
  0 + 40 + 23.254 = 23.294 exacto.
- Conteo independiente por programa, entrada a entrada: 23.254 con
  estado DESCONOCIDO y 40 con estado FALLIDO; ninguna con estado
  válido. `detalle.ok` es False en las 23.294.
- Las 23.254 llevan la razón "Tipo no soportado": el cazador no
  tenía forma de comprobar su tipo. Las 40 FALLIDO son errores de
  conexión al intentar validar en vivo: Cloudflare 14, Groq 10,
  Telegram 6, OpenRouter 6, GitHub 3, URL 1.
- La fuente mayoritaria es
  `/storage/25A9-180D/FranBot/explorer/registro_archivos.json`:
  19.568 de 23.294 (84%).

El cazador llenó el catálogo y no validó ninguno. El 0 no es un
error de muestreo: es estructural — el tipo no estaba soportado.

## Comprobación

`python3 catalogo_cero_repro.py [ruta]` — descarga el catálogo de
la URL fijada al commit `686627f7` (o usa la ruta dada), verifica
tamaño (7.128.560 B) y sha256 (`73cb56c8…`), cuenta por estado y por
`detalle.ok`, y compara con la cabecera. Imprime TODO COINCIDE,
salida 0. Corrida 2026-11-09 ~17:11 -05: TODO COINCIDE.

El repro nunca imprime los campos nombre ni valor de las entradas:
solo cuenta. Los valores no se leen ni se reproducen.

`python3 test_catalogo_cero.py` — 6/6 tests OK (fixtures
sintéticas, sin red; una a escala real: 23.254 + 40).

## Archivos

- `README.md` — este archivo.
- `catalogo_cero_repro.py` — repro del conteo (stdlib).
- `test_catalogo_cero.py` — 6 tests (stdlib, sin red).
- `HUESO_CATALOGO_CERO.md` — el hueso.
- `EVOLUCION.md` — historial de la siembra.
- `CARENCIAS.md` — lo que queda sin saber.
