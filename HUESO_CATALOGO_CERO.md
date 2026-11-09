# HUESO — El catálogo con 0 válidos de 23.294

El cazador de `fran-miu-micelio` recorrió la tablet y guardó 23.294
recursos en `nutrientes/catalogo_recursos.json` (7.128.560 B,
2026-08-30T05:27:44Z). Validó **cero**.

No es que fallara el 100%: es que no validó ninguno. Las 23.254
entradas pendientes llevan la razón "Tipo no soportado" — el cazador
no tenía forma de comprobar su tipo. Las 40 restantes sí se intentaron
en vivo y fallaron por conexión (Cloudflare 14, Groq 10, Telegram 6,
OpenRouter 6, GitHub 3, URL 1). `detalle.ok` es False en las 23.294.

El hueso: **un catálogo no es un inventario comprobado por tener
muchas filas.** 23.294 filas con 0 válidos valen menos que 1 fila
comprobada. El número grande es el señuelo; el cero es el dato.

La lección viaja: cada vez que un repo anuncie un conteo ("221",
"257", "258", "220" — la serie TN-14), la pregunta no es cuántas
filas dice, sino cuántas pasaron la comprobación. Aquí la
respuesta fue cero, y estaba escrita en la propia cabecera del
archivo (total 23.294, válidos 0, inválidos 40, pendientes 23.254).

Fuente: `Jaime393/fran-miu-micelio`,
`nutrientes/catalogo_recursos.json`, cabeza `686627f7`, contado por
programa 2026-11-09 ~17:11 -05. Verificado en
`~/workspace/mineria/fran-miu-micelio/CONTENIDO.md` §5.
