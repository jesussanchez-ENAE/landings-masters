import re

with open('rrhh-direccion-humana.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Title
html = re.sub(
    r'<title>.*?</title>',
    '<title>Máster en Recursos Humanos, IA y Talento Digital · ENAE & Dirección Humana</title>',
    html
)

# 2. Update Hero Title & Copy
old_hero_title = r'<h1 class="hero-title mix">.*?</h1>'
new_hero_title = """<h1 class="hero-title mix" style="font-size: clamp(28px, 4vw, 48px); line-height: 1.15; margin-bottom: 1.5rem;">
        <span class="t-bold" style="display:block; margin-bottom: 0.5rem;">La nueva generación de profesionales de RRHH empieza ahora.</span>
        <span class="t-serif" style="display:block; color: #ffd7a0; font-size: clamp(20px, 2.5vw, 28px); margin-bottom: 0.5rem;">La Inteligencia Artificial está transformando la forma de atraer, desarrollar y gestionar el talento.</span>
        <span class="t-light" style="display:block; font-size: clamp(20px, 2.5vw, 28px);">¿Estás preparado para liderar ese cambio?</span>
      </h1>"""
html = re.sub(old_hero_title, new_hero_title, html, flags=re.DOTALL)

# Insert the description "Un programa para profesionales..." below the CTA row or above it.
# Actually, let's put it below the hero title, above the CTA.
description_text = """<p style="color: rgba(255,255,255,0.9); font-size: 1.15rem; line-height: 1.5; margin-bottom: 2rem; max-width: 65ch;">
        Un programa para profesionales que quieren evolucionar de la gestión tradicional de personas a una función de RRHH más estratégica, digital y basada en datos.
      </p>"""

html = html.replace('<div class="cta-row"', description_text + '\n      <div class="cta-row"')

# Update Master Name in Meta
html = html.replace('<span>Máster en</span><strong>Dirección de<br>Recursos Humanos</strong>', 
                    '<span>Máster en</span><strong>Recursos Humanos,<br>IA y Talento Digital</strong>')
html = html.replace('Dirección de Recursos Humanos', 'Recursos Humanos, IA y Talento Digital')

# 3. Update Destacado Banner for Beca 15%
old_banner = r'<div class="ia-banner reveal".*?</div>'
new_banner = """<div class="ia-banner reveal" style="background: linear-gradient(90deg, var(--enae-granate), #8c1025); color: #fff; padding: 1.5rem 2rem; text-align: center; margin: 0 auto 4rem; width: 90%; max-width: 1000px; border-radius: 12px; box-shadow: 0 12px 24px rgba(169, 24, 50, 0.15); display: flex; align-items: center; justify-content: center; gap: 1rem; flex-wrap: wrap; position:relative; z-index:10;">
  <span style="background: rgba(255,255,255,0.2); padding: 6px 12px; border-radius: 20px; font-weight: 700; font-size: 13px; letter-spacing: 0.5px; border: 1px solid rgba(255,255,255,0.3);">EXCLUSIVO DIRECCIÓN HUMANA</span>
  <span style="font-size: clamp(17px, 2vw, 21px); font-family: var(--font-serif); font-weight: 500; line-height: 1.3;">Siguiendo el compromiso de ENAE por formar a los mejores profesionales, ofrecemos un <strong>15% de beca exclusivo</strong> para asociados de <strong>Dirección Humana</strong>.</span>
</div>"""
html = re.sub(old_banner, new_banner, html, flags=re.DOTALL)

# 4. Replace Beneficios with "QUÉ VAS A CONSEGUIR?"
# Find the whole section id="beneficio"
old_beneficios = r'<section class="enae-wm enae-wm--beneficio" id="beneficio">.*?</section>'
new_beneficios = """<section class="enae-wm enae-wm--beneficio" id="beneficio" style="background: var(--surface); padding-top: 5rem; padding-bottom: 5rem;">
  <div class="wrap">
    <h2 class="mix reveal" style="margin-bottom:clamp(36px,4vw,56px); text-align: center;">
      <span class="t-bold">¿Qué vas a conseguir?</span>
    </h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
      
      <div class="reveal delay-1" style="background: #fff; padding: 2rem; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-top: 4px solid var(--enae-granate);">
        <div style="font-size: 2.5rem; margin-bottom: 1rem;">🤖</div>
        <h3 style="font-family: var(--font-serif); font-size: 1.25rem; margin-bottom: 1rem; color: var(--enae-negro);">Dominar la IA aplicada a RRHH</h3>
        <p style="color: var(--ink); line-height: 1.5;">Incorpora herramientas de IA a tus procesos y toma de decisiones.</p>
      </div>

      <div class="reveal delay-2" style="background: #fff; padding: 2rem; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-top: 4px solid var(--enae-granate);">
        <div style="font-size: 2.5rem; margin-bottom: 1rem;">📊</div>
        <h3 style="font-family: var(--font-serif); font-size: 1.25rem; margin-bottom: 1rem; color: var(--enae-negro);">Potenciar el talento con datos</h3>
        <p style="color: var(--ink); line-height: 1.5;">Aprende a utilizar People Analytics para convertir datos en decisiones.</p>
      </div>

      <div class="reveal delay-3" style="background: #fff; padding: 2rem; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-top: 4px solid var(--enae-granate);">
        <div style="font-size: 2.5rem; margin-bottom: 1rem;">🚀</div>
        <h3 style="font-family: var(--font-serif); font-size: 1.25rem; margin-bottom: 1rem; color: var(--enae-negro);">Liderar la transformación digital</h3>
        <p style="color: var(--ink); line-height: 1.5;">Prepárate para afrontar los nuevos retos de la función de Personas.</p>
      </div>

      <div class="reveal delay-1" style="background: #fff; padding: 2rem; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-top: 4px solid var(--enae-granate);">
        <div style="font-size: 2.5rem; margin-bottom: 1rem;">🎯</div>
        <h3 style="font-family: var(--font-serif); font-size: 1.25rem; margin-bottom: 1rem; color: var(--enae-negro);">Conectar personas y estrategia</h3>
        <p style="color: var(--ink); line-height: 1.5;">Desarrolla una visión de RRHH orientada al negocio y al futuro.</p>
      </div>

    </div>
  </div>
</section>"""
html = re.sub(old_beneficios, new_beneficios, html, flags=re.DOTALL)

with open('rrhh-direccion-humana.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Update completed.")
