import re

files = ['rrhh-ceos.html', 'rrhh-mandos-intermedios.html']

old_url = "https://www.youtube.com/embed/coLwWC-6-jA?list=PLhkVTNrK6QC3n9oPmkOu7rELueV2cL7f_"
new_url = "https://www.youtube.com/embed/XmLgWgCDmt8?list=PLhkVTNrK6QC0FGUsrQmNmhQdL1t04fjic"

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_url in content:
        content = content.replace(old_url, new_url)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated YouTube link in {filepath}")
    else:
        print(f"URL not found in {filepath}!")

