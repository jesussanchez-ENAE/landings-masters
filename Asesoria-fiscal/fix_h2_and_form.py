import re

file_path = 'asesoria-fiscal-colegio-abogados.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove line-height: 1.1; from h2
content = re.sub(r'(<h2[^>]*style="[^"]*)line-height:\s*1\.1;?\s*([^"]*">)', r'\1\2', content)

# 2. Change align-items: center; to align-items: start; in the final-container
content = content.replace('align-items: center; gap: 4rem;', 'align-items: start; gap: 4rem;')

# Let's also check if the inline style ends up with empty style attributes and clean them if necessary, 
# but it's not strictly needed.

# 3. Just to be absolutely safe about the h2 mix gaps, I will remove ANY <br> tags inside h2.mix
def remove_br_in_h2(match):
    return match.group(0).replace('<br>', '').replace('<br/>', '').replace('<br />', '')

content = re.sub(r'<h2 class="mix.*?</h2\s*>', remove_br_in_h2, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed h2 and form alignment")
