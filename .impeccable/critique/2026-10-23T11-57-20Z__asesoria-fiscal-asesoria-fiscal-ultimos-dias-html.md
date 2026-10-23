---
target: "landing asesoria fiscal: sintomas de uso de IA"
total_score: 17
max_score: 24
na_heuristics: 5,7,9,10
p0_count: 0
p1_count: 3
target_identity: "file:/Users/jesussanchez/Documents/GitHub/landings-masters/Asesoria-fiscal/asesoria-fiscal-ultimos-dias.html"
target_fingerprint: "sha256:7d81c1e9c2869d95683f79962728e451b1add2bcb0fa496ad93c4cfdfd8e44f5"
target_path: /Users/jesussanchez/Documents/GitHub/landings-masters/Asesoria-fiscal/asesoria-fiscal-ultimos-dias.html
timestamp: 2026-10-23T11-57-20Z
slug: asesoria-fiscal-asesoria-fiscal-ultimos-dias-html
---
⚠️ DEGRADED: single-context (política de la sesión: no se lanzan sub-agentes sin petición explícita; la revisión de diseño se hizo antes de ver el detector)

# Crítica: asesoria-fiscal-ultimos-dias.html · síntomas de uso de IA

## Design Health Score

| # | Heurística | Puntuación | Problema clave |
|---|---|---|---|
| 1 | Visibilidad del estado | 3 | Pausa del carrusel y fachada del vídeo bien; el formulario no se pudo evaluar en local |
| 2 | Coincidencia con el mundo real | 3 | Lenguaje claro; el eslogan abstracto sustituye a datos concretos (precio, duración total) |
| 3 | Control y libertad | 3 | Carrusel pausable, acordeones; el desplazamiento automático sigue arrancando solo |
| 4 | Consistencia y estándares | 3 | Nueve radios de esquina distintos; tratamientos mixtos de etiquetas |
| 5 | Prevención de errores | n/a | El formulario es de Dynamics y no carga en local |
| 6 | Reconocer en vez de recordar | 3 | Navegación y CTA presentes en cada tramo |
| 7 | Flexibilidad y eficiencia | n/a | Superficie de Persuadir |
| 8 | Estética y diseño minimalista | 2 | 57 microetiquetas, 13 formas decorativas, mensaje repetido |
| 9 | Recuperación de errores | n/a | Depende del formulario externo |
| 10 | Ayuda y documentación | n/a | Superficie de Persuadir |
| **Total** | | **17/24 (71%)** | **Bueno, por poco** |

## Veredicto de especificidad de diseño

**Evaluación del LLM (antes de ver el detector).** La marca y los datos están anclados al producto: la pareja SF Display Black + Ogg Text, el granate ENAE, los inspectores de la AEAT, las firmas de Murcia, el horario de lunes y martes. Pero la composición y la voz son intercambiables entre categorías: cambia el logo y los sustantivos y vale para cualquier máster o bootcamp. La estructura es la de siempre: chip → titular → párrafo → dos botones → fila de datos → tarjeta flotante con "tres razones"; banda de 4 cifras; trío de tarjetas; "qué pasa después" en 3 pasos; acordeón. Los 7 titulares usan el mismo compás: afirmación + contraste.

**Escaneo determinista.** 52 hallazgos en el código y 51 en el navegador, de 11 reglas distintas. 27 son falsos positivos (14 "bajo contraste" sobre fondos oscuros que el detector da por blancos y 13 "padding ajustado" en contenedores cuyo margen lo da un `.wrap` interior). Reales: 25, de los que 21 son de "slop". El detector confirmó mis hallazgos de etiquetas, filo lateral, punto pulsante y halos; yo detecté lo que él no ve (fórmula del copy, tríadas, baldosas con icono, banda de cifras, formas decorativas, imagen).

**Superposición visual.** Inyectada en la pestaña del navegador y confirmada por consola; el servidor del detector ya está parado.

## Catálogo de síntomas (lo que se lee como "hecho por IA")

| # | Síntoma | Evidencia | Origen | Gravedad |
|---|---|---|---|---|
| 1 | Fórmula de titular "afirmación. Contraste." | 7 titulares: "Del aula al despacho. Sin tener que buscarlas solo." · "Tus profesores no explican la fiscalidad. La ejercen cada día." · "Nuestros alumnos. Ya lo aplican en su trabajo."… | Copy mío | P1 |
| 2 | Tríadas y eslóganes huecos | "Acceso / Profesores / 95%", 3 tarjetas de formato, 3 pasos finales, "Tu carrera en fiscalidad empieza aquí" | Copy mío | P1 |
| 3 | Mismo par negrita + serif cursiva en todo | 12 de 12 titulares mixtos | Plantilla ENAE (recurso de marca) | P2 |
| 4 | Microetiquetas en mayúsculas espaciadas | 57; kickers numerados 01/02/03; chip sobre el h1 | Plantilla + mío (numeración) | P2 |
| 5 | Baldosa con icono + título + descripción | 3 en la tarjeta del hero, 3 círculos de check/número en el CTA | Plantilla + mío | P2 |
| 6 | Banda de 4 cifras con pie en cursiva | 95% · 91% · +500 · 36ª | Plantilla | P2 |
| 7 | Formas oblicuas translúcidas | 13 `.pattern span` en secciones oscuras | Plantilla | P2 |
| 8 | Filo de color sobre esquinas redondeadas | `border-top: 2px` sobre radio de 10 px ×14 (tarjetas del claustro) | Mío | P2 |
| 9 | Aviso con barra lateral | "Incluye… Inteligencia Artificial" con `border-left: 3px` | Mío | P2 |
| 10 | Punto pulsante "en vivo" en la urgencia | `.countdown-pill .live`, animación infinita, sin dato en vivo | Mío | P2 |
| 11 | Halos y sombras de "efecto premium" | resplandor `#ffd7a0` al 10% y 14%; borde de 1 px con sombra de 60 px (×2) | Plantilla + mío | P3 |
| 12 | Foto del hero con aspecto generado | iluminación de estudio, viñeta fuerte, sin lugar reconocible | Imagen de la plantilla | P1 |
| 13 | Infografía isométrica "arquitectónica" | Género muy reconocible; metáfora de camino genérica | Mío | P2 |
| 14 | Urgencia sin dato | "Últimos días" sin fecha de cierre ni plazas | Petición del cliente | P2 |

Casi la mitad de los síntomas son tics míos: se introdujeron en esta sesión al escribir el copy y las piezas nuevas, no vienen de la plantilla de ENAE.

## Impresión general

La landing es sólida en contenido y datos reales, pero suena y se ve como una plantilla bien ejecutada. La mayor oportunidad es **la voz**: sustituir las frases de efecto por hechos con nombre propio.

## Qué funciona
- **Datos verificables y concretos:** inspectores de Hacienda, Garrigues, Grant Thornton, horario de lunes y martes, 95% con fuente oficial. Es lo menos genérico de la página.
- **Marca reconocible:** Ogg Text ExtraBold Italic junto a SF Display Black da carácter propio y no es una tipografía por defecto.
- **Retratos reales y alineados**, y los logos de las firmas: prueba social auténtica.

## Problemas prioritarios

**[P1] La voz del copy delata el origen.** Siete titulares con el mismo compás, tríadas por todas partes y eslóganes que valdrían para cualquier máster.
- *Por qué importa:* un lector escéptico (el público de fiscalidad lo es) desconfía de la fórmula y deja de leer los titulares.
- *Arreglo:* titulares con un hecho: "Joaquín Molina, jefe de Gestión Tributaria en la AEAT Murcia, da tus clases de procedimientos". Alternar la longitud y quitar el contraste forzado.
- *Comando:* `/impeccable clarify`.

**[P1] La maqueta es un molde.** Hero de plantilla, banda de cifras, trío de tarjetas, pasos, acordeón, 13 formas decorativas y un punto pulsante que no significa nada.
- *Arreglo:* eliminar lo que no carga significado (formas, punto pulsante, halos) y dar un único momento memorable a la pieza que sí es de este máster (la lámina del recorrido).
- *Comando:* `/impeccable distill`.

**[P1] La imagen principal parece generada.** La foto del hero tiene iluminación de estudio, viñeta y ningún lugar reconocible.
- *Arreglo:* una foto real de ENAE (campus de Espinardo, un aula, una sesión con los inspectores). Es lo que más sube la confianza.
- *Comando:* `/impeccable shape` para decidir las fotos y el mundo visual.

**[P2] Tics de CSS que el detector reconoce.** 14 filos de color sobre esquinas redondeadas, un aviso con barra lateral, 3 etiquetas numeradas sobre titulares y un punto pulsante.
- *Arreglo:* quitar el `border-top` de las leyendas del claustro, convertir el aviso de IA en una línea sin barra, quitar la numeración 01/02/03 de las etiquetas y dejar el punto estático.
- *Comando:* `/impeccable quieter`.

**[P2] Pequeños fallos tipográficos.** El párrafo del hero hereda un interletrado de -0,06em del titular; cuatro bloques con interlineado de 1,25–1,30; y los h3/h4 a 16 px quedaron del mismo tamaño que el cuerpo.
- *Comando:* `/impeccable typeset`.

## Red flags por perfil

**Jordan (primera visita):** lee 7 titulares seguidos con la misma cadencia y no encuentra cuánto cuesta ni cuántos meses dura; la FAQ solo dice "contacta con nosotros".

**Riley (escéptico):** "Acceso garantizado" se matiza en letra pequeña (depende de que la empresa acepte), el 95% no dice año ni muestra, "Últimos días" no da fecha de cierre ni plazas, y los testimonios no llevan foto.

**Casey (móvil):** la lámina, la pieza más distintiva, se convierte en una lista sin ilustración; hay barra fija inferior más barra superior; el carrusel arranca solo.

## Observaciones menores
- Tres textos largos en mayúsculas (33-46 caracteres) y etiquetas del dibujo de 7,7 px de cuerpo.
- Una línea de 155 caracteres (`+8 profesionales más…`).
- Dos contenedores recortan hijos posicionados (`overflow:hidden`), por diseño.
- Los 27 falsos positivos del detector (contraste y padding) no requieren acción.

## Preguntas
- ¿Qué diría esta página si no pudiera usar ningún adjetivo ni contraste, solo nombres, cifras y lugares?
- ¿Y si el hero fuera la foto real de un aula en Espinardo y el titular, el nombre del profesor que da la primera clase?
- ¿Es un tono tan "premium" lo que quiere un futuro asesor fiscal, o prefiere sentir que alguien lo conoce?
