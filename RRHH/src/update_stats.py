import re

files = ['rrhh-ceos.html', 'rrhh-directivos.html']

old_block = """    <div>
      <div class="kpi-num-lg">+30<span class="u">años</span></div>
      <div class="kpi-label">de experiencia</div>
      <span class="kpi-sub">formando directivos de RRHH</span>
    </div>"""

new_block = """    <div>
      <div class="kpi-num-lg">+5.000<span class="u"></span></div>
      <div class="kpi-label">alumni</div>
      <span class="kpi-sub">en la red de directivos internacionales</span>
    </div>"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_block in content:
        content = content.replace(old_block, new_block)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

