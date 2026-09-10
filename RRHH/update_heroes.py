import re

# Updates for CEOs
with open('rrhh-ceos.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update background image
html = re.sub(
    r"url\('\./src/img/hero_finanzas_ceos_\.jpg'\)", 
    r"url('./src/img/hero_rrhh_ceos.jpg')", 
    html
)

# Update Title
old_title = """      <h1 class="hero-title mix">
        <span class="t-bold">Te pagan por controlar.</span>
        <span class="t-serif">Pero te necesitan para decidir.</span>
        <span class="t-light">Da el salto del control financiero a la estrategia.</span>
      </h1>"""
new_title = """      <h1 class="hero-title mix">
        <span class="t-bold">El futuro de RRHH no se gestiona.</span>
        <span class="t-serif">Se anticipa.</span>
        <span class="t-light">Convierte los datos en decisiones estratégicas.</span>
      </h1>"""
html = html.replace(old_title, new_title)

# Update Master Name
html = html.replace("Finanzas, Fintech y<br>Control Estratégico", "Dirección de<br>Recursos Humanos")
html = html.replace("Finanzas, Fintech y Control Estratégico", "Dirección de Recursos Humanos")

# Write CEOs
with open('rrhh-ceos.html', 'w', encoding='utf-8') as f:
    f.write(html)


# Updates for Mandos Intermedios
with open('rrhh-mandos-intermedios.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update background image
html = re.sub(
    r"url\('\./src/img/hero_finanzas_mandos_intermedios\.jpg'\)", 
    r"url('./src/img/hero_rrhh_mandos_intermedios.jpg')", 
    html
)

# Update Title
old_title_mandos = """      <h1 class="hero-title mix">
        <span class="t-bold">Dominas la operativa diaria.</span>
        <span class="t-serif">Ahora domina la estrategia.</span>
        <span class="t-light">Da el salto de la ejecución financiera al control estratégico y la toma de decisiones.</span>
      </h1>"""
new_title_mandos = """      <h1 class="hero-title mix">
        <span class="t-bold">Ver personas es fácil.</span>
        <span class="t-serif">Entenderlas es otra cosa.</span>
        <span class="t-light">Da el salto a la toma de decisiones estratégicas apoyada en datos y tecnología.</span>
      </h1>"""
html = html.replace(old_title_mandos, new_title_mandos)

# Graphic replacement for Mandos Intermedios
# We replace the entire network-effect div with a new stat card graphic
old_visual_start = html.find('<div class="d-hero-visual reveal delay-1">')
old_visual_end = html.find('</div>\n    </div>\n  </div>\n</header>', old_visual_start)
if old_visual_start != -1 and old_visual_end != -1:
    new_visual = """<div class="d-hero-visual reveal delay-1">
      <div class="d-hero-img-wrap" style="padding-top:2rem; display: flex; flex-direction: column; gap: 1.5rem; justify-content: center; align-items: center; height: 100%;">
        
        <div style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); padding: 2rem; border-radius: 16px; width: 100%; max-width: 400px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
          <div style="font-size: 3rem; font-weight: 800; color: #ffd7a0; line-height: 1; margin-bottom: 0.5rem;">+30<span style="font-size: 1.5rem;">%</span></div>
          <div style="color: #fff; font-size: 1.1rem; font-weight: 500;">Productividad con tecnología en RRHH</div>
          
          <div style="width: 100%; height: 4px; background: rgba(255,255,255,0.2); margin: 1.5rem 0; border-radius: 2px; overflow: hidden;">
             <div style="width: 30%; height: 100%; background: #ffd7a0;"></div>
          </div>
          
          <div style="font-size: 3rem; font-weight: 800; color: #fff; line-height: 1; margin-bottom: 0.5rem;">95<span style="font-size: 1.5rem;">%</span></div>
          <div style="color: rgba(255,255,255,0.8); font-size: 1.1rem; font-weight: 500;">de empleabilidad</div>
        </div>

      """
    html = html[:old_visual_start] + new_visual + html[old_visual_end:]

# Update Master Name
html = html.replace("Finanzas, Fintech y<br>Control Estratégico", "Dirección de<br>Recursos Humanos")
html = html.replace("Finanzas, Fintech y Control Estratégico", "Dirección de Recursos Humanos")

# Write Mandos Intermedios
with open('rrhh-mandos-intermedios.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updates applied to both files.")

