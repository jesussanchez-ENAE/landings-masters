files = ['rrhh-ceos.html', 'rrhh-mandos-intermedios.html']
for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace("<title>Máster en Finanzas, Fintech y Control Estratégico · ENAE</title>", "<title>Máster en Dirección de Recursos Humanos · ENAE</title>")
    content = content.replace('alt="Visión estratégica de negocio"', 'alt="Visión estratégica de RRHH"')
    content = content.replace('alt="Decisiones de empresa"', 'alt="Decisiones de talento"')
    content = content.replace('alt="Liderazgo ejecutivo"', 'alt="Liderazgo en RRHH"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
print("Titles and alts fixed.")
