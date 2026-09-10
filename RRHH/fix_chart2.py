import re

with open('src/js/main.js', 'r') as f:
    content = f.read()

# Replace the DOMContentLoaded wrapper
chart_logic = re.search(r"document\.addEventListener\('DOMContentLoaded', function\(\) \{(.*?)\}\);", content, re.DOTALL)

if chart_logic:
    inner_code = chart_logic.group(1)
    new_code = f"(function() {{{inner_code}}})();"
    content = content.replace(chart_logic.group(0), new_code)
    
    with open('src/js/main.js', 'w') as f:
        f.write(content)
    print("Reverted to IIFE.")
else:
    print("Pattern not found.")
