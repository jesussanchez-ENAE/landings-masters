import re

with open('src/js/main.js', 'r') as f:
    content = f.read()

# Replace angleLines color
content = content.replace("color: 'rgba(0, 0, 0, 0.08)'", "color: 'rgba(255, 255, 255, 0.15)'")

# Replace pointLabels color
content = content.replace("color: '#334155'", "color: 'rgba(255, 255, 255, 0.85)'")

# Replace legend color
content = content.replace("color: '#0f172a'", "color: '#ffffff'")

# Also, the 'Sin Executive MBA' line might be hard to see if it's slate on dark background.
# Let's change its color from Slate to white-ish
content = content.replace("backgroundColor: 'rgba(100, 116, 139, 0.1)'", "backgroundColor: 'rgba(255, 255, 255, 0.05)'")
content = content.replace("borderColor: 'rgba(100, 116, 139, 0.5)'", "borderColor: 'rgba(255, 255, 255, 0.4)'")
content = content.replace("pointBackgroundColor: 'rgba(100, 116, 139, 1)'", "pointBackgroundColor: 'rgba(255, 255, 255, 0.8)'")
content = content.replace("pointHoverBorderColor: 'rgba(100, 116, 139, 1)'", "pointHoverBorderColor: 'rgba(255, 255, 255, 1)'")

with open('src/js/main.js', 'w') as f:
    f.write(content)

print("Updated JS colors.")
