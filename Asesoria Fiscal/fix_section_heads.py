import re

def fix_section_heads(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define new class CSS
    new_css = """
  .d-section-head {
    text-align: center;
    margin-bottom: 3.5rem;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
  }
  .d-section-head .mix {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.25rem;
  }
  .d-section-head .mix .t-bold {
    font-size: 2.5rem; /* Larger */
    line-height: 1.1;
  }
  .d-section-head .mix .t-serif {
    font-size: 3.5rem; /* Even larger and red */
    color: var(--enae-rojo);
    font-style: italic;
    font-weight: 400;
  }
  @media (max-width: 768px) {
    .d-section-head .mix .t-bold { font-size: 2rem; }
    .d-section-head .mix .t-serif { font-size: 2.5rem; }
  }
"""
    # Insert new CSS before closing custom style tag
    if ".d-section-head" not in content:
        content = content.replace("/* --- UX/UI PRO MAX FIXES --- */", new_css + "\n  /* --- UX/UI PRO MAX FIXES --- */")

    # Replace classes in the HTML body
    # "Lo que cambia"
    content = content.replace('class="section-head reveal" style="text-align:center;"', 'class="d-section-head reveal"')
    # "Un MBA pensado"
    content = content.replace('class="section-head reveal"\n', 'class="d-section-head reveal"\n')
    # "Todo lo que necesitas"
    # Note: there might be variations. Let's just use regex to replace class="section-head..." in our specific sections.
    # But wait, original template might have section-head that we don't want to break.
    # We only care about the directivos content. I can just regex replace all `section-head` between the nav and footer?
    # Yes, or just explicitly replace them.
    
    # Let's replace any `section-head reveal` or `section-head d-section-head` etc.
    content = content.replace('class="section-head reveal"', 'class="d-section-head reveal"')
    
    # Also clean up the inline styles on those headers to let the CSS do the work
    # 1. Lo que cambia
    content = re.sub(
        r'<h2 class="mix">\s*<span class="t-bold" style="display:block;">Lo que cambia</span>\s*<span class="t-serif">cuando<br>empiezas<br>a pensar<br>como director</span>\s*</h2>',
        r'<h2 class="mix">\n        <span class="t-bold">Lo que cambia</span>\n        <span class="t-serif">cuando empiezas a pensar como director</span>\n      </h2>',
        content,
        flags=re.IGNORECASE | re.MULTILINE
    )
    
    # 2. Un MBA pensado
    content = re.sub(
        r'<h2 class="mix">\s*<span class="t-bold" style="display:block;">Un MBA<br>pensado<br>para</span>\s*<span class="t-serif" style="display:block;">quienes<br>ya están<br>dirigiendo</span>\s*</h2>',
        r'<h2 class="mix">\n        <span class="t-bold">Un MBA pensado para</span>\n        <span class="t-serif">quienes ya están dirigiendo</span>\n      </h2>',
        content,
        flags=re.IGNORECASE | re.MULTILINE
    )
    
    # 3. Todo lo que necesitas
    content = re.sub(
        r'<h2 class="mix">\s*<span class="t-bold" style="display:block;">Todo lo que necesitas</span>\s*<span class="t-serif">para dirigir mejor</span>\s*</h2>',
        r'<h2 class="mix">\n        <span class="t-bold">Todo lo que necesitas</span>\n        <span class="t-serif">para dirigir mejor</span>\n      </h2>',
        content,
        flags=re.IGNORECASE | re.MULTILINE
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Section head layout fixed!")

if __name__ == '__main__':
    fix_section_heads('enae-executive-mba-directivos.html')
