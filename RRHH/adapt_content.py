import re

files = ['rrhh-ceos.html', 'rrhh-mandos-intermedios.html']

replacements = {
    "Criterio financiero": "Criterio en RRHH",
    "Interpreta la situación financiera de tu empresa con rigor y precisión para la toma de decisiones.": "Interpreta los datos de talento de tu empresa con rigor y precisión para la toma de decisiones.",
    "Comprende cómo las finanzas y las nuevas tecnologías (fintech) pueden potenciar el negocio y viceversa, desde una perspectiva práctica.": "Comprende cómo la gestión de personas y las nuevas tecnologías (IA) pueden potenciar el negocio y viceversa, desde una perspectiva práctica.",
    "Comprende cómo las finanzas y las nuevas tecnologías (fintech) pueden potenciar el negocio y viceversa.": "Comprende cómo la gestión de personas y las nuevas tecnologías (IA) pueden potenciar el negocio y viceversa.",
    "Dominio financiero": "Dominio de RRHH",
    "Las finanzas y el control de gestión explicados por quienes los aplican a diario, no desde la teoría, sino desde la práctica real en empresas.": "Los Recursos Humanos explicados por quienes los aplican a diario, no desde la teoría, sino desde la práctica real en empresas.",
    "identificar riesgos y plantear soluciones financieras con rigor": "identificar riesgos y plantear soluciones de talento con rigor",
    "identificar riesgos y plantear soluciones financieras con fundamento": "identificar riesgos y plantear soluciones de talento con fundamento",
    "las finanzas dejan de ser un asunto exclusivamente del departamento financiero.": "los recursos humanos dejan de ser un asunto exclusivamente del departamento de RRHH.",
    "formando directivos financieros": "formando directivos de RRHH",
    "impacto financiero en el negocio": "impacto del talento en el negocio",
    "Las finanzas no solo se analizan,": "El talento no solo se gestiona,",
    "conectar la gestión financiera con la estrategia": "conectar la gestión de personas con la estrategia",
    "directivos financieros de élite": "directivos de RRHH de élite",
    "conocen las finanzas desde dentro": "conocen los recursos humanos desde dentro",
    "referentes del ámbito financiero": "referentes del ámbito de RRHH",
    "expertos en fintech y controllers estratégicos": "expertos en People Analytics y gestión de talento",
    "Las finanzas se aprenden mejor": "La gestión de talento se aprende mejor",
    "problemáticas financieras": "problemáticas de RRHH",
    "problemáticas financieras y estratégicas": "problemáticas de gestión y estratégicas",
    "criterio financiero aplicable": "criterio aplicable",
    "competencias financieras": "competencias en dirección de personas",
    "Una visión completa de las finanzas": "Una visión completa de los Recursos Humanos",
    "criterio financiero también debe hacerlo": "criterio en gestión de talento también debe hacerlo",
    "visión financiera más sólida": "visión directiva más sólida",
    "dirección financiera a diario": "dirección de talento a diario"
}

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Content adapted.")
