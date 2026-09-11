import re

files = ['rrhh-ceos.html', 'rrhh-directivos.html']

anime_logic = """
  // Anime.js entry and exit animations
  document.addEventListener('DOMContentLoaded', () => {
    const elements = document.querySelectorAll('.reveal');
    
    // Override CSS transition so anime.js handles it smoothly
    elements.forEach(el => {
      el.style.transition = 'none';
      el.style.opacity = '0'; // Initial state
    });

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        // Determine delay based on classes
        let delayVal = 0;
        if (entry.target.classList.contains('delay-1')) delayVal = 200;
        if (entry.target.classList.contains('delay-2')) delayVal = 400;
        if (entry.target.classList.contains('delay-3')) delayVal = 600;

        if (entry.isIntersecting) {
          // Entry animation
          anime.remove(entry.target);
          anime({
            targets: entry.target,
            opacity: [0, 1],
            translateY: [40, 0],
            duration: 800,
            delay: delayVal,
            easing: 'easeOutQuart'
          });
        } else {
          // Exit animation (reset state for when they come back in)
          anime.remove(entry.target);
          anime({
            targets: entry.target,
            opacity: 0,
            translateY: 40,
            duration: 500,
            easing: 'easeInQuart'
          });
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    });

    elements.forEach(el => observer.observe(el));
  });
</script>"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'anime.remove(entry.target)' not in content:
        # replace the last </script> with anime_logic
        content = content.replace('});\n</script>', '});\n' + anime_logic)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed animations in {filepath}")

