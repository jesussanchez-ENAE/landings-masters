import re

files = ['rrhh-ceos.html', 'rrhh-mandos-intermedios.html']

replacements = {
    "directivos financieros": "directivos de RRHH",
    "dirección financiera": "dirección de recursos humanos",
    "implicaciones financieras": "implicaciones de talento",
    "soluciones financieras": "soluciones de recursos humanos",
    "impacto financiero": "impacto en el talento",
    "líderes financieros": "líderes en RRHH",
    "criterio financiero": "criterio en RRHH",
    "planificación financiera": "planificación estratégica de RRHH",
    "ejecución financiera": "ejecución de recursos humanos",
    "control financiero": "control de RRHH"
}

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Second pass content adapted.")
