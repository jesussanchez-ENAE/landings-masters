import sys
import re

file_path = 'asesoria-fiscal-colegio-abogados.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We will replace everything from `<header class="hero d-hero enae-wm enae-wm--hero"` down to `<footer>`
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

body_html = """<header class="hero d-hero enae-wm enae-wm--hero" style="background: url('./src/img/hero_asesoria_fiscal_directivos.jpg') no-repeat center center; background-size: cover; position: relative; min-height: 90vh; display: flex; align-items: center; justify-content: center; text-align: center;">
  <div class="pattern" aria-hidden="true" style="opacity: 0.5;">
    <span class="b1"></span><span class="b2"></span><span class="b3"></span><span class="b4"></span><span class="b5"></span>
  </div>
  <div class="wrap reveal" style="position: relative; z-index: 2; max-width: 1000px; padding-top: 80px;">
    <span class="eyebrow" style="margin-bottom:24px; justify-content: center;">
      <span class="dot"></span> ¿LA PARTE FISCAL TIENES QUE CONSULTARLA? <span class="rule" style="display: none;"></span>
    </span>
    <h1 class="hero-title mix" style="font-size: clamp(40px, 6vw, 72px); line-height: 1.1; margin-bottom: 32px;">
      <span class="t-bold">Añade la perspectiva fiscal a</span><br>
      <span class="t-serif" style="color: #fff;">tu conocimiento jurídico.</span>
    </h1>
    <p style="font-size: clamp(1.125rem, 2vw, 1.5rem); font-weight: 300; line-height: 1.6; color: rgba(255,255,255,0.9); max-width: 700px; margin: 0 auto 3rem;">
      <strong>Máster en Asesoría Fiscal de ENAE Business School</strong><br>
      Amplía tu capacidad de análisis y aporta más valor a tus clientes.
    </p>
    
    <div style="display: flex; gap: 1.5rem; justify-content: center; flex-wrap: wrap; margin-bottom: 4rem;">
      <a href="#solicitar" class="btn" style="padding: 1rem 2.5rem; font-size: 1.125rem;">Solicita información <span class="arrow">&rarr;</span></a>
      <a href="#programa" class="btn ghost" style="padding: 1rem 2.5rem; font-size: 1.125rem; border-color: rgba(255,255,255,0.3);">Ver el programa</a>
    </div>

    <div class="d-hero-meta" style="justify-content: center; flex-wrap: wrap; gap: 2rem; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 2rem;">
      <div style="text-align: center;"><span>Máster en</span><strong>Asesoría Fiscal</strong></div>
      <div style="text-align: center;"><span>Edición</span><strong>36ª edición</strong></div>
      <div style="text-align: center;"><span>Duración</span><strong>60 ECTS</strong></div>
      <div style="text-align: center;"><span>Inicio</span><strong>19 oct 2026</strong></div>
    </div>
  </div>
</header>

<!-- BANNER DESTACADO BECAS -->
<div class="ia-banner reveal" style="background: #111; color: #fff; padding: 1.5rem 2rem; text-align: center; margin: -2.5rem auto 5rem; width: 90%; max-width: 1000px; border-radius: 16px; box-shadow: 0 24px 48px rgba(0, 0, 0, 0.4); display: flex; align-items: center; justify-content: center; gap: 1.5rem; flex-wrap: wrap; position:relative; z-index:10; border: 1px solid rgba(212, 175, 55, 0.3);">
  <span style="background: linear-gradient(135deg, #dfc26a, #c09d3b); color: #111; padding: 6px 16px; border-radius: 30px; font-weight: 800; font-size: 13px; letter-spacing: 1px; text-transform: uppercase;">Exclusivo Colegiados</span>
  <span style="font-size: clamp(17px, 2vw, 21px); font-family: var(--font-serif); font-weight: 400; line-height: 1.3;">Disfruta de una <strong>beca del 20%</strong> exclusiva para miembros del <strong>Colegio de Abogados de la Región de Murcia</strong>.</span>
</div>

<!-- SECTION 1: CONTEXT (Image + Text) -->
<section class="enae-wm" style="padding: 4rem 0 8rem; background: var(--surface);">
  <div class="wrap">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6rem; align-items: center;">
      <div class="reveal">
        <h2 class="mix" style="margin-bottom: 2.5rem; font-size: clamp(2.5rem, 4vw, 3.5rem); line-height: 1.1;">
          <span class="t-bold" style="color: var(--ink);">Tu cliente no ve</span><br>
          <span class="t-serif" style="color: var(--enae-granate);">la parte jurídica y la fiscal por separado.</span>
        </h2>
        <div style="font-size: 1.125rem; line-height: 1.8; color: var(--text);">
          <ul style="list-style: none; padding: 0; margin: 0 0 2rem; border-left: 1px solid #e5e7eb; padding-left: 2rem;">
            <li style="margin-bottom: 1rem; position: relative;">Una compraventa no es solo un contrato.</li>
            <li style="margin-bottom: 1rem; position: relative;">Una reestructuración no es solo una operación societaria.</li>
            <li style="margin-bottom: 0; position: relative;">Una sucesión no es solo una cuestión patrimonial.</li>
          </ul>
          <p style="margin-bottom: 2rem; font-weight: 700; font-size: 1.375rem; color: var(--ink); line-height: 1.4;">Muchas de las decisiones que asesores jurídicamente tienen también consecuencias fiscales.</p>
          <p style="margin-bottom: 3rem;">Y cuanto mejor comprendas ambas dimensiones, mejor podrás analizar la operación en su conjunto.</p>
          <div style="background: #fff; padding: 2rem; border-radius: 12px; border-left: 4px solid var(--enae-granate); box-shadow: 0 10px 30px rgba(0,0,0,0.03);">
            <h3 style="font-family: var(--font-serif); font-size: 1.5rem; color: var(--enae-granate); margin: 0 0 0.5rem;">Porque conocer la ley es fundamental.</h3>
            <p style="font-weight: 700; color: var(--ink); margin: 0; font-size: 1.125rem;">Entender su impacto fiscal puede marcar la diferencia.</p>
          </div>
        </div>
      </div>
      <div class="reveal delay-1" style="position: relative;">
        <div style="position: absolute; top: -2rem; left: -2rem; width: 100%; height: 100%; border: 1px solid var(--enae-granate); border-radius: 24px; opacity: 0.2;"></div>
        <img src="./src/img/10042023-317A8104.jpg" alt="Profesionales en ENAE" style="width: 100%; border-radius: 24px; box-shadow: 0 24px 60px rgba(0,0,0,0.15); position: relative; z-index: 2; object-fit: cover; aspect-ratio: 4/5;">
      </div>
    </div>
  </div>
</section>

<!-- SECTION 2: PAIN POINTS (Dark background) -->
<section class="enae-wm" style="padding: 8rem 0; background: var(--enae-negro); color: #fff; position: relative; overflow: hidden;">
  <div style="position: absolute; top: 0; right: 0; width: 50%; height: 100%; background: url('./src/img/10042023-317A7390.jpg') no-repeat center center; background-size: cover; opacity: 0.1; mask-image: linear-gradient(to right, transparent, black); -webkit-mask-image: linear-gradient(to right, transparent, black);"></div>
  <div class="wrap" style="position: relative; z-index: 2;">
    <div style="max-width: 600px;">
      <span class="eyebrow" style="margin-bottom:1rem; color: rgba(255,255,255,0.5);">El reto actual</span>
      <h2 class="mix reveal" style="margin-bottom: 3rem;">
        <span class="t-bold" style="color: #fff;">¿Cuánto de tu asesoramiento</span><br>
        <span class="t-serif" style="color: var(--enae-granate);">depende hoy de otros especialistas?</span>
      </h2>
      <p class="reveal delay-1" style="font-size: 1.25rem; line-height: 1.6; color: rgba(255,255,255,0.7); margin-bottom: 1rem;">No se trata de sustituir al asesor fiscal.</p>
      <p class="reveal delay-1" style="font-size: 1.75rem; font-family: var(--font-serif); color: #fff; line-height: 1.4; margin-bottom: 3rem;">
        Se trata de <strong>entender la fiscalidad</strong> lo suficiente como para <span style="color: var(--enae-granate);">participar en la conversación con criterio.</span>
      </p>
      
      <div class="reveal delay-2" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); padding: 3rem; border-radius: 16px; backdrop-filter: blur(10px);">
        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1.5rem;">
          <li style="display: flex; gap: 1rem; align-items: flex-start; color: rgba(255,255,255,0.9); font-size: 1.125rem;">
            <span style="color: var(--enae-granate); font-weight: 800;">01.</span>
            <span>Para detectar las preguntas adecuadas.</span>
          </li>
          <li style="display: flex; gap: 1rem; align-items: flex-start; color: rgba(255,255,255,0.9); font-size: 1.125rem;">
            <span style="color: var(--enae-granate); font-weight: 800;">02.</span>
            <span>Para identificar posibles implicaciones tributarias.</span>
          </li>
          <li style="display: flex; gap: 1rem; align-items: flex-start; color: rgba(255,255,255,0.9); font-size: 1.125rem;">
            <span style="color: var(--enae-granate); font-weight: 800;">03.</span>
            <span>Para entender las alternativas y anticiparte.</span>
          </li>
          <li style="display: flex; gap: 1rem; align-items: flex-start; color: #fff; font-size: 1.25rem; font-weight: 700; margin-top: 1rem; padding-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.1);">
            <span style="color: var(--enae-granate);">→</span>
            <span>Y para ofrecer a tu cliente una visión más completa.</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- SECTION 3: BEFORE / AFTER -->
<section class="enae-wm" style="padding: 8rem 0; background: #fff;">
  <div class="wrap">
    <div style="text-align: center; margin-bottom: 5rem; max-width: 800px; margin-inline: auto;">
      <h2 class="mix reveal">
        <span class="t-bold">AMPLÍA LO QUE PUEDES</span>
        <span class="t-serif">HACER POR TUS CLIENTES</span>
      </h2>
    </div>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 3rem; max-width: 1100px; margin: 0 auto;">
      <!-- Antes -->
      <div class="reveal delay-1" style="background: var(--surface); padding: 4rem 3rem; border-radius: 24px; border: 1px solid #e5e7eb;">
        <h3 style="font-family: var(--font-serif); font-size: 2.5rem; color: #9ca3af; margin-bottom: 1.5rem; opacity: 0.5;">Antes</h3>
        <p style="font-weight: 700; color: var(--ink); margin-bottom: 2.5rem; font-size: 1.25rem; line-height: 1.5;">Tu conocimiento jurídico es el punto de partida. Pero ante determinadas operaciones:</p>
        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1.5rem; color: var(--text);">
          <li style="display: flex; gap: 1.25rem; align-items: flex-start;">
            <div style="width: 24px; height: 24px; border-radius: 50%; background: #e5e7eb; color: #6b7280; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 800; flex-shrink: 0; margin-top: 4px;">✕</div>
            <span style="font-size: 1.125rem; line-height: 1.5;">Tienes que consultar sus implicaciones fiscales.</span>
          </li>
          <li style="display: flex; gap: 1.25rem; align-items: flex-start;">
            <div style="width: 24px; height: 24px; border-radius: 50%; background: #e5e7eb; color: #6b7280; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 800; flex-shrink: 0; margin-top: 4px;">✕</div>
            <span style="font-size: 1.125rem; line-height: 1.5;">Hay cuestiones que necesitas derivar a otros especialistas.</span>
          </li>
          <li style="display: flex; gap: 1.25rem; align-items: flex-start;">
            <div style="width: 24px; height: 24px; border-radius: 50%; background: #e5e7eb; color: #6b7280; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 800; flex-shrink: 0; margin-top: 4px;">✕</div>
            <span style="font-size: 1.125rem; line-height: 1.5;">Parte del análisis queda fuera de tu ámbito.</span>
          </li>
          <li style="display: flex; gap: 1.25rem; align-items: flex-start;">
            <div style="width: 24px; height: 24px; border-radius: 50%; background: #e5e7eb; color: #6b7280; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 800; flex-shrink: 0; margin-top: 4px;">✕</div>
            <span style="font-size: 1.125rem; line-height: 1.5;">Puedes necesitar apoyo para valorar alternativas.</span>
          </li>
        </ul>
      </div>
      
      <!-- Después -->
      <div class="reveal delay-2" style="background: #fff; padding: 4rem 3rem; border-radius: 24px; box-shadow: 0 40px 80px rgba(169, 24, 50, 0.08); position: relative; border: 1px solid rgba(169, 24, 50, 0.1);">
        <div style="position: absolute; top: -16px; left: 3rem; background: var(--enae-granate); color: #fff; padding: 8px 24px; border-radius: 30px; font-weight: 800; font-size: 0.875rem; letter-spacing: 1px; text-transform: uppercase;">Con el Máster</div>
        <h3 style="font-family: var(--font-serif); font-size: 2.5rem; color: var(--enae-granate); margin-bottom: 1.5rem;">Después</h3>
        <p style="font-weight: 700; color: var(--ink); margin-bottom: 2.5rem; font-size: 1.25rem; line-height: 1.5;">Incorporas la perspectiva fiscal a tu análisis jurídico.</p>
        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1.5rem; color: var(--ink);">
          <li style="display: flex; gap: 1.25rem; align-items: flex-start;">
            <div style="width: 24px; height: 24px; border-radius: 50%; background: rgba(169, 24, 50, 0.1); color: var(--enae-granate); display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 800; flex-shrink: 0; margin-top: 4px;">✓</div>
            <span style="font-size: 1.125rem; line-height: 1.5;">Comprendes mejor las consecuencias tributarias.</span>
          </li>
          <li style="display: flex; gap: 1.25rem; align-items: flex-start;">
            <div style="width: 24px; height: 24px; border-radius: 50%; background: rgba(169, 24, 50, 0.1); color: var(--enae-granate); display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 800; flex-shrink: 0; margin-top: 4px;">✓</div>
            <span style="font-size: 1.125rem; line-height: 1.5;">Detectas implicaciones antes de tomar decisiones.</span>
          </li>
          <li style="display: flex; gap: 1.25rem; align-items: flex-start;">
            <div style="width: 24px; height: 24px; border-radius: 50%; background: rgba(169, 24, 50, 0.1); color: var(--enae-granate); display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 800; flex-shrink: 0; margin-top: 4px;">✓</div>
            <span style="font-size: 1.125rem; line-height: 1.5;">Puedes plantear mejores preguntas y alternativas.</span>
          </li>
          <li style="display: flex; gap: 1.25rem; align-items: flex-start;">
            <div style="width: 24px; height: 24px; border-radius: 50%; background: rgba(169, 24, 50, 0.1); color: var(--enae-granate); display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 800; flex-shrink: 0; margin-top: 4px;">✓</div>
            <span style="font-size: 1.125rem; line-height: 1.5;">Te comunicas con mayor criterio con asesores.</span>
          </li>
          <li style="display: flex; gap: 1.25rem; align-items: flex-start;">
            <div style="width: 24px; height: 24px; border-radius: 50%; background: var(--enae-granate); color: #fff; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 800; flex-shrink: 0; margin-top: 4px; box-shadow: 0 4px 12px rgba(169, 24, 50, 0.3);">✓</div>
            <span style="font-size: 1.125rem; line-height: 1.5; font-weight: 700;">Aportas una visión más completa al cliente.</span>
          </li>
        </ul>
      </div>
    </div>
    
    <div class="reveal delay-3" style="text-align: center; margin-top: 6rem;">
      <h3 style="font-size: 1.5rem; font-weight: 300; color: var(--text); margin-bottom: 0.5rem;">No tienes que cambiar de profesión.</h3>
      <h2 style="font-family: var(--font-serif); font-size: clamp(2rem, 4vw, 3rem); color: var(--ink); margin: 0;">Tienes que ampliar tu perspectiva.</h2>
    </div>
  </div>
</section>

<!-- SECTION 4: USE CASES (Image + Tags) -->
<section class="enae-wm" style="padding: 8rem 0; background: var(--surface);">
  <div class="wrap">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6rem; align-items: center;">
      <div class="reveal delay-1" style="order: 2;">
        <h2 class="mix" style="margin-bottom: 1.5rem;">
          <span class="t-bold">Tus clientes ya necesitan</span><br>
          <span class="t-serif">asesoramiento fiscal.</span>
        </h2>
        <p style="font-size: 1.25rem; font-weight: 700; color: var(--ink); margin-bottom: 3rem;">La cuestión es quién participa en esa conversación.</p>
        
        <p style="font-size: 1.125rem; color: var(--text); margin-bottom: 2rem;">Dentro de tu propia cartera de clientes ya existen decisiones con una dimensión fiscal:</p>
        
        <div style="display: flex; flex-wrap: wrap; gap: 1rem; margin-bottom: 3rem;">
          <span style="background: #fff; padding: 10px 20px; border-radius: 8px; font-weight: 700; color: var(--ink); font-size: 0.875rem; border: 1px solid #e5e7eb; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">Operaciones societarias</span>
          <span style="background: #fff; padding: 10px 20px; border-radius: 8px; font-weight: 700; color: var(--ink); font-size: 0.875rem; border: 1px solid #e5e7eb; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">Compraventas</span>
          <span style="background: #fff; padding: 10px 20px; border-radius: 8px; font-weight: 700; color: var(--ink); font-size: 0.875rem; border: 1px solid #e5e7eb; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">Contratos</span>
          <span style="background: #fff; padding: 10px 20px; border-radius: 8px; font-weight: 700; color: var(--ink); font-size: 0.875rem; border: 1px solid #e5e7eb; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">Sucesiones y donaciones</span>
          <span style="background: #fff; padding: 10px 20px; border-radius: 8px; font-weight: 700; color: var(--ink); font-size: 0.875rem; border: 1px solid #e5e7eb; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">Inversiones</span>
          <span style="background: #fff; padding: 10px 20px; border-radius: 8px; font-weight: 700; color: var(--ink); font-size: 0.875rem; border: 1px solid #e5e7eb; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">Patrimonio</span>
          <span style="background: #fff; padding: 10px 20px; border-radius: 8px; font-weight: 700; color: var(--ink); font-size: 0.875rem; border: 1px solid #e5e7eb; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">Retribuciones</span>
        </div>
        
        <div style="background: rgba(169, 24, 50, 0.05); padding: 2rem; border-radius: 12px; border-left: 4px solid var(--enae-granate);">
          <p style="font-size: 1.125rem; line-height: 1.6; color: var(--text); margin: 0;">
            Incorporar conocimientos avanzados de fiscalidad puede ayudarte a <strong style="color: var(--enae-granate);">ampliar los problemas que eres capaz de analizar</strong> y a participar en operaciones donde la dimensión jurídica y fiscal están estrechamente relacionadas.
          </p>
        </div>
      </div>
      
      <div class="reveal" style="order: 1;">
        <img src="./src/img/10042023-317A7711.jpg" alt="Networking ENAE" style="width: 100%; border-radius: 24px; box-shadow: 0 30px 60px rgba(0,0,0,0.1); object-fit: cover; aspect-ratio: 4/5;">
      </div>
    </div>
  </div>
</section>

<!-- SECTION 5: THE PROGRAM & DATA -->
<section class="enae-wm" style="padding: 8rem 0; background: #fff;" id="programa">
  <div class="wrap">
    <div style="text-align: center; margin-bottom: 5rem; max-width: 800px; margin-inline: auto;">
      <h2 class="mix reveal">
        <span class="t-bold">LO QUE APRENDES.</span>
        <span class="t-serif">LO QUE PUEDES HACER CON ELLO.</span>
      </h2>
      <p class="reveal delay-1" style="font-size: 1.25rem; color: var(--text); margin-top: 1.5rem; line-height: 1.6;">Una formación especializada para profesionales que quieren comprender la fiscalidad aplicada a las decisiones empresariales y patrimoniales.</p>
    </div>
    
    <div class="reveal delay-2" style="background: #fff; border-radius: 24px; border: 1px solid #e5e7eb; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.04); margin-bottom: 5rem; max-width: 1000px; margin-inline: auto;">
      <div style="overflow-x: auto;">
        <table style="width: 100%; border-collapse: collapse; text-align: left; min-width: 600px;">
          <thead>
            <tr style="background: var(--surface); border-bottom: 2px solid #e5e7eb;">
              <th style="padding: 2rem; font-weight: 800; font-size: 1.25rem; width: 45%; color: var(--ink);">El Máster en Asesoría Fiscal</th>
              <th style="padding: 2rem; font-weight: 800; font-size: 1.25rem; color: var(--ink);">Lo que aporta a tu práctica jurídica</th>
            </tr>
          </thead>
          <tbody style="color: var(--ink);">
            <tr style="border-bottom: 1px solid #f3f4f6;">
              <td style="padding: 1.5rem 2rem; font-weight: 700; font-size: 1.125rem;">Formación fiscal especializada</td>
              <td style="padding: 1.5rem 2rem; color: var(--text); font-size: 1.125rem;">Comprender la dimensión tributaria de las operaciones</td>
            </tr>
            <tr style="border-bottom: 1px solid #f3f4f6; background: #fafafa;">
              <td style="padding: 1.5rem 2rem; font-weight: 700; font-size: 1.125rem;">Claustro de profesionales</td>
              <td style="padding: 1.5rem 2rem; color: var(--text); font-size: 1.125rem;">Aprender desde la experiencia y la práctica real diaria</td>
            </tr>
            <tr style="border-bottom: 1px solid #f3f4f6;">
              <td style="padding: 1.5rem 2rem; font-weight: 700; font-size: 1.125rem;">Metodología del Caso</td>
              <td style="padding: 1.5rem 2rem; color: var(--text); font-size: 1.125rem;">Aplicar la teoría a situaciones y convertirlas en criterio aplicable</td>
            </tr>
            <tr style="border-bottom: 1px solid #f3f4f6; background: #fafafa;">
              <td style="padding: 1.5rem 2rem; font-weight: 700; font-size: 1.125rem;">Formación presencial / híbrida</td>
              <td style="padding: 1.5rem 2rem; color: var(--text); font-size: 1.125rem;">Crear relaciones y compartir experiencias profesionales</td>
            </tr>
            <tr style="border-bottom: 1px solid #f3f4f6;">
              <td style="padding: 1.5rem 2rem; font-weight: 700; font-size: 1.125rem;">Visión empresarial integral</td>
              <td style="padding: 1.5rem 2rem; color: var(--text); font-size: 1.125rem;">Comprender al cliente corporativo más allá del expediente</td>
            </tr>
            <tr style="border-bottom: 1px solid #f3f4f6; background: #fafafa;">
              <td style="padding: 1.5rem 2rem; font-weight: 700; font-size: 1.125rem;">Diversidad de perfiles</td>
              <td style="padding: 1.5rem 2rem; color: var(--text); font-size: 1.125rem;">Entender cómo piensan economistas y financieros en la operación</td>
            </tr>
            <tr>
              <td style="padding: 1.5rem 2rem; font-weight: 700; font-size: 1.125rem; color: var(--enae-granate);">Titulación ENAE Business School</td>
              <td style="padding: 1.5rem 2rem; color: var(--text); font-size: 1.125rem;">Reforzar tu perfil y posicionamiento en el mercado</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Data cards -->
    <div class="reveal delay-3" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 2rem; max-width: 1000px; margin-inline: auto;">
      <div style="background: var(--surface); padding: 2.5rem 2rem; border-radius: 16px; text-align: center;">
        <div style="font-size: 0.875rem; color: var(--text); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.75rem; font-weight: 700;">Inicio</div>
        <div style="font-size: 1.75rem; font-weight: 800; color: var(--ink);">19 octubre 2026</div>
      </div>
      <div style="background: var(--surface); padding: 2.5rem 2rem; border-radius: 16px; text-align: center;">
        <div style="font-size: 0.875rem; color: var(--text); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.75rem; font-weight: 700;">Créditos</div>
        <div style="font-size: 1.75rem; font-weight: 800; color: var(--ink);">60 ECTS</div>
      </div>
      <div style="background: var(--surface); padding: 2.5rem 2rem; border-radius: 16px; text-align: center;">
        <div style="font-size: 0.875rem; color: var(--text); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.75rem; font-weight: 700;">Modalidad</div>
        <div style="font-size: 1.75rem; font-weight: 800; color: var(--ink);">Presencial</div>
      </div>
      <div style="background: var(--surface); padding: 2.5rem 2rem; border-radius: 16px; text-align: center;">
        <div style="font-size: 0.875rem; color: var(--text); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.75rem; font-weight: 700;">Horarios</div>
        <div style="font-size: 1.75rem; font-weight: 800; color: var(--ink);">Fines de semana</div>
      </div>
    </div>
  </div>
</section>

<!-- SECTION 6: OBJECTIONS (Split Layout) -->
<section class="enae-wm" style="padding: 8rem 0; background: var(--surface);">
  <div class="wrap">
    <div style="display: grid; grid-template-columns: 1fr 1.2fr; gap: 6rem; max-width: 1200px; margin: 0 auto; align-items: start;">
      
      <div class="reveal" style="position: sticky; top: 120px;">
        <h2 class="mix" style="margin-bottom: 2rem;">
          <span class="t-bold">Respuestas a</span><br>
          <span class="t-serif">tus dudas.</span>
        </h2>
        <p style="font-size: 1.25rem; color: var(--text); line-height: 1.6;">Es natural preguntarse si un programa fiscal encaja en un perfil puramente jurídico. La respuesta corta es sí.</p>
        <img src="./src/img/10042023-317A8264.jpg" alt="Detalle ENAE" style="width: 100%; border-radius: 16px; margin-top: 3rem; box-shadow: 0 20px 40px rgba(0,0,0,0.08); aspect-ratio: 16/9; object-fit: cover;">
      </div>

      <div>
        <div class="reveal" style="background: #fff; padding: 3rem; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.03); margin-bottom: 2rem;">
          <h3 style="font-family: var(--font-serif); font-size: 1.75rem; color: var(--ink); margin-bottom: 0.5rem;">NO NECESITAS SER ECONOMISTA.</h3>
          <h4 style="font-size: 1.25rem; font-weight: 400; color: var(--enae-granate); margin-bottom: 1.5rem;">Necesitas entender mejor la operación.</h4>
          <div style="border-left: 4px solid var(--enae-gris-claro); padding-left: 1.5rem; margin-bottom: 1.5rem;">
            <p style="font-weight: 700; color: var(--ink); font-size: 1.125rem; font-style: italic; margin: 0;">«Yo soy abogado, no economista.»</p>
          </div>
          <p style="color: var(--text); line-height: 1.7; font-size: 1.125rem; margin-bottom: 1rem;">Precisamente por eso tu conocimiento jurídico es una base especialmente valiosa.</p>
          <p style="color: var(--text); line-height: 1.7; font-size: 1.125rem; margin-bottom: 1rem;">El objetivo no es convertirte en economista. Es <strong>incorporar la perspectiva tributaria a la forma en la que ya analizas las operaciones.</strong> Tu especialidad sigue siendo el Derecho. Ahora puedes añadir una nueva dimensión a tu análisis.</p>
        </div>
        
        <div class="reveal" style="background: #fff; padding: 3rem; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.03); margin-bottom: 2rem;">
          <h3 style="font-family: var(--font-serif); font-size: 1.75rem; color: var(--ink); margin-bottom: 0.5rem;">NO SE TRATA DE SUSTITUIR AL ASESOR FISCAL.</h3>
          <h4 style="font-size: 1.25rem; font-weight: 400; color: var(--enae-granate); margin-bottom: 1.5rem;">Se trata de entenderlo mejor.</h4>
          <div style="border-left: 4px solid var(--enae-gris-claro); padding-left: 1.5rem; margin-bottom: 1.5rem;">
            <p style="font-weight: 700; color: var(--ink); font-size: 1.125rem; font-style: italic; margin: 0;">«Para eso ya tengo un asesor fiscal.»</p>
          </div>
          <p style="color: var(--text); line-height: 1.7; font-size: 1.125rem; margin-bottom: 1.5rem;">Y contar con especialistas seguirá siendo fundamental. La diferencia está en poder detectar cuándo existe una cuestión fiscal, comprender su relevancia y participar en la conversación con conocimiento.</p>
          <div style="background: rgba(169, 24, 50, 0.05); padding: 1.5rem; border-radius: 8px;">
            <p style="font-weight: 700; color: var(--enae-granate); font-size: 1.125rem; margin: 0; text-align: center;">Preguntar mejor. Analizar mejor. Coordinarte mejor. Asesorar mejor.</p>
          </div>
        </div>
        
        <div class="reveal" style="background: #fff; padding: 3rem; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.03); margin-bottom: 2rem;">
          <h3 style="font-family: var(--font-serif); font-size: 1.75rem; color: var(--ink); margin-bottom: 0.5rem;">NO TIENES QUE DEDICARTE EXCLUSIVAMENTE A FISCAL.</h3>
          <h4 style="font-size: 1.25rem; font-weight: 400; color: var(--enae-granate); margin-bottom: 1.5rem;">Complementa tu especialidad.</h4>
          <p style="color: var(--text); line-height: 1.7; font-size: 1.125rem; margin-bottom: 1rem;">No necesitas cambiar de profesión. El conocimiento fiscal puede complementar tu práctica jurídica y ayudarte a abordar situaciones que ya forman parte de tu trabajo. Porque la fiscalidad puede aparecer en muchas áreas del Derecho.</p>
          <p style="font-weight: 700; color: var(--ink); font-size: 1.125rem; margin: 0;">La cuestión no es convertirte en otra cosa. Es ampliar lo que puedes hacer como abogado.</p>
        </div>

        <div class="reveal" style="background: var(--enae-negro); padding: 3rem; border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.2); color: #fff;">
          <h3 style="font-family: var(--font-serif); font-size: 1.75rem; color: #fff; margin-bottom: 1rem;">¿Y LA INVERSIÓN?</h3>
          <p style="color: rgba(255,255,255,0.8); line-height: 1.7; font-size: 1.125rem; margin-bottom: 2rem;">No podemos prometerte una determinada facturación ni un retorno económico concreto. Pero sí podemos plantearte otra pregunta:</p>
          <h4 style="font-size: 1.5rem; font-weight: 700; color: var(--enae-granate); margin-bottom: 1.5rem; line-height: 1.4;">¿Qué valor tiene para tu carrera poder resolver problemas que hoy tienes que derivar?</h4>
          <p style="color: rgba(255,255,255,0.8); line-height: 1.7; font-size: 1.125rem; margin-bottom: 0;">Una formación especializada no solo amplía tus conocimientos. <strong style="color: #fff;">Amplía tu capacidad de análisis, tu conversación con otros profesionales y el valor que puedes aportar a tus clientes.</strong></p>
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
    <div class="final-container" style="grid-template-columns: 1fr 1fr; align-items: center; gap: 4rem;">
      <div class="final-info reveal">
        <span class="eyebrow" style="margin-bottom:18px;">
          <span class="dot"></span> DERECHO + FISCALIDAD <span class="rule"></span>
        </span>
        <h2 class="mix" style="margin-bottom:24px; font-size:clamp(32px, 4vw, 54px);">
          <span class="t-bold">Una visión más</span>
          <span class="t-serif">completa del cliente.</span>
        </h2>
        <p class="lede-final" style="font-size: 1.25rem;">
          Tu próximo paso profesional puede empezar con una nueva perspectiva. No tienes que dejar de ser abogado para incorporar la fiscalidad a tu forma de asesorar.
        </p>
        <p class="lede-final" style="margin-top: 1rem; font-size: 1.25rem;">
          Solo necesitas comprender mejor una dimensión que ya está presente en muchas de las decisiones de tus clientes.
        </p>
        
        <div style="margin-top: 3rem; background: rgba(0,0,0,0.3); padding: 2.5rem; border-radius: 16px; border-left: 4px solid var(--enae-granate); backdrop-filter: blur(10px);">
          <h4 style="color: rgba(255,255,255,0.8); margin: 0 0 0.5rem; font-size: 1.125rem; font-weight: 400; text-transform: uppercase; letter-spacing: 1px;">No se trata de saber más.</h4>
          <h3 style="font-family: var(--font-serif); color: #fff; margin: 0; font-size: 2.25rem; line-height: 1.2;">SE TRATA DE PODER APORTAR MÁS.</h3>
        </div>
        
      </div>
      <div class="d-form-container reveal delay-1" style="background:#fff; padding: 3rem; border-radius: 20px; box-shadow: 0 40px 80px rgba(0,0,0,0.2); width:100%; max-width:560px;">
        <h3 style="margin: 0 0 1rem; font-size: 1.75rem; font-weight: 800; color: var(--ink);">Descubre si este Máster es para ti</h3>
        <p style="color: var(--text); font-size: 1rem; margin-bottom: 2rem; line-height: 1.6;">Déjanos tus datos y recibe toda la información sobre el programa, profesorado, becas y proceso de admisión.</p>
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

print("Impeccable page regenerated successfully")
