import re

with open('rrhh-direccion-humana.html', 'r', encoding='utf-8') as f:
    html = f.read()

fundae_section = """
<!-- FUNDAE SECTION -->
<section class="enae-wm enae-wm--fundae" id="fundae" style="background: var(--surface); padding-top: 5rem; padding-bottom: 5rem; border-bottom: 1px solid rgba(0,0,0,0.05);">
  <div class="wrap reveal">
    <div class="faq-grid" style="align-items: start;">
      <div class="faq-head">
        <img src="https://impulse.es/wp-content/uploads/2025/12/Group-118-1.png" alt="Formación Bonificable FUNDAE" style="max-width: 200px; margin-bottom: 2rem;">
        <h2 class="mix">
          <span class="t-bold" style="font-size: clamp(28px, 4vw, 42px);">Formación bonificable FUNDAE</span>
        </h2>
        <p style="color: var(--ink); font-size: 1.15rem; line-height: 1.5; margin-top: 1rem;">
          <strong>¿Sabías que puedes acceder a nuestros cursos de forma bonificada?</strong> Te ayudamos a aprovechar el crédito para que la formación no suponga ningún coste adicional ni complicaciones.
        </p>
      </div>
      <div class="faq-list">
        
        <details class="pillar">
          <summary>¿Se puede bonificar la formación con FUNDAE?</summary>
          <div class="a">
            <p>Sí.<br>La mayoría de nuestros cursos son <strong>bonificables a través de FUNDAE</strong>. Todas las empresas que cotizan por Formación Profesional disponen de un <strong>crédito anual</strong>, aunque muchas no lo saben o no lo utilizan.</p>
            <p>En ENAE <strong>calculamos tu crédito disponible</strong> y te explicamos cómo aprovecharlo al máximo.</p>
          </div>
        </details>

        <details class="pillar">
          <summary>¿Muchas empresas pierden su crédito FUNDAE cada año?</summary>
          <div class="a">
            <p>Sí, y es más habitual de lo que parece.<br><strong>Más del 79,8 % de las empresas españolas pierde su crédito formativo cada año</strong> por desconocimiento o por miedo a la gestión administrativa.</p>
            <p>Ese crédito <strong>ya lo has pagado</strong> en tus cotizaciones a la Seguridad Social y, si no se utiliza antes del 31 de diciembre, <strong>se pierde</strong>.</p>
            <p>Nos encargamos de que no desaproveches esa oportunidad.</p>
          </div>
        </details>

        <details class="pillar">
          <summary>¿La gestión de FUNDAE es complicada?</summary>
          <div class="a">
            <p>Puede serlo si no se tiene experiencia.<br>Por eso, como <strong>Entidad Organizadora</strong>, nos encargamos del <strong>100 % de la gestión administrativa</strong>: comunicaciones, documentación, justificaciones y seguimiento.</p>
            <p>👉 Tú te centras en formar a tu equipo.<br>👉 Nosotros nos ocupamos de todo, <strong>con cero riesgos</strong>.</p>
          </div>
        </details>

        <details class="pillar">
          <summary>Hemos tenido malas experiencias con FUNDAE, ¿por qué ahora sería diferente?</summary>
          <div class="a">
            <p>Es una situación bastante común cuando la formación está mal planteada o mal gestionada. Las malas experiencias suelen venir de: contenidos poco aplicables, formación genérica sin relación con la actividad de la empresa, errores administrativos o incumplimientos normativos.</p>
            <p>Trabajamos diferente. Contamos con <strong>profesionales con experiencia en gestión de bonificaciones y subvenciones</strong>, garantizando <strong>seguridad jurídica, cumplimiento normativo y calidad formativa</strong>, para que no tengas sorpresas.</p>
          </div>
        </details>

        <details class="pillar">
          <summary>¿Qué tipo de empresas pueden beneficiarse de FUNDAE?</summary>
          <div class="a">
            <p>Cualquier empresa, independientemente de su tamaño o sector, que tenga trabajadores en plantilla y cotice por Formación Profesional dispone de <strong>crédito FUNDAE</strong>.</p>
          </div>
        </details>

        <details class="pillar">
          <summary>¿Hay que pagar primero la formación?</summary>
          <div class="a">
            <p>Sí.<br>El sistema FUNDAE funciona como un reembolso garantizado: la empresa abona inicialmente el coste del curso y, una vez finalizado correctamente, recupera ese importe descontándolo de sus cotizaciones a la Seguridad Social.</p>
            <p>Nuestro equipo te acompaña durante todo el proceso para que sea claro, sencillo y seguro.</p>
            <p>👉 No es un gasto, es una inversión estratégica que retorna a la empresa.</p>
          </div>
        </details>

        <details class="pillar">
          <summary>No tenemos tiempo para organizar cursos...</summary>
          <div class="a">
            <p>Lo entendemos perfectamente.<br>La carga de trabajo diaria es uno de los principales frenos.</p>
            <p>Por eso: planificamos los contenidos, adaptamos los horarios a la actividad del negocio, y gestionamos toda la documentación.</p>
            <p>👉 <strong>Liberamos tu agenda</strong> para que la formación no afecte a la productividad de la empresa.</p>
          </div>
        </details>

        <details class="pillar">
          <summary>¿La formación bonificada realmente aporta resultados?</summary>
          <div class="a">
            <p>Sí, siempre que la formación sea de calidad.<br>Cuando los cursos son genéricos o teóricos, el impacto es mínimo.</p>
            <p>En ENAE <strong>no enseñamos teoría, enseñamos soluciones</strong>.<br>Trabajamos con <strong>metodología propia</strong>, contenidos actualizados y <strong>docentes expertos en activo</strong>, lo que garantiza una <strong>aplicabilidad inmediata</strong>: lo que se aprende hoy, se aplica mañana en el trabajo.</p>
          </div>
        </details>

        <details class="pillar">
          <summary>¿Formar a mi equipo no hará que se vaya a otra empresa?</summary>
          <div class="a">
            <p>Todo lo contrario.<br>El verdadero riesgo es <strong>no formarlos y que se queden estancados</strong>.</p>
            <p>La formación: aumenta la motivación, refuerza el compromiso, mejora el rendimiento, y reduce la rotación.</p>
            <p>Un equipo formado se siente valorado y permanece más tiempo en la empresa.<br>👉 <strong>Un equipo estancado frena tu empresa; un equipo formado la impulsa.</strong></p>
          </div>
        </details>

        <details class="pillar">
          <summary>Si mi empresa tiene más de 5 trabajadores, ¿debo aportar cofinanciación privada?</summary>
          <div class="a">
            <p>Sí, la normativa exige una pequeña cofinanciación para empresas de más de 5 trabajadores.<br>Pero <strong>no tiene por qué ser económica</strong>.</p>
            <p>Puede realizarse imputando los <strong>costes salariales de los trabajadores durante las horas de formación</strong> dentro de su jornada laboral.</p>
            <p>Nosotros nos encargamos de calcularla, gestionarla y justificarla correctamente.</p>
          </div>
        </details>

      </div>
    </div>
  </div>
</section>
"""

# Insert FUNDAE section right before the FAQ section
html = html.replace('<!-- FAQ -->\n<section class="enae-wm enae-wm--faq"', fundae_section + '\n<!-- FAQ -->\n<section class="enae-wm enae-wm--faq"')

with open('rrhh-direccion-humana.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("FUNDAE section injected")

