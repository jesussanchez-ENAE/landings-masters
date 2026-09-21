import re

file_path = 'asesoria-fiscal-colegio-abogados.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove style="margin-top: 20%;" from final-info
content = content.replace('style="margin-top: 20%;"', '')

# 2. Clean inline font-size from h2 elements so they use the global base.css sizes
# This will fix any overlapping or line-height scaling issues caused by custom clamp() sizes.
content = re.sub(r'(<h2[^>]*style="[^"]*)font-size:\s*clamp\([^)]*\);?\s*([^"]*">)', r'\1\2', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Cleaned up inline font-size and margin-top")
