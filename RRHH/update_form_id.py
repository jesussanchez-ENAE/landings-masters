import re

files = ['rrhh-ceos.html', 'rrhh-mandos-intermedios.html']
old_id = '90ea3a6e-104e-f111-bec7-7ced8d498631'
new_id = '81df57a6-104e-f111-bec7-7ced8d498631'

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_id in content:
        content = content.replace(old_id, new_id)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated form ID in {filepath}")
    else:
        print(f"Old ID not found in {filepath}!")

