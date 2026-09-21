import os
import glob

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<!DOCTYPE html>' in content or '<html' in content:
        continue
    
    # Find split point
    split_str = '<!-- ENAE Logo inline SVG'
    idx = content.find(split_str)
    
    if idx == -1:
        # fallback to looking for the first svg
        split_str = '<svg xmlns='
        idx = content.find(split_str)
    
    if idx == -1:
        # fallback to nav
        split_str = '<nav class="nav">'
        idx = content.find(split_str)
        
    if idx != -1:
        head_content = content[:idx]
        body_content = content[idx:]
        
        fixed_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
{head_content.strip()}
</head>
<body>
{body_content.strip()}
</body>
</html>
"""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        print(f"Fixed {filepath}")
    else:
        print(f"Could not find split point in {filepath}")

