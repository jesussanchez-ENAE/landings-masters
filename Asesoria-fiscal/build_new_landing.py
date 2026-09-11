import sys

file_path = 'asesoria-fiscal-colegio-abogados.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

head_split = content.split('<header class="hero d-hero enae-wm enae-wm--hero"')
if len(head_split) < 2:
    print("Error finding header start")
    sys.exit(1)

head_html = head_split[0]

foot_split = head_split[1].split('<footer>')
if len(foot_split) < 2:
    print("Error finding footer start")
    sys.exit(1)

foot_html = '<footer>' + foot_split[1]

body_html = """<header class="hero d-hero enae-wm enae-wm--hero" style="background: url('./src/img/hero_asesoria_fiscal_directivos.jpg') no-repeat center center; background-size: cover; position: relative;">
  <div class="pattern" aria-hidden="true">
    <span class="b1"></span><span class="b2"></span><span class="b3"></span><span class="b4"></span><span class="b5"></span>
  </div>
  <div class="wrap d-hero-inner reveal">
    <div class="d-hero-content">
      <span class="eyebrow" style="margin-bottom:16px;"><span class="dot"></span> ¿LA PARTE FISCAL TIENES QUE CONSULTARLA? <span class="rule"></span></span>
      <h1 class="hero-title mix">
        <span class="t-bold">Añade la perspectiva fiscal a</span>
        <span class="t-serif">tu conocimiento jurídico.</span>
      </h1>
      <p style="font-size: 1.125rem; font-weight: 300; line-height: 1.6; margin-top: 1rem; color: rgba(255,255,255,0.9);">
        <strong>Máster en Asesoría Fiscal de ENAE Business School</strong><br>
        Amplía tu capacidad de análisis y aporta más valor a tus clientes.
      </p>
      
      <div class="d-hero-meta" style="margin-top: 2.5rem;">
        <div><span>Máster en</span><strong>Asesoría Fiscal</strong></div>
        <div><span>Edición</span><strong>36ª edición</strong></div>
        <div><span>Duración</span><strong>60 ECTS</strong></div>
        <div><span>Inicio</span><strong>19 oct 2026</strong></div>
      </div>
    </div>
    <div class="d-hero-visual reveal delay-1" style="display:flex; justify-content:center; align-items:center;">
      <div class="d-form-container" style="background:#fff; padding: 2rem; border-radius: 12px; box-shadow: 0 20px 40px rgba(0,0,0,0.2); width:100%; max-width:500px;">
        <h3 style="margin: 0 0 1.25rem; font-size: 1.25rem; font-weight: 800; color: #111;">Solicita información</h3>
        <div data-form-id='90ea3a6e-104e-f111-bec7-7ced8d498631' data-form-api-url='https://public-eur.mkt.dynamics.com/api/v1.0/orgs/8bc28068-3b86-4b51-aa0e-5a151b861c76/landingpageforms' data-cached-form-url='https://assets-eur.mkt.dynamics.com/8bc28068-3b86-4b51-aa0e-5a151b861c76/digitalassets/forms/90ea3a6e-104e-f111-bec7-7ced8d498631'></div>
        <script src='https://formui-usa1.mkt.dynamics.com/eur/FormLoader/FormLoader.bundle.js'></script>
      </div>
    </div>
  </div>
</header>

<!-- BANNER DESTACADO BECAS -->
<div class="ia-banner reveal" style="background: linear-gradient(90deg, #1a1c1e, #0d0f11); color: #fff; padding: 1.5rem 1rem; text-align: center; margin: -2rem auto 3rem; width: 90%; max-width: 1000px; border-radius: 12px; box-shadow: 0 16px 32px rgba(0, 0, 0, 0.3); display: flex; align-items: center; justify-content: center; gap: 1rem; flex-wrap: wrap; position:relative; z-index:10; border: 1px solid rgba(212, 175, 55, 0.5);">
  <span style="background: linear-gradient(135deg, #dfc26a, #c09d3b); color: #111; padding: 6px 16px; border-radius: 20px; font-weight: 800; font-size: 13px; letter-spacing: 0.5px; text-transform: uppercase;">Exclusivo Colegiados</span>
  <span style="font-size: clamp(17px, 2vw, 21px); font-family: var(--font-serif); font-weight: 400; line-height: 1.3;">Disfruta de una <strong>beca del 20%</strong> exclusiva para miembros del <strong>Colegio de Abogados de la Región de Murcia</strong>.</span>
</div>

<section class="enae-wm" style="padding: 4rem 0 5rem; background: var(--surface);">
  <div class="wrap" style="max-width: 800px; margin: 0 auto; text-align: center;">
    <h2 class="mix reveal" style="margin-bottom: 2rem;">
      <span class="t-bold" style="color: var(--enae-granate);">TU CLIENTE NO VE LA PARTE JURÍDICA</span>
      <span class="t-serif" style="color: var(--ink);">Y LA FISCAL POR SEPARADO</span>
    </h2>
    <div class="reveal delay-1" style="font-size: 1.125rem; line-height: 1.8; color: var(--text);">
      <p style="margin-bottom: 1rem;">Una compraventa no es solo un contrato.</p>
      <p style="margin-bottom: 1rem;">Una reestructuración no es solo una operación societaria.</p>
      <p style="margin-bottom: 2rem;">Una sucesión no es solo una cuestión patrimonial.</p>
      <p style="margin-bottom: 2rem; font-weight: 700; font-size: 1.25rem; color: var(--ink);">Muchas de las decisiones que asesores jurídicamente tienen también consecuencias fiscales.</p>
      <p style="margin-bottom: 3rem;">Y cuanto mejor comprendas ambas dimensiones, mejor podrás analizar la operación en su conjunto.</p>
      <div style="background: rgba(169, 24, 50, 0.05); padding: 2.5rem; border-left: 4px solid var(--enae-granate); border-radius: 0 12px 12px 0; text-align: left;">
        <h3 style="font-family: var(--font-serif); font-size: 1.75rem; color: var(--enae-granate); margin: 0 0 0.5rem;">Porque conocer la ley es fundamental.</h3>
        <p style="font-weight: 700; color: var(--ink); margin: 0; font-size: 1.25rem;">Entender su impacto fiscal puede marcar la diferencia.</p>
      </div>
    </div>
  </div>
</section>

<section class="enae-wm" style="padding: 6rem 0; background: #fff;">
  <div class="wrap">
    <h2 class="mix reveal" style="text-align: center; margin-bottom: 4rem;">
      <span class="t-bold">¿CUÁNTO DE TU ASESORAMIENTO</span>
      <span class="t-serif">DEPENDE HOY DE OTROS ESPECIALISTAS?</span>
    </h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 4rem; align-items: center; max-width: 1000px; margin: 0 auto;">
      <div class="reveal">
        <p style="font-size: 1.25rem; line-height: 1.6; color: var(--text); margin-bottom: 1.5rem;">No se trata de sustituir al asesor fiscal.</p>
        <p style="font-size: 1.75rem; font-family: var(--font-serif); color: var(--ink); line-height: 1.4; margin-bottom: 2rem;">
          Se trata de <strong>entender la fiscalidad</strong> lo suficiente como para <span style="color: var(--enae-granate);">participar en la conversación con criterio.</span>
        </p>
      </div>
      <div class="reveal delay-1">
        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1.25rem;">
          <li style="display: flex; gap: 1rem; align-items: flex-start;">
            <svg style="flex-shrink:0; color: var(--enae-granate); width: 24px; height: 24px; margin-top: 2px;" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
            <span style="font-size: 1.125rem; color: var(--text);">Para detectar las preguntas adecuadas.</span>
          </li>
          <li style="display: flex; gap: 1rem; align-items: flex-start;">
            <svg style="flex-shrink:0; color: var(--enae-granate); width: 24px; height: 24px; margin-top: 2px;" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
            <span style="font-size: 1.125rem; color: var(--text);">Para identificar posibles implicaciones tributarias.</span>
          </li>
          <li style="display: flex; gap: 1rem; align-items: flex-start;">
            <svg style="flex-shrink:0; color: var(--enae-granate); width: 24px; height: 24px; margin-top: 2px;" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
            <span style="font-size: 1.125rem; color: var(--text);">Para entender las alternativas.</span>
          </li>
          <li style="display: flex; gap: 1rem; align-items: flex-start;">
            <svg style="flex-shrink:0; color: var(--enae-granate); width: 24px; height: 24px; margin-top: 2px;" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
            <span style="font-size: 1.125rem; color: var(--text);">Para anticiparte a determinadas situaciones.</span>
          </li>
          <li style="display: flex; gap: 1rem; align-items: flex-start;">
            <svg style="flex-shrink:0; color: var(--enae-granate); width: 24px; height: 24px; margin-top: 2px;" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
            <span style="font-size: 1.125rem; font-weight: 700; color: var(--ink);">Y para ofrecer a tu cliente una visión más completa.</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="enae-wm" style="padding: 6rem 0; background: var(--surface);">
  <div class="wrap">
    <h2 class="mix reveal" style="text-align: center; margin-bottom: 4rem;">
      <span class="t-bold">AMPLÍA LO QUE PUEDES</span>
      <span class="t-serif">HACER POR TUS CLIENTES</span>
    </h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem; max-width: 1000px; margin: 0 auto;">
      <!-- Antes -->
      <div class="reveal delay-1" style="background: #fff; padding: 3rem; border-radius: 16px; border: 1px solid #e5e7eb; box-shadow: 0 10px 25px rgba(0,0,0,0.05);">
        <h3 style="font-family: var(--font-serif); font-size: 2.25rem; color: #6b7280; margin-bottom: 1rem;">Antes</h3>
        <p style="font-weight: 700; color: var(--ink); margin-bottom: 2rem; font-size: 1.125rem;">Tu conocimiento jurídico es el punto de partida. Pero ante determinadas operaciones:</p>
        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1.25rem; color: var(--text);">
          <li style="display: flex; gap: 1rem; align-items: flex-start;">
            <span style="color: #9ca3af; font-weight: 700; font-size: 1.25rem; margin-top: -2px;">✕</span>
            <span>Tienes que consultar sus implicaciones fiscales.</span>
          </li>
          <li style="display: flex; gap: 1rem; align-items: flex-start;">
            <span style="color: #9ca3af; font-weight: 700; font-size: 1.25rem; margin-top: -2px;">✕</span>
            <span>Hay cuestiones que necesitas derivar a otros especialistas.</span>
          </li>
          <li style="display: flex; gap: 1rem; align-items: flex-start;">
            <span style="color: #9ca3af; font-weight: 700; font-size: 1.25rem; margin-top: -2px;">✕</span>
            <span>Parte del análisis queda fuera de tu ámbito.</span>
          </li>
          <li style="display: flex; gap: 1rem; align-items: flex-start;">
            <span style="color: #9ca3af; font-weight: 700; font-size: 1.25rem; margin-top: -2px;">✕</span>
            <span>Puedes necesitar apoyo para valorar determinadas alternativas.</span>
          </li>
        </ul>
      </div>
      <!-- Después -->
      <div class="reveal delay-2" style="background: #fff; padding: 3rem; border-radius: 16px; border: 2px solid var(--enae-granate); box-shadow: 0 20px 40px rgba(169, 24, 50, 0.1); position: relative;">
        <div style="position: absolute; top: -14px; right: 32px; background: var(--enae-granate); color: #fff; padding: 6px 16px; border-radius: 20px; font-weight: 800; font-size: 0.875rem; letter-spacing: 0.5px;">CON EL MÁSTER</div>
        <h3 style="font-family: var(--font-serif); font-size: 2.25rem; color: var(--enae-granate); margin-bottom: 1rem;">Después</h3>
        <p style="font-weight: 700; color: var(--ink); margin-bottom: 2rem; font-size: 1.125rem;">Incorporas la perspectiva fiscal a tu análisis jurídico.</p>
        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1.25rem; color: var(--ink);">
          <li style="display: flex; gap: 1rem; align-items: flex-start;">
            <svg style="flex-shrink:0; color: var(--enae-granate); width: 24px; height: 24px; margin-top: 0px;" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
            <span>Comprendes mejor las consecuencias tributarias.</span>
          </li>
          <li style="display: flex; gap: 1rem; align-items: flex-start;">
            <svg style="flex-shrink:0; color: var(--enae-granate); width: 24px; height: 24px; margin-top: 0px;" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
            <span>Detectas posibles implicaciones antes de tomar decisiones.</span>
          </li>
          <li style="display: flex; gap: 1rem; align-items: flex-start;">
            <svg style="flex-shrink:0; color: var(--enae-granate); width: 24px; height: 24px; margin-top: 0px;" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
            <span>Puedes plantear mejores preguntas y alternativas.</span>
          </li>
          <li style="display: flex; gap: 1rem; align-items: flex-start;">
            <svg style="flex-shrink:0; color: var(--enae-granate); width: 24px; height: 24px; margin-top: 0px;" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
            <span>Te comunicas con mayor criterio con asesores financieros.</span>
          </li>
          <li style="display: flex; gap: 1rem; align-items: flex-start;">
            <svg style="flex-shrink:0; color: var(--enae-granate); width: 24px; height: 24px; margin-top: 0px;" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
            <span style="font-weight: 700;">Aportas una visión más completa al cliente.</span>
          </li>
        </ul>
      </div>
    </div>
    <div class="reveal delay-3" style="text-align: center; margin-top: 5rem;">
      <h3 style="font-size: 1.5rem; font-weight: 300; color: var(--text); margin-bottom: 0.5rem;">No tienes que cambiar de profesión.</h3>
      <h2 style="font-family: var(--font-serif); font-size: 2.5rem; color: var(--ink); margin: 0;">Tienes que ampliar tu perspectiva.</h2>
    </div>
  </div>
</section>

<section class="enae-wm" style="padding: 6rem 0; background: #fff;">
  <div class="wrap">
    <div style="max-width: 800px; margin: 0 auto; text-align: center;">
      <h2 class="mix reveal" style="margin-bottom: 1.5rem;">
        <span class="t-bold">TUS CLIENTES YA NECESITAN</span>
        <span class="t-serif">ASESORAMIENTO FISCAL.</span>
      </h2>
      <p class="reveal delay-1" style="font-size: 1.25rem; font-weight: 700; color: var(--text); margin-bottom: 3rem;">La cuestión es quién participa en esa conversación.</p>
      
      <p class="reveal delay-1" style="font-size: 1.125rem; color: var(--text); margin-bottom: 2.5rem;">Dentro de tu propia cartera de clientes ya existen decisiones con una dimensión fiscal:</p>
      
      <div class="reveal delay-2" style="display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem; margin-bottom: 4rem;">
        <span style="background: var(--surface); padding: 12px 24px; border-radius: 30px; font-weight: 700; color: var(--ink); border: 1px solid #e5e7eb;">Operaciones societarias</span>
        <span style="background: var(--surface); padding: 12px 24px; border-radius: 30px; font-weight: 700; color: var(--ink); border: 1px solid #e5e7eb;">Compraventas</span>
        <span style="background: var(--surface); padding: 12px 24px; border-radius: 30px; font-weight: 700; color: var(--ink); border: 1px solid #e5e7eb;">Contratos</span>
        <span style="background: var(--surface); padding: 12px 24px; border-radius: 30px; font-weight: 700; color: var(--ink); border: 1px solid #e5e7eb;">Sucesiones y donaciones</span>
        <span style="background: var(--surface); padding: 12px 24px; border-radius: 30px; font-weight: 700; color: var(--ink); border: 1px solid #e5e7eb;">Inversiones</span>
        <span style="background: var(--surface); padding: 12px 24px; border-radius: 30px; font-weight: 700; color: var(--ink); border: 1px solid #e5e7eb;">Patrimonio</span>
        <span style="background: var(--surface); padding: 12px 24px; border-radius: 30px; font-weight: 700; color: var(--ink); border: 1px solid #e5e7eb;">Retribuciones</span>
        <span style="background: var(--surface); padding: 12px 24px; border-radius: 30px; font-weight: 700; color: var(--ink); border: 1px solid #e5e7eb;">Reestructuraciones</span>
      </div>
      
      <p class="reveal delay-3" style="font-size: 1.125rem; line-height: 1.6; color: var(--text); margin-bottom: 3rem; background: rgba(169, 24, 50, 0.05); padding: 2rem; border-radius: 12px;">
        Incorporar conocimientos avanzados de fiscalidad puede ayudarte a <strong style="color: var(--enae-granate);">ampliar los problemas que eres capaz de analizar</strong> y a participar en operaciones donde la dimensión jurídica y fiscal están estrechamente relacionadas.
      </p>
      
      <h3 class="reveal delay-3" style="font-size: 1.5rem; font-weight: 300; color: var(--text); margin-bottom: 0.5rem;">No se trata únicamente de saber más.</h3>
      <h2 class="reveal delay-3" style="font-family: var(--font-serif); font-size: 2.5rem; color: var(--enae-granate); margin-bottom: 3rem;">SE TRATA DE PODER APORTAR MÁS.</h2>
      
      <a href="#solicitar" class="btn reveal delay-4">Solicita información <span class="arrow">&rarr;</span></a>
    </div>
  </div>
</section>

<section class="enae-wm" style="padding: 6rem 0; background: var(--surface);" id="programa">
  <div class="wrap">
    <div style="text-align: center; margin-bottom: 4rem; max-width: 800px; margin-inline: auto;">
      <h2 class="mix reveal">
        <span class="t-bold">LO QUE APRENDES.</span>
        <span class="t-serif">LO QUE PUEDES HACER CON ELLO.</span>
      </h2>
      <p class="reveal delay-1" style="font-size: 1.125rem; color: var(--text); margin-top: 1rem; line-height: 1.6;">Una formación especializada para profesionales que quieren comprender la fiscalidad aplicada a las decisiones empresariales y patrimoniales.</p>
    </div>
    
    <div class="reveal delay-2" style="background: #fff; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.05); margin-bottom: 4rem; max-width: 1000px; margin-inline: auto;">
      <div style="overflow-x: auto;">
        <table style="width: 100%; border-collapse: collapse; text-align: left; min-width: 600px;">
          <thead>
            <tr style="background: var(--enae-granate); color: #fff;">
              <th style="padding: 1.5rem 2rem; font-weight: 700; font-size: 1.125rem; width: 40%;">El Máster en Asesoría Fiscal</th>
              <th style="padding: 1.5rem 2rem; font-weight: 700; font-size: 1.125rem;">Lo que aporta a tu práctica jurídica</th>
            </tr>
          </thead>
          <tbody style="color: var(--ink);">
            <tr style="border-bottom: 1px solid #e5e7eb;">
              <td style="padding: 1.5rem 2rem; font-weight: 700;">Formación fiscal especializada</td>
              <td style="padding: 1.5rem 2rem; color: var(--text);">Comprender la dimensión tributaria de las operaciones</td>
            </tr>
            <tr style="border-bottom: 1px solid #e5e7eb; background: #fafafa;">
              <td style="padding: 1.5rem 2rem; font-weight: 700;">Profesores profesionales</td>
              <td style="padding: 1.5rem 2rem; color: var(--text);">Aprender desde la experiencia y la práctica</td>
            </tr>
            <tr style="border-bottom: 1px solid #e5e7eb;">
              <td style="padding: 1.5rem 2rem; font-weight: 700;">Casos prácticos</td>
              <td style="padding: 1.5rem 2rem; color: var(--text);">Aplicar los conocimientos a situaciones reales</td>
            </tr>
            <tr style="border-bottom: 1px solid #e5e7eb; background: #fafafa;">
              <td style="padding: 1.5rem 2rem; font-weight: 700;">Metodología ENAE</td>
              <td style="padding: 1.5rem 2rem; color: var(--text);">Convertir la normativa en criterio aplicable</td>
            </tr>
            <tr style="border-bottom: 1px solid #e5e7eb;">
              <td style="padding: 1.5rem 2rem; font-weight: 700;">Formación presencial / híbrida</td>
              <td style="padding: 1.5rem 2rem; color: var(--text);">Crear relaciones y compartir experiencias profesionales</td>
            </tr>
            <tr style="border-bottom: 1px solid #e5e7eb; background: #fafafa;">
              <td style="padding: 1.5rem 2rem; font-weight: 700;">Visión empresarial</td>
              <td style="padding: 1.5rem 2rem; color: var(--text);">Comprender al cliente más allá del expediente</td>
            </tr>
            <tr style="border-bottom: 1px solid #e5e7eb;">
              <td style="padding: 1.5rem 2rem; font-weight: 700;">Diversidad de perfiles</td>
              <td style="padding: 1.5rem 2rem; color: var(--text);">Entender cómo piensan otros profesionales que participan en una operación</td>
            </tr>
            <tr style="background: #fafafa;">
              <td style="padding: 1.5rem 2rem; font-weight: 700;">Titulación de ENAE Business School</td>
              <td style="padding: 1.5rem 2rem; color: var(--text);">Reforzar tu perfil y posicionamiento profesional</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Data cards -->
    <div class="reveal delay-3" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; max-width: 1000px; margin-inline: auto;">
      <div style="background: #fff; padding: 2rem; border-radius: 12px; text-align: center; border: 1px solid #e5e7eb; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
        <div style="font-size: 0.875rem; color: var(--text); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem; font-weight: 700;">Inicio</div>
        <div style="font-size: 1.5rem; font-weight: 800; color: var(--enae-granate);">19 octubre 2026</div>
      </div>
      <div style="background: #fff; padding: 2rem; border-radius: 12px; text-align: center; border: 1px solid #e5e7eb; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
        <div style="font-size: 0.875rem; color: var(--text); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem; font-weight: 700;">Créditos</div>
        <div style="font-size: 1.5rem; font-weight: 800; color: var(--enae-granate);">60 ECTS</div>
      </div>
      <div style="background: #fff; padding: 2rem; border-radius: 12px; text-align: center; border: 1px solid #e5e7eb; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
        <div style="font-size: 0.875rem; color: var(--text); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem; font-weight: 700;">Modalidad</div>
        <div style="font-size: 1.5rem; font-weight: 800; color: var(--enae-granate);">Presencial / Semipres.</div>
      </div>
      <div style="background: #fff; padding: 2rem; border-radius: 12px; text-align: center; border: 1px solid #e5e7eb; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
        <div style="font-size: 0.875rem; color: var(--text); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem; font-weight: 700;">Horarios</div>
        <div style="font-size: 1.5rem; font-weight: 800; color: var(--enae-granate);">Fines de semana</div>
      </div>
    </div>
  </div>
</section>

<section class="enae-wm" style="padding: 6rem 0; background: #fff;">
  <div class="wrap">
    <div style="display: grid; grid-template-columns: 1fr; gap: 4rem; max-width: 800px; margin: 0 auto;">
      
      <div class="reveal">
        <h3 style="font-family: var(--font-serif); font-size: 2rem; color: var(--ink); margin-bottom: 0.5rem;">NO NECESITAS SER ECONOMISTA.</h3>
        <h4 style="font-size: 1.5rem; font-weight: 300; color: var(--enae-granate); margin-bottom: 1.5rem;">Necesitas entender mejor la operación.</h4>
        <div style="border-left: 4px solid var(--enae-gris-claro); padding-left: 1.5rem; margin-bottom: 1.5rem;">
          <p style="font-weight: 700; color: var(--ink); font-size: 1.125rem; font-style: italic;">«Yo soy abogado, no economista.»</p>
        </div>
        <p style="color: var(--text); line-height: 1.8; font-size: 1.125rem; margin-bottom: 1rem;">Precisamente por eso tu conocimiento jurídico es una base especialmente valiosa.</p>
        <p style="color: var(--text); line-height: 1.8; font-size: 1.125rem; margin-bottom: 1rem;">El objetivo no es convertirte en economista. Es <strong>incorporar la perspectiva tributaria a la forma en la que ya analizas las operaciones.</strong></p>
        <p style="color: var(--text); line-height: 1.8; font-size: 1.125rem; margin-bottom: 1rem;">Tu especialidad sigue siendo el Derecho. Ahora puedes añadir una nueva dimensión a tu análisis.</p>
      </div>
      
      <hr style="border: 0; height: 1px; background: #e5e7eb;">
      
      <div class="reveal">
        <h3 style="font-family: var(--font-serif); font-size: 2rem; color: var(--ink); margin-bottom: 0.5rem;">NO SE TRATA DE SUSTITUIR AL ASESOR FISCAL.</h3>
        <h4 style="font-size: 1.5rem; font-weight: 300; color: var(--enae-granate); margin-bottom: 1.5rem;">Se trata de entenderlo mejor.</h4>
        <div style="border-left: 4px solid var(--enae-gris-claro); padding-left: 1.5rem; margin-bottom: 1.5rem;">
          <p style="font-weight: 700; color: var(--ink); font-size: 1.125rem; font-style: italic;">«Para eso ya tengo un asesor fiscal.»</p>
        </div>
        <p style="color: var(--text); line-height: 1.8; font-size: 1.125rem; margin-bottom: 1rem;">Y contar con especialistas seguirá siendo fundamental.</p>
        <p style="color: var(--text); line-height: 1.8; font-size: 1.125rem; margin-bottom: 1.5rem;">La diferencia está en poder detectar cuándo existe una cuestión fiscal, comprender su relevancia y participar en la conversación con conocimiento.</p>
        <div style="background: rgba(169, 24, 50, 0.05); padding: 1.5rem; border-radius: 8px;">
          <p style="font-weight: 700; color: var(--enae-granate); font-size: 1.25rem; margin: 0; text-align: center;">Preguntar mejor. Analizar mejor. Coordinarte mejor. Asesorar mejor.</p>
        </div>
      </div>

      <hr style="border: 0; height: 1px; background: #e5e7eb;">
      
      <div class="reveal">
        <h3 style="font-family: var(--font-serif); font-size: 2rem; color: var(--ink); margin-bottom: 0.5rem;">NO TIENES QUE DEDICARTE EXCLUSIVAMENTE A FISCAL.</h3>
        <h4 style="font-size: 1.5rem; font-weight: 300; color: var(--enae-granate); margin-bottom: 1.5rem;">Puedes hacer que la fiscalidad complemente tu especialidad.</h4>
        <p style="color: var(--text); line-height: 1.8; font-size: 1.125rem; margin-bottom: 1rem;">No necesitas cambiar de profesión. El conocimiento fiscal puede complementar tu práctica jurídica y ayudarte a abordar situaciones que ya forman parte de tu trabajo.</p>
        <p style="color: var(--text); line-height: 1.8; font-size: 1.125rem; margin-bottom: 1rem;">Porque la fiscalidad puede aparecer en muchas áreas del Derecho.</p>
        <p style="color: var(--text); line-height: 1.8; font-size: 1.125rem; margin-bottom: 1.5rem;"><strong>La cuestión no es convertirte en otra cosa.</strong></p>
        <p style="font-weight: 700; color: var(--ink); font-size: 1.25rem; margin: 0;">Es ampliar lo que puedes hacer como abogado.</p>
      </div>

      <hr style="border: 0; height: 1px; background: #e5e7eb;">

      <div class="reveal">
        <h3 style="font-family: var(--font-serif); font-size: 2rem; color: var(--ink); margin-bottom: 0.5rem;">¿Y LA INVERSIÓN?</h3>
        <p style="color: var(--text); line-height: 1.8; font-size: 1.125rem; margin-bottom: 1rem; margin-top: 1.5rem;">No podemos prometerte una determinada facturación ni un retorno económico concreto.</p>
        <p style="color: var(--text); line-height: 1.8; font-size: 1.125rem; margin-bottom: 2rem;">Pero sí podemos plantearte otra pregunta:</p>
        <h4 style="font-size: 1.5rem; font-weight: 700; color: var(--enae-granate); margin-bottom: 1.5rem; line-height: 1.4;">¿Qué valor tiene para tu carrera poder resolver problemas que hoy tienes que derivar?</h4>
        <p style="color: var(--text); line-height: 1.8; font-size: 1.125rem; margin-bottom: 1.5rem;">Una formación especializada no solo amplía tus conocimientos.</p>
        <div style="background: #111; color: #fff; padding: 2rem; border-radius: 12px; border: 1px solid rgba(212, 175, 55, 0.4);">
          <p style="font-weight: 700; line-height: 1.6; font-size: 1.25rem; margin: 0;">Amplía tu capacidad de análisis, tu conversación con otros profesionales y el valor que puedes aportar a tus clientes.</p>
        </div>
      </div>

    </div>
  </div>
</section>

<section class="final enae-wm enae-wm--final" id="solicitar">
  <div class="pattern" aria-hidden="true">
    <span class="b1"></span><span class="b2"></span><span class="b3"></span>
  </div>
  <div class="wrap" style="position:relative;z-index:2;">
    <div class="final-container">
      <div class="final-info reveal">
        <span class="eyebrow" style="margin-bottom:18px;">
          <span class="dot"></span> DERECHO + FISCALIDAD <span class="rule"></span>
        </span>
        <h2 class="mix" style="margin-bottom:20px; font-size:clamp(32px, 4vw, 54px);">
          <span class="t-bold">Una visión más</span>
          <span class="t-serif">completa del cliente.</span>
        </h2>
        <p class="lede-final">
          Tu próximo paso profesional puede empezar con una nueva perspectiva. No tienes que dejar de ser abogado para incorporar la fiscalidad a tu forma de asesorar.
        </p>
        <p class="lede-final" style="margin-top: 1rem; font-size: 1.125rem;">
          Solo necesitas comprender mejor una dimensión que ya está presente en muchas de las decisiones de tus clientes.
        </p>
        
        <div style="margin-top: 3rem; background: rgba(0,0,0,0.3); padding: 2rem; border-radius: 12px; border-left: 4px solid var(--enae-granate);">
          <h4 style="color: rgba(255,255,255,0.9); margin: 0 0 0.5rem; font-size: 1.125rem; font-weight: 300; text-transform: uppercase; letter-spacing: 1px;">No se trata de saber más.</h4>
          <h3 style="font-family: var(--font-serif); color: #fff; margin: 0; font-size: 2rem; line-height: 1.2;">SE TRATA DE PODER APORTAR MÁS.</h3>
        </div>
        
      </div>
      <div class="d-form-container reveal delay-1">
        <h3 style="margin: 0 0 1.25rem; font-size: 1.25rem; font-weight: 800; color: var(--ink);">Descubre si este Máster es para ti</h3>
        <p style="color: var(--text); font-size: 0.95rem; margin-bottom: 1.5rem; line-height: 1.5;">Déjanos tus datos y recibe toda la información sobre el programa, profesorado, becas y proceso de admisión.</p>
        <div data-form-id='90ea3a6e-104e-f111-bec7-7ced8d498631' data-form-api-url='https://public-eur.mkt.dynamics.com/api/v1.0/orgs/8bc28068-3b86-4b51-aa0e-5a151b861c76/landingpageforms' data-cached-form-url='https://assets-eur.mkt.dynamics.com/8bc28068-3b86-4b51-aa0e-5a151b861c76/digitalassets/forms/90ea3a6e-104e-f111-bec7-7ced8d498631'></div>
        <script src='https://formui-usa1.mkt.dynamics.com/eur/FormLoader/FormLoader.bundle.js'></script>
      </div>
    </div>
  </div>
</section>
"""

new_content = head_html + body_html + '\n' + foot_html

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Page regenerated successfully")
