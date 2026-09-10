import glob

html_files = glob.glob('asesoria-fiscal-*.html')

old_block = """  <div class="curric-pillars reveal delay-1">
    <details class="pillar" open>
      <summary>Sistema tributario y fiscalidad empresarial <span class="p-count">Módulos clave</span></summary>
      <div class="p-modules">
        <div class="p-mod"><span class="m-num">i</span><span class="m-name">Sistema tributario español</span></div>
        <div class="p-mod"><span class="m-num">ii</span><span class="m-name">Fiscalidad empresarial</span></div>
        <div class="p-mod"><span class="m-num">iii</span><span class="m-name">Procedimientos tributarios</span></div>
      </div>
    </details>
    <details class="pillar">
      <summary>Impuestos principales <span class="p-count">Módulos clave</span></summary>
      <div class="p-modules">
        <div class="p-mod"><span class="m-num">i</span><span class="m-name">Impuesto sobre Sociedades</span></div>
        <div class="p-mod"><span class="m-num">ii</span><span class="m-name">Impuesto sobre el Valor Añadido (IVA)</span></div>
        <div class="p-mod"><span class="m-num">iii</span><span class="m-name">IRPF</span></div>
      </div>
    </details>
    <details class="pillar">
      <summary>Estrategia y contexto internacional <span class="p-count">Módulos clave</span></summary>
      <div class="p-modules">
        <div class="p-mod"><span class="m-num">i</span><span class="m-name">Fiscalidad internacional</span></div>
        <div class="p-mod"><span class="m-num">ii</span><span class="m-name">Planificación y estrategia fiscal</span></div>
      </div>
    </details>
  </div>"""

new_block = """  <div class="curric-pillars reveal delay-1">
    <details class="pillar" open>
      <summary>Imposición sobre Sociedades</summary>
      <div class="p-modules">
        <p style="padding-bottom: 1rem; margin: 0; color: var(--enae-negro); font-size: 15px; line-height: 1.5;">Este curso tiene como finalidad adquirir unos conocimientos adecuados en materia fiscal dentro del ámbito de las empresas.</p>
      </div>
    </details>
    <details class="pillar">
      <summary>Imposición Indirecta Vinculada a la Actividad Empresarial</summary>
      <div class="p-modules">
        <p style="padding-bottom: 1rem; margin: 0; color: var(--enae-negro); font-size: 15px; line-height: 1.5;">Comprender y aplicar correctamente la imposición indirecta es esencial para garantizar el cumplimiento fiscal y optimizar la gestión tributaria de cualquier empresa.</p>
      </div>
    </details>
    <details class="pillar">
      <summary>Procedimientos Tributarios. Dictámenes y Agencia Tributaria</summary>
      <div class="p-modules">
        <p style="padding-bottom: 1rem; margin: 0; color: var(--enae-negro); font-size: 15px; line-height: 1.5;">Relacionarse con la Administración Tributaria es más que conocer las obligaciones fiscales, también es entender los procedimientos que las regulan.</p>
      </div>
    </details>
    <details class="pillar">
      <summary>Imposición sobre la Renta y el Patrimonio de las Personas Físicas</summary>
      <div class="p-modules">
        <p style="padding-bottom: 1rem; margin: 0; color: var(--enae-negro); font-size: 15px; line-height: 1.5;">Gestionar correctamente la fiscalidad personal no solo es una obligación, es una herramienta clave para tomar decisiones económicas con inteligencia y previsión.</p>
      </div>
    </details>
    <details class="pillar">
      <summary>Imposición Autonómica y Local</summary>
      <div class="p-modules">
        <p style="padding-bottom: 1rem; margin: 0; color: var(--enae-negro); font-size: 15px; line-height: 1.5;">Este curso aborda de manera integral las dos principales figuras impositivas compartidas por todas las comunidades autónomas: el Impuesto sobre Sucesiones y Donaciones y el Impuesto sobre Transmisiones Patrimoniales y Actos Jurídicos Documentados.</p>
      </div>
    </details>
    <details class="pillar">
      <summary>Bases para el Estudio del Sistema Tributario Español</summary>
      <div class="p-modules">
        <p style="padding-bottom: 1rem; margin: 0; color: var(--enae-negro); font-size: 15px; line-height: 1.5;">Este Curso en Bases para el Estudio del Sistema de Tributación Española es esencial para dominar conceptos fundamentales que abarcan los tributos y la normativa que regula los procedimientos tributarios.</p>
      </div>
    </details>
  </div>"""

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if old_block in content:
        print(f"Updating {f}...")
        content = content.replace(old_block, new_block)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
    else:
        print(f"Block not found in {f}!")

