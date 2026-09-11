import re

with open('rrhh-mandos-intermedios.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the graphic block we inserted earlier with a Chart.js implementation
old_visual_start = html.find('<div class="d-hero-visual reveal delay-1">')
old_visual_end = html.find('</div>\n    </div>\n  </div>\n</header>', old_visual_start)

new_visual = """<div class="d-hero-visual reveal delay-1" style="display: flex; align-items: center; justify-content: center; height: 100%;">
      <div style="background: rgba(25, 25, 25, 0.7); border: 1px solid rgba(255,255,255,0.15); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); padding: 2.5rem; border-radius: 20px; width: 100%; max-width: 480px; box-shadow: 0 20px 40px rgba(0,0,0,0.4);">
        <h3 style="color: #fff; font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 1.5rem; text-align: center; font-weight: 500;">Impacto de la Tecnología en RRHH</h3>
        
        <div style="position: relative; height: 180px; margin-bottom: 2rem;">
          <canvas id="rrhhChart"></canvas>
        </div>
        
        <div style="display: flex; justify-content: space-between; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 1.5rem;">
          <div style="text-align: center; width: 45%;">
            <div style="font-size: 2.5rem; font-weight: 800; color: #ffd7a0; line-height: 1; margin-bottom: 0.5rem;">+30<span style="font-size: 1.2rem;">%</span></div>
            <div style="color: rgba(255,255,255,0.8); font-size: 0.9rem; line-height: 1.3;">Productividad con tecnología</div>
          </div>
          <div style="width: 1px; background: rgba(255,255,255,0.1);"></div>
          <div style="text-align: center; width: 45%;">
            <div style="font-size: 2.5rem; font-weight: 800; color: #fff; line-height: 1; margin-bottom: 0.5rem;">95<span style="font-size: 1.2rem;">%</span></div>
            <div style="color: rgba(255,255,255,0.8); font-size: 0.9rem; line-height: 1.3;">Empleabilidad de perfiles formados</div>
          </div>
        </div>
      </div>
      
      <script>
        document.addEventListener('DOMContentLoaded', function() {
          const ctx = document.getElementById('rrhhChart');
          if(ctx) {
            new Chart(ctx, {
              type: 'bar',
              data: {
                labels: ['Gestión Tradicional', 'Gestión con Tecnología'],
                datasets: [{
                  label: 'Nivel de Productividad',
                  data: [100, 130],
                  backgroundColor: [
                    'rgba(255, 255, 255, 0.2)',
                    '#ffd7a0'
                  ],
                  borderRadius: 6,
                  borderWidth: 0
                }]
              },
              options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                  legend: { display: false },
                  tooltip: {
                    backgroundColor: 'rgba(0,0,0,0.8)',
                    titleColor: '#fff',
                    bodyColor: '#fff',
                    padding: 10,
                    displayColors: false,
                    callbacks: {
                      label: function(context) {
                        return context.raw + ' (Base 100)';
                      }
                    }
                  }
                },
                scales: {
                  y: {
                    beginAtZero: true,
                    max: 150,
                    grid: { color: 'rgba(255,255,255,0.05)', drawBorder: false },
                    ticks: { color: 'rgba(255,255,255,0.5)', stepSize: 50, font: { size: 10 } }
                  },
                  x: {
                    grid: { display: false, drawBorder: false },
                    ticks: { color: 'rgba(255,255,255,0.8)', font: { size: 11 } }
                  }
                },
                animation: {
                  duration: 2000,
                  easing: 'easeOutQuart'
                }
              }
            });
          }
        });
      </script>
"""
html = html[:old_visual_start] + new_visual + html[old_visual_end:]

with open('rrhh-mandos-intermedios.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated graphic in rrhh-mandos-intermedios.html")
