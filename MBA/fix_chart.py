import re

with open('src/js/main.js', 'r') as f:
    content = f.read()

# Find the radar chart logic
chart_logic = re.search(r'/\* RADAR CHART LOGIC \*/\s*\(function\(\) \{(.*?)\}\)\(\);', content, re.DOTALL)

if chart_logic:
    inner_code = chart_logic.group(1)
    new_code = f"/* RADAR CHART LOGIC */\ndocument.addEventListener('DOMContentLoaded', function() {{{inner_code}}});"
    content = content.replace(chart_logic.group(0), new_code)
    
    with open('src/js/main.js', 'w') as f:
        f.write(content)
    print("Fixed Chart.js initialization.")
else:
    print("Chart logic not found.")
