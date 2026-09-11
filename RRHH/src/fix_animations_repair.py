import re

files = ['rrhh-ceos.html', 'rrhh-directivos.html']

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The broken part is:
    # <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js">  // Anime.js entry and exit animations
    # ... up to </script>
    
    # We will find the broken script tag and replace it with just the correct script tag.
    broken_start = '<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js">  // Anime.js'
    if broken_start in content:
        start_idx = content.find('<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js">')
        end_idx = content.find('</script>', start_idx) + len('</script>')
        
        # Replace the broken block with the correct chart.js script tag
        content = content[:start_idx] + '<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>' + content[end_idx:]
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Repaired head in {filepath}")

