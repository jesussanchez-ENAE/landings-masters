with open('rrhh-ceos.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("<span>CONTROL</span>", "<span>TALENTO</span>")
content = content.replace("<span>NEGOCIO</span>", "<span>LIDERAZGO</span>")
content = content.replace("<span>FINTECH</span>", "<span>ANALYTICS</span>")
content = content.replace("<span>DATOS</span>", "<span>CULTURA</span>")
content = content.replace("<span>RIESGO</span>", "<span>RETENCIÓN</span>")

with open('rrhh-ceos.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated nodes in rrhh-ceos.html")
