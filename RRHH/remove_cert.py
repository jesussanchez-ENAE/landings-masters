import re

files = ['rrhh-ceos.html', 'rrhh-mandos-intermedios.html']

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex to remove the CCA certificate section
    content = re.sub(
        r'<!-- CERTIFICADO CCA -->\s*<section class="enae-wm enae-wm--cert" id="certificado".*?</section>', 
        '', 
        content, 
        flags=re.DOTALL
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
print("CCA Certificate section removed.")
