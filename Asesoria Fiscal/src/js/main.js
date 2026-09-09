  (function() {
    document.documentElement.classList.add('js-ready');

    var revealElements = document.querySelectorAll('.reveal');
    var revealObserver = new IntersectionObserver(function(entries, observer) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          observer.unobserve(entry.target);
        }
      })();
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
    revealElements.forEach(function(el) { revealObserver.observe(el); });

    var floatWrap = document.querySelector('.float-wrap');
    if (floatWrap) {
      floatWrap.style.opacity = '0';
      floatWrap.style.transition = 'opacity 0.4s ease';
      floatWrap.style.pointerEvents = 'none';
      
      var heroEl = document.querySelector('.hero');
      var finalEl = document.querySelector('.final');
      
      var state = { heroVisible: true, finalVisible: false };
      
      function updateFloatVisibility() {
        if (state.heroVisible || state.finalVisible) {
          floatWrap.style.opacity = '0';
          floatWrap.style.pointerEvents = 'none';
        } else {
          floatWrap.style.opacity = '1';
          floatWrap.style.pointerEvents = 'auto';
        }
      }

      var observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
          if (entry.target === heroEl) state.heroVisible = entry.isIntersecting;
          if (entry.target === finalEl) state.finalVisible = entry.isIntersecting;
        });
        updateFloatVisibility();
      }, { threshold: 0.05 });
      
      if (heroEl) observer.observe(heroEl);
      if (finalEl) observer.observe(finalEl);
    }


  });

  document.addEventListener('DOMContentLoaded', function() {
    var videoIds = [
      '2T0A5SGVtA4', '8AcfkIh5YVY', 'BUYyotdKEvs', 'CkE-EuoyteQ',
      'DwtJ9eh56v4', 'HamrB9F-2kE', 'HfUJcGfEnI0', 'HgihrYXC1OQ',
      'HpggmVElsMI', 'HsV1E92ANq4', 'IYVfbEHHZG8', 'J6FLEsZ3inI',
      'N5yi6EHH1ks', 'SUSoz6o5v2s', 'Ts9V-OJMqQ4', 'Vuh5Xx2SqfQ',
      'YRgrMlRWhFU', 'YertN_4BlTg', '_G6AtJ4CQSE', '_b-068CGg1c',
      'ayzCkb97d2c', 'd3X8gVQwFmo', 'eLL0270JSB0', 'fowTYTg0XXo',
      'gwWqMYW5-T4', 'iJUqiLE8yb4', 'jH3QBeILZBs', 'n48UXasy1UA',
      'nnpK0_PyZWE', 'p7buS5mXaEY', 'pc8z18H18es', 'rwmB94RiaHo',
      'xyIfglpd4Eg', 'ysVbmLYDJW4'
    ];
    var randomId = videoIds[Math.floor(Math.random() * videoIds.length)];
    var iframe = document.getElementById('random-testimonial-video');
    if (iframe) {
      iframe.src = 'https://www.youtube.com/embed/' + randomId + '?rel=0&modestbranding=1';
    }
  });

(function() {
  var canvas = document.getElementById('cobe-globe');
  if (!canvas) return;

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    canvas.style.opacity = '0.6';
    return;
  }

  var ctx = canvas.getContext('2d');
  var NODE_COUNT = 120;
  var CONNECT_DIST = 0.55;
  var PULSE_COUNT = 12;
  var rotY = 0, rotX = 0.3;
  var autoSpeed = 0.002;
  var pointerDown = null;
  var dragOffset = { x: 0, y: 0 };
  var baseRotY = 0, baseRotX = 0.3;
  var paused = false;
  var sphereVisible = true;
  var nodes = [];
  var edges = [];
  var pulses = [];

  var golden = (1 + Math.sqrt(5)) / 2;
  for (var i = 0; i < NODE_COUNT; i++) {
    var theta = Math.acos(1 - 2 * (i + 0.5) / NODE_COUNT);
    var phi = 2 * Math.PI * i / golden;
    nodes.push({
      x: Math.sin(theta) * Math.cos(phi),
      y: Math.sin(theta) * Math.sin(phi),
      z: Math.cos(theta),
      size: 1.5 + Math.random() * 2
    });
  }

  for (var i = 0; i < NODE_COUNT; i++) {
    for (var j = i + 1; j < NODE_COUNT; j++) {
      var dx = nodes[i].x - nodes[j].x;
      var dy = nodes[i].y - nodes[j].y;
      var dz = nodes[i].z - nodes[j].z;
      var d = Math.sqrt(dx*dx + dy*dy + dz*dz);
      if (d < CONNECT_DIST) edges.push({ a: i, b: j, dist: d });
    }
  }

  function spawnPulse() {
    var e = edges[Math.floor(Math.random() * edges.length)];
    return { edge: e, t: 0, speed: 0.008 + Math.random() * 0.012, forward: Math.random() > 0.5 };
  }
  for (var i = 0; i < PULSE_COUNT; i++) {
    var p = spawnPulse(); p.t = Math.random(); pulses.push(p);
  }

  function rotatePoint(px, py, pz) {
    var cosY = Math.cos(rotY), sinY = Math.sin(rotY);
    var x1 = px * cosY - pz * sinY;
    var z1 = px * sinY + pz * cosY;
    var cosX = Math.cos(rotX), sinX = Math.sin(rotX);
    var y1 = py * cosX - z1 * sinX;
    var z2 = py * sinX + z1 * cosX;
    return { x: x1, y: y1, z: z2 };
  }

  function resize() {
    var w = canvas.offsetWidth;
    if (w === 0) return false;
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = w * dpr;
    canvas.height = w * dpr;
    canvas.style.width = w + 'px';
    canvas.style.height = w + 'px';
    return true;
  }

  function draw() {
    if (!sphereVisible) { requestAnimationFrame(draw); return; }
    if (!paused) rotY += autoSpeed;

    var w = canvas.width, h = canvas.height;
    var cx = w / 2, cy = h / 2;
    var radius = w * 0.38;

    ctx.clearRect(0, 0, w, h);

    var veilGrad = ctx.createRadialGradient(cx, cy, 0, cx, cy, radius * 1.05);
    veilGrad.addColorStop(0, 'rgba(0,0,0,0.35)');
    veilGrad.addColorStop(0.75, 'rgba(0,0,0,0.2)');
    veilGrad.addColorStop(1, 'rgba(0,0,0,0)');
    ctx.beginPath();
    ctx.arc(cx, cy, radius * 1.05, 0, Math.PI * 2);
    ctx.fillStyle = veilGrad;
    ctx.fill();

    var projected = [];
    for (var i = 0; i < nodes.length; i++) {
      var n = nodes[i];
      var r = rotatePoint(n.x, n.y, n.z);
      var depth = (r.z + 1) / 2;
      projected.push({ x: cx + r.x * radius, y: cy + r.y * radius, z: r.z, depth: depth, size: n.size });
    }

    for (var pass = 0; pass < 2; pass++) {
      for (var i = 0; i < edges.length; i++) {
        var e = edges[i];
        var a = projected[e.a], b = projected[e.b];
        var avgZ = (a.z + b.z) / 2;
        if (pass === 0 && avgZ > -0.05) continue;
        if (pass === 1 && avgZ <= -0.05) continue;
        var alpha = Math.max(0, Math.min(1, (avgZ + 1) / 2));
        alpha = alpha * alpha * 0.6;
        ctx.beginPath();
        ctx.moveTo(a.x, a.y);
        ctx.lineTo(b.x, b.y);
        ctx.strokeStyle = 'rgba(255,255,255,' + Math.min(1, alpha * 3).toFixed(3) + ')';
        ctx.lineWidth = 1.2;
        ctx.stroke();
      }
    }

    for (var i = 0; i < pulses.length; i++) {
      var p = pulses[i], e = p.edge;
      var a = projected[e.a], b = projected[e.b];
      var t = p.forward ? p.t : 1 - p.t;
      var px = a.x + (b.x - a.x) * t;
      var py = a.y + (b.y - a.y) * t;
      var pz = a.z + (b.z - a.z) * t;
      var depth = (pz + 1) / 2;
      if (depth > 0.3) {
        var glow = ctx.createRadialGradient(px, py, 0, px, py, 8 * (w/800));
        glow.addColorStop(0, 'rgba(255,255,255,' + Math.min(1, depth * 1.2).toFixed(2) + ')');
        glow.addColorStop(1, 'rgba(255,255,255,0)');
        ctx.beginPath();
        ctx.arc(px, py, 8 * (w/800), 0, Math.PI * 2);
        ctx.fillStyle = glow;
        ctx.fill();
      }
      p.t += p.speed;
      if (p.t >= 1) pulses[i] = spawnPulse();
    }

    var sorted = projected.slice().sort(function(a, b) { return a.z - b.z; });
    for (var i = 0; i < sorted.length; i++) {
      var n = sorted[i];
      var alpha = Math.max(0.15, n.depth * 1.2);
      var r = n.size * (0.7 + n.depth * 1) * (w / 800);
      if (n.depth > 0.35) {
        var glow = ctx.createRadialGradient(n.x, n.y, 0, n.x, n.y, r * 5);
        glow.addColorStop(0, 'rgba(255,255,255,' + (alpha * 0.6).toFixed(3) + ')');
        glow.addColorStop(1, 'rgba(255,255,255,0)');
        ctx.beginPath();
        ctx.arc(n.x, n.y, r * 5, 0, Math.PI * 2);
        ctx.fillStyle = glow;
        ctx.fill();
      }
      ctx.beginPath();
      ctx.arc(n.x, n.y, r, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(255,255,255,' + Math.min(1, alpha * 1.3).toFixed(3) + ')';
      ctx.fill();
    }

    requestAnimationFrame(draw);
  }

  canvas.addEventListener('pointerdown', function(e) {
    pointerDown = { x: e.clientX, y: e.clientY };
    canvas.style.cursor = 'grabbing';
    paused = true;
  });
  window.addEventListener('pointermove', function(e) {
    if (pointerDown) {
      dragOffset.x = (e.clientX - pointerDown.x) / 200;
      dragOffset.y = (e.clientY - pointerDown.y) / 200;
      rotY = baseRotY + dragOffset.x;
      rotX = baseRotX - dragOffset.y;
    }
  }, { passive: true });
  window.addEventListener('pointerup', function() {
    if (pointerDown) { baseRotY = rotY; baseRotX = rotX; dragOffset = { x: 0, y: 0 }; }
    pointerDown = null;
    canvas.style.cursor = 'grab';
    paused = false;
  }, { passive: true });

  new IntersectionObserver(function(entries) {
    sphereVisible = entries[0].isIntersecting;
  }, { threshold: 0 }).observe(canvas);

  window.addEventListener('resize', resize);

  function start() {
    if (!resize()) return false;
    canvas.style.opacity = '1';
    draw();
    return true;
  }

  if (!start()) {
    var ro = new ResizeObserver(function(entries) {
      if (entries[0] && entries[0].contentRect.width > 0) {
        ro.disconnect();
        start();
      }
    });
    ro.observe(canvas);
  }
})();

// Metodología que transforma — Carousel controller (Embla-inspired with drag & snap)
(function() {
  var viewport = document.getElementById('method-carousel');
  var prevBtn = document.getElementById('method-prev');
  var nextBtn = document.getElementById('method-next');
  if (!viewport || !prevBtn || !nextBtn) return;

  function getStep() {
    var firstCard = viewport.querySelector('.method-service-card');
    return firstCard ? firstCard.offsetWidth + 24 : 340;
  }

  function updateControls() {
    var sl = viewport.scrollLeft;
    var max = viewport.scrollWidth - viewport.clientWidth;
    prevBtn.disabled = sl <= 6;
    nextBtn.disabled = sl >= max - 6;
  }

  prevBtn.addEventListener('click', function() {
    viewport.scrollBy({ left: -getStep(), behavior: 'smooth' });
  });

  nextBtn.addEventListener('click', function() {
    viewport.scrollBy({ left: getStep(), behavior: 'smooth' });
  });

  viewport.addEventListener('scroll', updateControls, { passive: true });
  window.addEventListener('resize', updateControls);

  // Keyboard navigation
  viewport.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowLeft') {
      e.preventDefault();
      viewport.scrollBy({ left: -getStep(), behavior: 'smooth' });
    } else if (e.key === 'ArrowRight') {
      e.preventDefault();
      viewport.scrollBy({ left: getStep(), behavior: 'smooth' });
    }
  });

  // Drag to scroll functionality
  var isDown = false;
  var startX = 0;
  var scrollLeftStart = 0;
  var isDragging = false;

  viewport.addEventListener('mousedown', function(e) {
    if (e.button !== 0) return; // Only left click
    isDown = true;
    isDragging = false;
    startX = e.pageX - viewport.offsetLeft;
    scrollLeftStart = viewport.scrollLeft;
    viewport.style.scrollBehavior = 'auto'; // instantaneous tracking
    viewport.style.scrollSnapType = 'none'; // free-flow drag without snap stutter
  });

  window.addEventListener('mousemove', function(e) {
    if (!isDown) return;
    var x = e.pageX - viewport.offsetLeft;
    var walk = (x - startX);
    if (Math.abs(walk) > 4) {
      isDragging = true;
      viewport.style.cursor = 'grabbing';
      document.body.style.userSelect = 'none';
    }
    if (isDragging) {
      viewport.scrollLeft = scrollLeftStart - walk;
    }
  });

  window.addEventListener('mouseup', function() {
    if (!isDown) return;
    isDown = false;
    viewport.style.cursor = 'grab';
    viewport.style.scrollBehavior = 'smooth';
    viewport.style.scrollSnapType = 'x mandatory'; // re-enable snap
    document.body.style.removeProperty('user-select');
    updateControls();
    setTimeout(function() {
      isDragging = false;
    }, 50);
  });

  // Initial check after DOM ready
  setTimeout(updateControls, 100);
})();

/* RADAR CHART LOGIC */
document.addEventListener('DOMContentLoaded', function() {
  var canvas = document.getElementById('mba-radar-chart');
  if (!canvas) return;
  canvas.style.opacity = '1';

  var ctx = canvas.getContext('2d');
  
  // Custom plugin to add a glow effect to the chart lines
  const glowPlugin = {
    id: 'glowPlugin',
    beforeDatasetsDraw: function(chart) {
      const ctx = chart.ctx;
      ctx.save();
      ctx.shadowColor = 'rgba(169, 24, 50, 0.4)';
      ctx.shadowBlur = 15;
      ctx.shadowOffsetX = 0;
      ctx.shadowOffsetY = 0;
    },
    afterDatasetsDraw: function(chart) {
      chart.ctx.restore();
    }
  };

  new Chart(ctx, {
    type: 'radar',
    data: {
      labels: [
        'Visión Estratégica', 
        'Liderazgo', 
        'Innovación', 
        'Finanzas', 
        'Toma Decisiones', 
        'Networking'
      ],
      datasets: [{
        label: 'Con Executive MBA',
        data: [95, 90, 85, 90, 95, 90],
        backgroundColor: 'rgba(169, 24, 50, 0.25)', /* ENAE Granate */
        borderColor: 'rgba(169, 24, 50, 1)',
        pointBackgroundColor: 'rgba(169, 24, 50, 1)',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: 'rgba(169, 24, 50, 1)',
        borderWidth: 3,
        fill: true
      }, {
        label: 'Sin Executive MBA',
        data: [50, 55, 45, 50, 60, 40],
        backgroundColor: 'rgba(255, 255, 255, 0.05)', /* Slate */
        borderColor: 'rgba(255, 255, 255, 0.4)',
        pointBackgroundColor: 'rgba(255, 255, 255, 0.8)',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: 'rgba(255, 255, 255, 1)',
        borderWidth: 2,
        fill: true,
        borderDash: [5, 5]
      }]
    },
    plugins: [glowPlugin],
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        r: {
          angleLines: {
            color: 'rgba(255, 255, 255, 0.15)'
          },
          grid: {
            color: 'rgba(255, 255, 255, 0.15)',
            circular: true
          },
          pointLabels: {
            font: {
              family: "'Inter', sans-serif",
              size: 13,
              weight: '600'
            },
            color: 'rgba(255, 255, 255, 0.85)' /* Slate 700 */
          },
          ticks: {
            display: false, /* Hide the numeric values (0, 20, 40...) */
            min: 0,
            max: 100
          }
        }
      },
      plugins: {
        legend: {
          position: 'bottom',
          labels: {
            font: {
              family: "'Inter', sans-serif",
              size: 14,
              weight: '500'
            },
            color: '#ffffff',
            padding: 20,
            usePointStyle: true,
            pointStyle: 'circle'
          }
        },
        tooltip: {
          backgroundColor: 'rgba(15, 23, 42, 0.9)',
          titleFont: { size: 14, family: "'Inter', sans-serif" },
          bodyFont: { size: 13, family: "'Inter', sans-serif" },
          padding: 12,
          cornerRadius: 8,
          displayColors: true
        }
      },
      animation: {
        duration: 2000,
        easing: 'easeOutQuart'
      }
    }
  });
});
