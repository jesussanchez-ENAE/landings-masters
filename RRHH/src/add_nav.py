import re

with open('rrhh-direccion-humana.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Top Nav
content = content.replace(
    '<a href="#programa">Programa</a>',
    '<a href="#programa">Programa</a>\n      <a href="#fundae">FUNDAE</a>'
)

# Footer Nav
content = content.replace(
    '<li><a href="#programa">Plan de estudios</a></li>',
    '<li><a href="#programa">Plan de estudios</a></li>\n          <li><a href="#fundae">Bonificación FUNDAE</a></li>'
)

with open('rrhh-direccion-humana.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Menu updated.")

