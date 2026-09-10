import re

html_files = ['rrhh-ceos.html', 'rrhh-mandos-intermedios.html']

new_block = """  <div class="curric-pillars reveal delay-1">
    <details class="pillar" open>
      <summary>1. LEARNING DEVELOPMENT Y UPSKILLING - RESKILLING</summary>
      <div class="p-modules">
        <p style="padding-bottom: 1rem; margin: 0; color: var(--enae-negro); font-size: 15px; line-height: 1.5;">Aprende a <strong>diseñar, planificar y ejecutar acciones formativas eficaces, innovadoras y alineadas con objetivos estratégicos</strong>.</p>
      </div>
    </details>
    <details class="pillar">
      <summary>2. LABORATORIO DE VISUALIZACIÓN Y STORYTELLING CON DATOS PARA RRHH</summary>
      <div class="p-modules">
        <p style="padding-bottom: 1rem; margin: 0; color: var(--enae-negro); font-size: 15px; line-height: 1.5;">Los datos por sí solos no generan impacto. Lo que marca la diferencia es saber interpretarlos, visualizarlos con claridad y convertirlos en historias que generen decisiones.</p>
      </div>
    </details>
    <details class="pillar">
      <summary>3. IA APLICADA A RRHH</summary>
      <div class="p-modules">
        <p style="padding-bottom: 1rem; margin: 0; color: var(--enae-negro); font-size: 15px; line-height: 1.5;">La Inteligencia Artificial ya está transformando la forma en que las organizaciones atraen, gestionan y desarrollan el talento.</p>
      </div>
    </details>
    <details class="pillar">
      <summary>4. GESTIÓN DE ENTORNOS AGILE EN RRHH</summary>
      <div class="p-modules">
        <p style="padding-bottom: 1rem; margin: 0; color: var(--enae-negro); font-size: 15px; line-height: 1.5;">El propósito principal de este curso es proporcionarte un profundo entendimiento de la <strong>cultura ágil</strong>, enfocándose en la necesidad crucial de que los departamentos de Recursos Humanos asuman el <strong>mindset ágil</strong>.</p>
      </div>
    </details>
    <details class="pillar">
      <summary>5. TOTAL REWARD: DISEÑO DE COMPENSACIÓN TOTAL</summary>
      <div class="p-modules">
        <p style="padding-bottom: 1rem; margin: 0; color: var(--enae-negro); font-size: 15px; line-height: 1.5;">A través de este curso podrás aprender a <strong>diseñar sistemas de compensación integrales</strong> que no solo benefician a tus empleados, sino que también tienen un impacto directo en el desempeño y los resultados de tu organización.</p>
      </div>
    </details>
    <details class="pillar">
      <summary>6. LEAN CHANGE AGENT</summary>
      <div class="p-modules">
        <p style="padding-bottom: 1rem; margin: 0; color: var(--enae-negro); font-size: 15px; line-height: 1.5;"><strong>Lean Change Agent: lidera la transformación en entornos de cambio constante.</strong></p>
      </div>
    </details>
    <details class="pillar">
      <summary>7. EXPERIENCIA DE EMPLEADO</summary>
      <div class="p-modules">
        <p style="padding-bottom: 1rem; margin: 0; color: var(--enae-negro); font-size: 15px; line-height: 1.5;">Transforma la cultura de las empresas y logra formar equipos resilientes, ágiles y comprometidos. Para <strong>atraer y retener el mejor talento</strong>, es crucial evolucionar hacia un modelo de gestión que ponga al empleado en el centro.</p>
      </div>
    </details>
    <details class="pillar">
      <summary>8. CLIMA Y WELLBEING</summary>
      <div class="p-modules">
        <p style="padding-bottom: 1rem; margin: 0; color: var(--enae-negro); font-size: 15px; line-height: 1.5;">Los continuos cambios en el entorno de las empresas y la globalización de los mercados han supuesto que las empresas deban agudizar su ingenio a la hora de buscar nuevas formas de conseguir ventajas competitivas.</p>
      </div>
    </details>
    <details class="pillar">
      <summary>9. DISEÑO ORGANIZACIONAL</summary>
      <div class="p-modules">
        <p style="padding-bottom: 1rem; margin: 0; color: var(--enae-negro); font-size: 15px; line-height: 1.5;">La evolución en las características del mundo laboral ha impulsado cambios significativos en la estructura de organizaciones y entidades.</p>
      </div>
    </details>
    <details class="pillar">
      <summary>10. TALENT MANAGEMENT: EVALUACIÓN DEL DESEMPEÑO Y DIRECCIÓN POR OBJETIVOS</summary>
      <div class="p-modules">
        <p style="padding-bottom: 1rem; margin: 0; color: var(--enae-negro); font-size: 15px; line-height: 1.5;">En el dinámico panorama empresarial actual, la <strong>gestión eficaz del talento es un factor crítico</strong> que impulsa el éxito y la sostenibilidad de las organizaciones.</p>
      </div>
    </details>
    <details class="pillar">
      <summary>11. TALENT ACQUISITION & EMPLOYER BRANDING</summary>
      <div class="p-modules">
        <p style="padding-bottom: 1rem; margin: 0; color: var(--enae-negro); font-size: 15px; line-height: 1.5;">La gestión del talento es un proceso que comienza con la <strong>identificación y contratación de personas</strong> que den valor a la empresa; además, también se ocupa de <strong>retener</strong> el que ya existe dentro de la organización.</p>
      </div>
    </details>
    <details class="pillar">
      <summary>12. VISIÓN ESTRATÉGICA DE LOS RECURSOS HUMANOS HR BUSINESS PARTNER</summary>
      <div class="p-modules">
        <p style="padding-bottom: 1rem; margin: 0; color: var(--enae-negro); font-size: 15px; line-height: 1.5;">En el actual escenario global, la gestión de personas demanda más que nunca una aportación interna significativa, exigiendo la <strong>creación de valor</strong>.</p>
      </div>
    </details>
    <details class="pillar">
      <summary>13. DIRECCIÓN DE EQUIPOS DE ALTO RENDIMIENTO</summary>
      <div class="p-modules">
        <p style="padding-bottom: 1rem; margin: 0; color: var(--enae-negro); font-size: 15px; line-height: 1.5;">En un mundo empresarial cada vez más competitivo y en constante evolución, contar con equipos efectivos se ha convertido en un factor clave para el éxito.</p>
      </div>
    </details>
    <details class="pillar">
      <summary>14. MARCO REGULATORIO Y RELACIONES LABORALES EN LA ERA DIGITAL</summary>
      <div class="p-modules">
        <p style="padding-bottom: 1rem; margin: 0; color: var(--enae-negro); font-size: 15px; line-height: 1.5;">La finalidad de este curso es ofrecer un <strong>acercamiento a la normativa en el ámbito de las relaciones laborales</strong> desde una perspectiva eminentemente práctica y operativa.</p>
      </div>
    </details>
  </div>"""

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Use regex to find the curric-pillars block and replace it
    content = re.sub(r'<div class="curric-pillars reveal delay-1">.*?</div>\s*<p class="curric-note', new_block + '\n  <p class="curric-note', content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Updated {f}")

