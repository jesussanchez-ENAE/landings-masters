import re

with open('enae-executive-mba-directivos.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract parts
head_end = html.find('</nav>') + len('</nav>')
footer_start = html.find('<footer>')

head_part = html[:head_end]
footer_part = html[footer_start:]
form_cta_part_match = re.search(r'(<section class="final enae-wm enae-wm--final" id="solicitar">.*?</section>)', html, re.DOTALL)
form_cta_part = form_cta_part_match.group(1) if form_cta_part_match else ''

# Build new content
new_content = """
<!-- CUSTOM CSS DIRECTIVOS -->
  <link rel="stylesheet" href="./src/css/style.css">
  <style>
    .split-section { display: flex; flex-wrap: wrap; gap: 4rem; padding: 6rem 0; align-items: center; }
    .split-text { flex: 1; min-width: 300px; }
    .split-visual { flex: 1; min-width: 300px; background: var(--surface); padding: 3rem; border-radius: 12px; }
    
    .table-cambio { width: 100%; border-collapse: collapse; margin-top: 2rem; }
    .table-cambio th, .table-cambio td { padding: 1rem; border-bottom: 1px solid rgba(0,0,0,0.1); text-align: left; }
    .table-cambio th { font-family: var(--font-serif); font-size: 1.2rem; color: var(--enae-granate); border-bottom: 2px solid var(--ink); }
    .table-cambio td:first-child { color: var(--text); opacity: 0.7; }
    .table-cambio td:last-child { font-weight: 600; color: var(--ink); }

    .develop-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-top: 3rem; }
    .develop-card { background: #fff; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); border-top: 4px solid var(--enae-granate); }
    .develop-card h4 { font-family: var(--font-serif); font-size: 1.4rem; color: var(--ink); margin-bottom: 1rem; }
  </style>
<!-- END CUSTOM CSS DIRECTIVOS -->

<!-- HERO -->
<header class="hero d-hero enae-wm enae-wm--hero" style="background: url('./src/img/hero_executive_mba_mandos_intermedios.jpg') center/cover no-repeat; position: relative;">
  <div class="pattern" aria-hidden="true">
    <span class="b1"></span><span class="b2"></span><span class="b3"></span><span class="b4"></span><span class="b5"></span>
  </div>
  <div class="wrap d-hero-inner reveal">
    <div class="d-hero-content" style="flex: 1; max-width: 600px;">
      <h1 class="hero-title mix">
        <span class="t-bold" style="display:block; font-size: clamp(28px, 4vw, 42px); line-height: 1.1; margin-bottom: 0.5rem;">Sabes hacer.</span>
        <span class="t-serif" style="display:block; font-size: clamp(32px, 5vw, 54px); line-height: 1.1; margin-bottom: 1.5rem; color: #ffd7a0;">Ahora aprende a dirigir.</span>
        <span class="t-light" style="font-size: clamp(20px, 2.5vw, 28px); font-weight: 500; color: #fff; margin-bottom: 1rem; display:block;">Da el salto de especialista a directivo.</span>
      </h1>
      <p style="color: rgba(255,255,255,0.9); font-size: 1.1rem; line-height: 1.6; margin-bottom: 2rem;">
        <strong>Executive MBA · ENAE</strong><br><br>
        Un programa para profesionales que quieren ampliar su visión de negocio, asumir nuevas responsabilidades y prepararse para su siguiente paso profesional.
      </p>
      <div class="cta-row">
        <a href="#solicitar" class="btn">Solicita información <span class="arrow">&rarr;</span></a>
      </div>
    </div>
  </div>
</header>

<!-- BLOQUE 1: EL MOMENTO PROFESIONAL -->
<section class="enae-wm" style="padding: 6rem 0; background: var(--enae-blanco);">
  <div class="wrap" style="max-width: 800px; text-align: center;">
    <h2 class="mix reveal" style="margin-bottom: 2rem;">
      <span class="t-bold">Tu experiencia te ha traído hasta aquí.</span><br>
      <span class="t-serif" style="color: var(--enae-granate);">Pero el siguiente nivel exige algo diferente.</span>
    </h2>
    <p class="reveal delay-1" style="font-size: 1.25rem; color: var(--text); line-height: 1.6; margin-bottom: 2rem;">
      Has conseguido resultados. Has ganado responsabilidades. Dominas tu área.
    </p>
    <p class="reveal delay-2" style="font-size: 1.1rem; color: var(--text); line-height: 1.6;">
      Pero dirigir una empresa no consiste únicamente en ser el mejor en tu función.<br><br>
      <strong>Implica entender cómo funciona el negocio en su conjunto, tomar decisiones con visión estratégica y liderar más allá de tu área.</strong>
    </p>
  </div>
</section>

<!-- BLOQUE 2: EL PROBLEMA -->
<section class="enae-wm enae-wm--problema" style="background: var(--ink); color: #fff; padding: 6rem 0; position: relative; overflow: hidden;">
  <div class="pattern" aria-hidden="true">
    <span class="b1"></span><span class="b2"></span><span class="b3"></span>
  </div>
  <div class="wrap split-section reveal" style="padding: 0; position: relative; z-index: 2;">
    <div class="split-text">
      <h2 class="mix" style="margin-bottom: 1.5rem; color: #fff;">
        <span class="t-bold">Ser especialista te hizo crecer.</span><br>
        <span class="t-serif" style="color: #ffd7a0;">No dejes que te limite.</span>
      </h2>
      <p style="font-size: 1.1rem; color: rgba(255,255,255,0.8); margin-bottom: 1.5rem;">
        Marketing, finanzas, operaciones, RRHH, ventas… Tu especialización es tu fortaleza.
      </p>
      <p style="font-size: 1.1rem; color: #fff; margin-bottom: 1.5rem; font-weight: 500;">
        Pero cuando llega el momento de asumir una posición directiva, necesitas comprender también estrategia, finanzas, operaciones, personas, tecnología y negocio.
      </p>
      <p style="font-size: 1.25rem; color: #ffd7a0; font-family: var(--font-serif); font-style: italic;">
        El siguiente salto no consiste en saber más de lo mismo. Consiste en ampliar tu perspectiva.
      </p>
    </div>
    <div class="split-visual" style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);">
       <ul style="list-style: none; padding: 0; margin: 0; color: #fff; font-size: 1.2rem; display: flex; flex-direction: column; gap: 1rem;">
         <li style="display:flex; align-items:center; gap: 1rem; opacity: 0.5;">
           <span style="color: var(--enae-granate);">✗</span> Visión departamental
         </li>
         <li style="display:flex; align-items:center; gap: 1rem; opacity: 0.5;">
           <span style="color: var(--enae-granate);">✗</span> Ejecución de tareas
         </li>
         <li style="display:flex; align-items:center; gap: 1rem; opacity: 0.5;">
           <span style="color: var(--enae-granate);">✗</span> Lenguaje técnico
         </li>
         <li style="display:flex; align-items:center; gap: 1rem; font-weight: bold; font-size: 1.4rem; margin-top: 1rem; color: #ffd7a0;">
           <span style="color: #28a745;">✓</span> Visión global de negocio
         </li>
       </ul>
    </div>
  </div>
</section>

<!-- BLOQUE 3: EL CAMBIO -->
<section class="enae-wm" style="padding: 6rem 0; background: var(--surface);">
  <div class="wrap" style="max-width: 900px;">
    <h2 class="mix reveal" style="text-align: center; margin-bottom: 1rem;">
      <span class="t-serif">De especialista a</span>
      <span class="t-bold">directivo.</span>
    </h2>
    <div class="reveal delay-1">
      <table class="table-cambio">
        <thead>
          <tr>
            <th>Hasta ahora</th>
            <th>A partir de ahora</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Dominar tu área</td>
            <td>Entender el negocio</td>
          </tr>
          <tr>
            <td>Ejecutar</td>
            <td>Decidir</td>
          </tr>
          <tr>
            <td>Gestionar tareas</td>
            <td>Liderar personas</td>
          </tr>
          <tr>
            <td>Pensar en tu departamento</td>
            <td>Pensar en la empresa</td>
          </tr>
          <tr>
            <td>Conseguir resultados funcionales</td>
            <td>Generar impacto de negocio</td>
          </tr>
        </tbody>
      </table>
      <p style="text-align: center; margin-top: 3rem; font-size: 1.3rem; font-weight: 600; color: var(--enae-granate);">
        Ese es el cambio que necesitas para dar el siguiente paso.
      </p>
    </div>
  </div>
</section>

<!-- BLOQUE 4: QUÉ VAS A DESARROLLAR -->
<section class="enae-wm" style="padding: 6rem 0; background: var(--enae-blanco);">
  <div class="wrap">
    <div style="text-align: center; max-width: 800px; margin: 0 auto;">
      <h2 class="mix reveal">
        <span class="t-bold">Una visión que va</span>
        <span class="t-serif">más allá de tu área.</span>
      </h2>
      <p class="reveal delay-1" style="font-size: 1.1rem; color: var(--text); margin-top: 1.5rem;">
        Con el Executive MBA desarrollarás las capacidades necesarias para asumir mayores responsabilidades:
      </p>
    </div>
    
    <div class="develop-grid reveal delay-2">
      <div class="develop-card">
        <h4>Estrategia</h4>
        <p>Entender el negocio y tomar decisiones con visión global.</p>
      </div>
      <div class="develop-card">
        <h4>Finanzas</h4>
        <p>Interpretar los números que determinan las decisiones empresariales.</p>
      </div>
      <div class="develop-card">
        <h4>Liderazgo</h4>
        <p>Pasar de gestionar tareas a movilizar equipos.</p>
      </div>
      <div class="develop-card">
        <h4>Operaciones y marketing</h4>
        <p>Comprender cómo las diferentes áreas generan valor.</p>
      </div>
      <div class="develop-card">
        <h4>IA y transformación</h4>
        <p>Entender las nuevas herramientas y su impacto en el negocio.</p>
      </div>
    </div>
  </div>
</section>

<!-- BLOQUE 5: EL VALOR PROFESIONAL -->
<section class="enae-wm" style="padding: 6rem 0; background: var(--surface);">
  <div class="wrap" style="max-width: 800px; text-align: center;">
    <h2 class="mix reveal" style="margin-bottom: 2rem;">
      <span class="t-serif">Tu próxima promoción no debería depender solo de los años que llevas.</span><br>
      <span class="t-bold" style="color: var(--enae-granate); font-size: clamp(24px, 3vw, 36px);">Debe depender de lo preparado que estás para asumir más.</span>
    </h2>
    <p class="reveal delay-1" style="font-size: 1.2rem; color: var(--text); line-height: 1.6;">
      El Executive MBA te ayuda a desarrollar una perspectiva directiva para afrontar nuevos retos, acceder a posiciones de mayor responsabilidad y dejar de ser visto únicamente como especialista.
    </p>
  </div>
</section>

<!-- BLOQUE 6: EXPERIENCIA / NETWORKING -->
<section id="claustro" class="enae-wm enae-wm--porque">
  <div class="wrap">
    <div class="claustro-banner reveal">
      <div class="claustro-img-col">
        <img src="./src/img/entrega%20diplomas%20enae%20gnfoto2022%20(76).jpg" alt="Networking ENAE" loading="lazy">
      </div>
      <div class="claustro-content-col">
        <div class="claustro-quote-col">
          <span class="eyebrow" style="margin-bottom:16px;"><span class="dot"></span> Networking <span class="rule"></span></span>
          <blockquote class="quote" style="font-size: 1.4rem;">
            No aprendas a dirigir solo desde los libros. Comparte aula con profesionales que, como tú, están creciendo en responsabilidad.
          </blockquote>
          <p class="quote-attrib">Experiencias diferentes. Sectores diferentes.</p>
        </div>
        <div class="claustro-facts-col" style="justify-content: center;">
          <div class="cf-item" style="border: none;">
            <span class="cf-num" style="color: var(--enae-granate); font-size: 1.5rem; text-align: left; line-height: 1.3;">Una misma ambición:<br>dar el siguiente paso profesional.</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- BLOQUE 7: DATOS DEL PROGRAMA -->
<section class="stats enae-wm" style="background: var(--enae-granate); color: #fff; padding: 4rem 0;">
  <div class="wrap reveal">
    <div class="stats-grid" style="grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 2rem; border: none;">
      <div style="border: none; padding: 0; text-align: center;">
        <div class="kpi-num-lg">60<span class="u">ECTS</span></div>
      </div>
      <div style="border: none; padding: 0; text-align: center;">
        <div class="kpi-num-lg">10<span class="u">meses</span></div>
      </div>
      <div style="border: none; padding: 0; text-align: center;">
        <div class="kpi-num-lg" style="font-size: 2rem; line-height: 2;">Executive MBA</div>
      </div>
      <div style="border: none; padding: 0; text-align: center;">
        <div class="kpi-num-lg">31<span class="u">años</span></div>
        <div class="kpi-label">edad media</div>
      </div>
      <div style="border: none; padding: 0; text-align: center;">
        <div class="kpi-num-lg">40<span class="u">%</span></div>
        <div class="kpi-label">ejecutivos</div>
      </div>
      <div style="border: none; padding: 0; text-align: center;">
        <div class="kpi-num-lg">29<span class="u">%</span></div>
        <div class="kpi-label">mandos intermedios</div>
      </div>
    </div>
    <p style="text-align: center; margin-top: 3rem; font-size: 1.1rem; opacity: 0.9;">
      Una formación compatible con profesionales que ya están trabajando y quieren seguir avanzando.
    </p>
  </div>
</section>

<!-- BLOQUE 8: CIERRE -->
"""

new_form_cta = form_cta_part.replace(
    '<span class="t-bold">El Executive MBA</span>\n          <span class="t-serif">empieza con una conversación.</span>',
    '<span class="t-serif">Ya has demostrado que sabes hacer.</span><br><span class="t-bold">Ahora es el momento de demostrar que sabes dirigir.</span>'
).replace(
    'Cuéntanos sobre tu trayectoria y tus objetivos. Un asesor directivo analizará tu perfil, te explicará las modalidades de estudio y resolverá todas tus preguntas sin compromiso.',
    'Da el salto de especialista a directivo.<br><br><strong>Executive MBA · ENAE</strong>'
)

new_content += new_form_cta

# Combine everything
final_html = head_part + new_content + footer_part

# Let's fix the CTA URL just in case
final_html = final_html.replace('href="#solicitar" class="btn float">Solicitar info', 'href="#solicitar" class="btn float">Solicita información')

with open('enae-executive-mba-mandos-intermedios.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Created enae-executive-mba-mandos-intermedios.html successfully.")
