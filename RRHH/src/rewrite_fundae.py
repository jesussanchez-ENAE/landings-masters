import re

with open('rrhh-direccion-humana.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract the block inside the faq-list of the FUNDAE section
start_marker = '<div class="faq-list" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; align-items: start;">'
end_marker = '      </div>\n    </div>\n  </div>\n</section>\n<!-- FAQ -->'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker, start_idx)

if start_idx == -1 or end_idx == -1:
    print("Could not find the bounds for replacing FUNDAE.")
    exit(1)

new_faq_list = """
        <details class="pillar">
          <summary>¿Es posible bonificar este máster con FUNDAE?</summary>
          <div class="a">
            <p>Absolutamente. La mayoría de nuestros programas ejecutivos son bonificables. Las empresas disponen de un crédito anual para formación que, a menudo, queda sin utilizar.</p>
            <p>En ENAE nos encargamos de analizar el saldo disponible de tu organización y te asesoramos para optimizarlo al máximo.</p>
          </div>
        </details>

        <details class="pillar">
          <summary>¿Se pierde el crédito si no se utiliza?</summary>
          <div class="a">
            <p>Así es. Cerca del 80% del tejido empresarial español desaprovecha su saldo formativo anual, generalmente por falta de tiempo o dudas con los trámites.</p>
            <p>Al ser una cantidad ya abonada mediante las cotizaciones a la Seguridad Social, este crédito caduca el 31 de diciembre de cada año. Desde ENAE evitamos que tu empresa pierda esta inversión.</p>
          </div>
        </details>

        <details class="pillar">
          <summary>¿Supone una carga administrativa para la empresa?</summary>
          <div class="a">
            <p>En absoluto. Actuamos como Entidad Organizadora ante FUNDAE, asumiendo de forma integral todos los trámites burocráticos: notificaciones, documentación exigida y cierre de expedientes.</p>
            <p>Tu único objetivo será el desarrollo de tu equipo; nosotros gestionamos el papeleo con total rigor y sin complicaciones.</p>
          </div>
        </details>

        <details class="pillar">
          <summary>¿Qué ocurre si hemos tenido incidencias previas con bonificaciones?</summary>
          <div class="a">
            <p>Es una inquietud comprensible cuando se ha trabajado con modelos estándar o poco rigurosos. Nuestra metodología es diferente.</p>
            <p>Contamos con un equipo experto en cumplimiento normativo y trazabilidad formativa, asegurando que cada gestión se realice bajo los máximos estándares de calidad y seguridad jurídica.</p>
          </div>
        </details>

        <details class="pillar">
          <summary>¿Mi empresa cumple los requisitos para beneficiarse?</summary>
          <div class="a">
            <p>Cualquier organización con centros de trabajo en España, que cotice por Formación Profesional y tenga empleados asalariados en el Régimen General, cuenta por ley con este fondo.</p>
            <p>Da igual el tamaño de tu plantilla o el sector al que pertenezca la empresa.</p>
          </div>
        </details>

        <details class="pillar">
          <summary>¿Cómo funciona el proceso de pago y reembolso?</summary>
          <div class="a">
            <p>El sistema estatal se basa en la bonificación diferida. La empresa abona el coste de la matrícula y, una vez que el profesional finaliza el máster con éxito, el importe bonificado se descuenta automáticamente de los seguros sociales.</p>
            <p>Es una inversión estratégica que retorna de forma directa a la compañía.</p>
          </div>
        </details>

        <details class="pillar">
          <summary>¿Cómo compatibilizamos las clases con el horario laboral?</summary>
          <div class="a">
            <p>Entendemos que el tiempo es el recurso más valioso de un directivo. Nuestros programas están diseñados bajo un formato compatible con la jornada profesional.</p>
            <p>Maximizamos el aprendizaje práctico para que cada hora invertida se traduzca en soluciones aplicables al puesto de trabajo desde el primer día, sin frenar la productividad.</p>
          </div>
        </details>

        <details class="pillar">
          <summary>¿Realmente impacta en el rendimiento de la organización?</summary>
          <div class="a">
            <p>Por supuesto. Un programa en ENAE no es un curso teórico genérico. Aportamos herramientas tangibles, toma de decisiones basada en datos y casos reales de negocio.</p>
            <p>La actualización de competencias (upskilling) es el motor que permite a tu equipo afrontar la transformación digital de la función de Recursos Humanos.</p>
          </div>
        </details>

        <details class="pillar">
          <summary>¿Existe el riesgo de formar al talento y que abandone la empresa?</summary>
          <div class="a">
            <p>La falta de desarrollo profesional es, paradójicamente, la principal causa de fuga de talento. Apostar por la formación de tus equipos fideliza a los profesionales clave.</p>
            <p>Potencia su motivación e incrementa la competitividad de la empresa. El verdadero riesgo para el negocio es tener a un equipo desactualizado.</p>
          </div>
        </details>

        <details class="pillar">
          <summary>¿Se exige cofinanciación para empresas de más de 5 empleados?</summary>
          <div class="a">
            <p>La normativa requiere un porcentaje de cofinanciación, pero no implica necesariamente un desembolso económico adicional para la compañía.</p>
            <p>Este porcentaje se puede cubrir imputando el coste salarial del trabajador durante las horas lectivas que coincidan con su jornada. En ENAE te ayudamos a calcular y justificar esta partida.</p>
          </div>
        </details>

"""

html = html[:start_idx + len(start_marker)] + "\n" + new_faq_list + html[end_idx:]

with open('rrhh-direccion-humana.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("FUNDAE rewritten.")
