import re

files = ['rrhh-ceos.html', 'rrhh-mandos-intermedios.html']

block_to_remove = """          <div class="f-perk">
            <span class="f-perk-icon">✓</span>
            <div>
              <strong>Prácticas Garantizadas</strong>
              <span>Acceso directo a las principales firmas y despachos.</span>
            </div>
          </div>"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if block_to_remove in content:
        content = content.replace(block_to_remove, "")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Removed from {filepath}")
    else:
        print(f"Block not found in {filepath}!")

