import re

with open('rrhh-directivos.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update Title
old_title = """      <h1 class="hero-title mix">
        <span class="t-bold">El futuro de RRHH no se gestiona.</span>
        <span class="t-serif">Se anticipa.</span>
        <span class="t-light">Convierte los datos en decisiones estratégicas.</span>
      </h1>"""
new_title = """      <h1 class="hero-title mix">
        <span class="t-bold" style="font-size: clamp(24px, 3.5vw, 42px); line-height: 1.1; margin-bottom: 0.5rem; display: block;">Las decisiones sobre talento también son decisiones de negocio.</span>
        <span class="t-serif" style="color: #ffd7a0;">El talento cambia.</span>
        <span class="t-light" style="display: block; margin-top: 0.5rem;">La tecnología también.</span>
      </h1>"""
html = html.replace(old_title, new_title)

# Graphic replacement
old_visual_start = html.find('<div class="d-hero-visual reveal delay-1">')
old_visual_end = html.find('</div>\n    </div>\n  </div>\n</header>', old_visual_start)

if old_visual_start != -1 and old_visual_end != -1:
    new_visual = """<div class="d-hero-visual reveal delay-1" style="display: flex; align-items: center; justify-content: center; height: 100%;">
      <div style="background: rgba(25, 25, 25, 0.7); border: 1px solid rgba(255,255,255,0.15); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); padding: 2rem; border-radius: 16px; width: 100%; max-width: 450px; box-shadow: 0 20px 40px rgba(0,0,0,0.4);">
        
        <div style="margin-bottom: 2rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 1.5rem;">
          <div style="display: flex; align-items: baseline; gap: 0.5rem; margin-bottom: 0.5rem;">
            <span style="font-size: 3.5rem; font-weight: 800; color: #ffd7a0; line-height: 1; letter-spacing: -1px;">39%</span>
          </div>
          <p style="color: #fff; font-size: 1.1rem; line-height: 1.4; font-weight: 500; margin-bottom: 1rem;">
            de las habilidades clave cambiarán de aquí a 2030.
          </p>
          <p style="color: rgba(255,255,255,0.5); font-size: 0.75rem; line-height: 1.4; margin: 0;">
            Fuente: World Economic Forum, Future of Jobs Report 2025.
          </p>
        </div>
        
        <div>
          <div style="display: flex; align-items: baseline; gap: 0.5rem; margin-bottom: 0.5rem;">
            <span style="font-size: 3.5rem; font-weight: 800; color: #fff; line-height: 1; letter-spacing: -1px;">63%</span>
          </div>
          <p style="color: rgba(255,255,255,0.9); font-size: 1.1rem; line-height: 1.4; font-weight: 500; margin-bottom: 1rem;">
            de los empleadores considera la brecha de habilidades una de las principales barreras para transformar su negocio.
          </p>
          <a href="https://www.weforum.org/press/2025/01/future-of-jobs-report-2025-78-million-new-job-opportunities-by-2030-but-urgent-upskilling-needed-to-prepare-workforces//?utm_source=chatgpt.com" target="_blank" rel="noopener noreferrer" style="color: rgba(255,255,255,0.5); font-size: 0.75rem; line-height: 1.4; text-decoration: underline;">
            Fuente: Informe de Riesgos WEF
          </a>
        </div>
        
      </div>
      """
    html = html[:old_visual_start] + new_visual + html[old_visual_end:]

with open('rrhh-directivos.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updates applied to rrhh-directivos.html.")

