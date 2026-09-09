# DESIGN.md — ENAE Executive MBA Landings

Sistema de diseño derivado de las landings de conversión del Executive MBA de ENAE Business School.

---

## 1. Arquitectura del proyecto

```
landings-masters/
├── enae-executive-mba-ceos.html          # Variante para CEOs
├── enae-executive-mba-directivos.html    # Variante para Directivos
├── enae-executive-mba-mandos-intermedios.html  # Variante para Mandos
├── src/
│   ├── css/
│   │   ├── base.css          # Sistema de diseño compartido (incluye fuentes embebidas base64)
│   │   └── style.css         # Overrides por variante: hero, rankings, carrusel, formulario
│   ├── js/
│   │   └── main.js           # Reveal animations, globo 3D, carrusel, radar chart, tracking
│   ├── fonts/                # Fuentes source (TTF/OTF)
│   ├── img/                  # Heros y fotografías
│   └── Rankings/             # SVGs de rankings/acreditaciones
```

**Cada landing es un HTML autocontenido** — no usa framework, bundler ni router. Los tres archivos comparten `base.css`, `style.css` y `main.js`. Las variantes se diferencian por:
- Imagen y gradiente del hero (clase `d-hero--ceo`, etc.)
- Textos, perfil de audiencia y datos de programa
- ID del formulario de Dynamics 365

---

## 2. Paleta de color

### Tokens de marca (`:root`)

| Token | Valor | Uso |
|---|---|---|
| `--enae-granate` | `#a91831` | Color primario, CTAs, acentos, hover states |
| `--enae-granate-oscuro` | `#5e0f1e` | Gradientes oscuros (final CTA, stats) |
| `--enae-negro` | `#202221` | Fondo oscuro, texto principal, botones hover |
| `--enae-carbon` | `#111211` | Fondo más profundo (hero) |
| `--enae-blanco` | `#ffffff` | Fondo claro, texto sobre oscuro |
| `--enae-azul-gris` | `#dee5ec` | Fondo del plan de estudios (curriculum) |
| `--enae-gris-oscuro` | `#404040` | Texto secundario (labels, subtítulos) |
| `--enae-gris-medio` | `#636363` | Texto terciario (placeholders, metadata) |
| `--enae-gris-suave` | `#f4f6f8` | Superficie elevada sobre blanco |
| `--enae-gris-claro` | `#dbdbdb` | Bordes suaves auxiliares |

### Tokens semánticos (light/dark aware)

| Token | Light | Dark |
|---|---|---|
| `--ground` | `#ffffff` | `#202221` |
| `--ink` | `#202221` | `#f5f2ec` |
| `--ink-soft` | `#404040` | `#c9c5bc` |
| `--hair` | `#e7e7e7` | `#2c2a26` |
| `--surface` | `#f4f6f8` | `#191919` |

### Colores funcionales

| Uso | Valor |
|---|---|
| Acento dorado (serif, pills, KPIs) | `#ffd7a0` |
| Texto sobre oscuro | `#F8F9FA` |
| Asterisco obligatorio (formulario) | `#c33400` (Dynamics) / `--enae-granate` (override) |
| Error de validación | `#a80000` |

---

## 3. Tipografía

### Font stacks

| Token | Familia | Peso disponible | Uso |
|---|---|---|---|
| `--font-display` | SFUIDisplay, Arial Black, Impact | 900 (Black), 700 (Bold) | Titulares `.t-bold`, nav, badge |
| `--font-body` | OpenSans, Arial, Helvetica | 300, 700, 800 | Cuerpo, labels, botones, KPIs |
| `--font-serif` | OggText, Georgia, Times New Roman | 400 (Italic) | Subtítulos `.t-serif`, numerales, quotes |

### Escala tipográfica

| Elemento | Font | Size | Weight | Tracking |
|---|---|---|---|---|
| H1 hero `.t-bold` | Display | `clamp(38px, 4.5vw, 65px)` | 900 | `-0.02em` |
| H1 hero `.t-serif` | Serif | `clamp(20px, 2.5vw, 32px)` | 400 italic | `-0.01em` |
| H2 section `.t-bold` | Display | `clamp(30px, 3.8vw, 52px)` | 900 | `-0.02em` |
| H2 section `.t-serif` | Serif | same | 400 italic | `-0.01em` |
| H3 card title | Body | `22px` | 800 | `-0.01em` |
| Body text | Body | `15–17.5px` | 300 | normal |
| Eyebrow | Body | `12px` | 700 | `0.22em` |
| Label (form) | Body | `11px` | 700 | `0.03em` |
| Button | Body | `13.5px` | 700 | `0.02em` |
| Small meta | Body | `12.5px` | 700 | `0.06em` |

### Patrón de título mixto (`.mix`)

Recurso tipográfico de marca: combina `.t-bold` (display, sin serifa, peso 900) + `.t-serif` (serif itálica, peso 400) en una misma composición. Se usa en hero, secciones y CTA final. Line-height: `1.02`, letter-spacing: `-0.02em`, `text-wrap: balance`.

---

## 4. Layout y espaciado

### Grid principal

| Token | Valor |
|---|---|
| `--page-max` | `1240px` |
| `--gutter` | `clamp(20px, 4vw, 56px)` |

**Contenedor**: `.wrap` — `max-width: var(--page-max); margin-inline: auto; padding-inline: var(--gutter)`.

### Secciones

Padding vertical uniforme: `clamp(60px, 8vw, 110px)`.

### Grids por componente

| Componente | Columnas desktop | Breakpoint |
|---|---|---|
| Hero (d-hero-inner) | `flex: 1.25fr + 0.85fr` | ≤991px → stack |
| Rankings | `repeat(4, 1fr)` | ≤991px → 2col, ≤767px → 1col |
| Perfil cards | `repeat(4, 1fr)` | ≤800px → 1col |
| Value trio cards | `repeat(3, 1fr)` | ≤767px → 1col |
| Stats KPIs | `repeat(4, 1fr)` | ≤800px → 2col |
| Modalidades | `repeat(3, 1fr)` | ≤900px → 1col |
| Curriculum | `repeat(2, 1fr)` | ≤800px → 1col |
| Final CTA | `1fr 1.15fr` | ≤991px → 1col |
| Footer | `1.4fr 1fr 1fr` | ≤800px → 1col |

---

## 5. Componentes

### 5.1 Navegación (`.nav`)

Sticky top, backdrop-filter blur, borde inferior `--hair`. Logo a la izquierda (70px), links al centro (hidden < 960px), CTA button a la derecha.

### 5.2 Botón (`.btn`)

```
padding: 12px 22px
border-radius: 2px (sharp, editorial)
font: 13.5px/700 OpenSans, uppercase, 0.02em
border: 1.5px solid
transition: background .2s, transform .15s
```

Variantes: default (granate), `.ghost` (transparente), `.dark` (negro). Hover: negro + translateY(-1px). Flecha `→` con `translateX(3px)` al hover.

### 5.3 Hero (`.d-hero`)

Background-image con overlay de gradiente (`:before`). Pattern bars decorativas (spans con `skewX(-14deg)`). Globo 3D interactivo dibujado en `<canvas>` (120 nodos, edges, pulses). Orbit concept pills flotantes (`@keyframes float`).

### 5.4 Carrusel de metodología

Cards oscuras (gradiente 150deg, 3 stops) con hover lift (-12px), glow radial, iconos con backdrop-filter. Scroll horizontal con snap, drag & drop, navegación por teclado. Gradient mask en los bordes del viewport.

### 5.5 Formulario de Dynamics 365 (`.d-form-container`)

Widget embebido de Microsoft Dynamics 365 Customer Insights. Se carga dinámicamente via `FormLoader.bundle.js`. Los estilos nativos del widget se sobreescriben con selectores de alta especificidad + `!important` dentro de `.d-form-container`.

**Grid interno**: `.columnContainer` forzado a `display: grid`. Una columna por defecto; dos columnas cuando el contenedor mide ≥400px (container query, no media query).

**Campos que ocupan ancho completo** (grid-column 1/-1): textarea, consent block, botón de envío, bloque de texto legal.

**Labels**: 11px, uppercase, 700, `--enae-gris-oscuro`.  
**Inputs**: border `1.5px solid #b7bbc0`, border-radius 8px, padding `9px 12px`, focus ring granate.  
**Botón submit**: full-width, granate, con flecha `→`, hover a negro.

### 5.6 Tarjeta de ranking (`.d-ranking-item`)

Borde `--hair`, fondo `--ground`, hover con lift y borde granate suave. Logo/imagen 100px height + label + valor.

### 5.7 Value cards (`.value-card`)

Imagen top (220px, object-fit cover, zoom al hover), contenido abajo con numeral serif, título y descripción.

### 5.8 Claustro banner

Grid 2 columnas (1fr + 1.25fr). Imagen a la izquierda, contenido + facts a la derecha. Facts separados por border-top granate.

### 5.9 FAQ (`.qa`)

Acordeones nativos con `<details>/<summary>`. Indicador `+`/`−` en granate. Texto de respuesta en 15.5px weight 300.

---

## 6. Patrones visuales

### Fondos sección

| Sección | Fondo |
|---|---|
| Hero | Imagen + gradiente overlay (negro→granate) |
| Rankings, Perfil, FAQ | `--ground` (blanco) |
| Curriculum | `--enae-azul-gris` (#dee5ec) |
| Stats, Steps, Final CTA | Gradiente granate→negro con radial highlight dorado |
| Método/Claustro | Tarjeta negra sobre sección clara |

### Pattern bars

Rectángulos semitransparentes rotados (`skewX(-14deg)`) superpuestos en secciones oscuras. Crean textura de "velocidad" editorial sin imágenes.

### Watermarks ENAE (`.enae-wm`)

SVG de la "E" corporativa como `::after` pseudo-element, escala grande (400–600px), rotado, opacidad .03–.05. Posiciones variables por sección.

### Gradientes recurrentes

- Hero: `linear-gradient(135deg, negro 0%, gris 50%, granate 78%)`
- Stats/Final: `linear-gradient(150deg, granate 0%, granate-oscuro 60%, negro 100%)` + `radial-gradient dorado`

---

## 7. Interacciones y animaciones

### Reveal on scroll

`IntersectionObserver` con threshold 0.1, rootMargin `-40px`. Elementos `.reveal` arrancan con `opacity: 0; translateY(18px)` y animan a visible con `cubic-bezier(.22,1,.36,1)` en 0.7s. Delays escalonados: `.delay-1` (0.15s), `.delay-2` (0.3s), `.delay-3` (0.45s).

### Hover micro-interactions

- Cards: `translateY(-2px to -12px)`, border-color transition, box-shadow
- Botones: `translateY(-1px)`, flecha `translateX(3px)`
- Carrusel cards: glow scale, icon background shift, number color change to dorado
- Images en value cards: `scale(1.05)` con cubic-bezier

### Globo 3D (Canvas)

120 nodos distribuidos por Fibonacci sphere, edges bajo distancia 0.55, 12 pulsos luminosos. Rotación automática + drag interactivo. Se pausa cuando está fuera del viewport.

### Floating CTA

Fixed bottom-right, aparece/desaparece según visibilidad del hero y la sección final (IntersectionObserver). Badge "Plazas limitadas" + botón con shadow granate.

---

## 8. Responsive

### Breakpoints

| Breakpoint | Uso |
|---|---|
| `960px` | Nav links visible, hero 2-col, claustro 2-col |
| `991px` | Rankings 2-col, final CTA stack |
| `900px` | Modalidades stack, floating CTA resize |
| `800px` | Perfil/Stats/Curriculum/Footer a 1 col |
| `767px` | Rankings 1-col, value trio 1-col, form padding reduced |
| `680px` | Carrusel cards full width |

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  * { transition: none !important; animation: none !important }
  html { scroll-behavior: auto }
}
```

El globo 3D también detecta esta media query y se desactiva.

---

## 9. Formulario embebido — Notas técnicas

El formulario de Dynamics 365 trae sus propios estilos inline y en `<style>` embebido dentro del HTML del widget. Los overrides en `style.css` necesitan:

1. **`!important`** en padding, display, width de los bloques de campo — el widget aplica inline styles.
2. **Container queries** (`container-type: inline-size`) en `.d-form-container` para decidir 1 vs 2 columnas por ancho real del contenedor, no del viewport.
3. **`transform: none !important`** en `.d-form-container.reveal` — sin esto, el dropdown de jQuery UI Autocomplete (lookup fields) se posiciona relativo al contenedor transformado en vez del viewport.
4. El script `FormLoader.bundle.js` carga el form asíncronamente; solo funciona en el dominio de producción (CORS).

---

## 10. Tracking y conversión

- Evento GTM `master_solicitud_informacion` disparado en `d365mkt-afterformsubmit`.
- Deduplicación por `sessionStorage` con key por programa.
- Campos ocultos para UTMs de Google (gclid, wbraid, gbraid, campaign, source, medium, content, userId) y Facebook (ad_id, ad_name, adset_id, campaign_id, platform, retailer_item_id).
- Campos de fingerprint: browser, OS, city (IP), timezone, URL origen.
- `event_id` generado con `crypto.randomUUID()` (fallback timestamp+random).

---

## 11. Accesibilidad

- `::selection` con granate + blanco.
- `:focus-visible` con outline granate 2px, offset 3px.
- `prefers-reduced-motion` respetado globalmente.
- Nav links con underline animado (decorativo, no funcional).
- FAQ con `<details>/<summary>` nativo (keyboard-accessible).
- Logo con `aria-hidden="true"` y `aria-label` en el enlace.
- Formulario con labels explícitos, asteriscos de obligatoriedad.

---

## 12. Dependencias externas

| Recurso | Origen | Uso |
|---|---|---|
| Chart.js 4.4.1 | cdn.jsdelivr.net | Radar chart de competencias |
| FormLoader.bundle.js | formui-usa1.mkt.dynamics.com | Carga del formulario Dynamics 365 |
| YouTube embed | youtube.com | Video testimonial aleatorio |

No hay frameworks CSS, no hay React/Vue/Angular, no hay build step. HTML + CSS + vanilla JS.
