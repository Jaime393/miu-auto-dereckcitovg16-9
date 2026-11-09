# CARENCIAS — miu-auto-dereckcitovg16-9

Lo que queda sin saber, con dónde se buscó y fecha. Nada de esto se
afirma en los demás archivos de la semilla.

1. **Qué hace válido a un recurso.** NO SÉ qué comprobación, ni qué
   criterio, convierte una entrada en válida. El catálogo no trae
   su definición: solo trae el contador en 0. Buscado en el archivo
   mismo y en `~/workspace/mineria/fran-miu-micelio/` (2026-11-09).
2. **Qué tipos no estaban soportados.** NO SÉ cuáles son los tipos
   de las 23.254 entradas DESCONOCIDO más allá del agregado: el
   tipo mayoritario es "generic" (23.202 de 23.294). Qué significa
   "generic" y por qué no se soporta, no está escrito en el archivo.
3. **Si el cazador volvió a correr después del 2026-08-30.** NO SÉ:
   el archivo tiene un solo timestamp (2026-08-30T05:27:44Z) y el
   repo murió ese día. Ninguna segunda versión en el árbol.
4. **Si las 40 FALLIDO validarían con red.** NO SÉ: sus razones son
   errores de conexión (Cloudflare 14, Groq 10, Telegram 6,
   OpenRouter 6, GitHub 3, URL 1). Con red podrían validar o no;
   el archivo no lo dice.
5. **Para qué era el catálogo.** NO SÉ qué consumidor lo leía: no
   hay código en el repo que lo importe (la minería de la ola 5 no
   encontró lector; no se re-verificó aquí).
6. **Si alguna entrada es una credencial viva.** NO SÉ, y no se
   comprobó: los campos nombre y valor de las entradas nunca se
   leyeron más allá del esquema. No se reproduce ningún valor.
