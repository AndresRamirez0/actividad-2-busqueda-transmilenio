from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, PageBreak, PageTemplate,
    Paragraph, Spacer, Table, TableStyle)

ROOT = Path(__file__).parent
REPORT = ROOT / "docs" / "Informe_Pruebas_Actividad_2.pdf"
DELIVERY = ROOT / "entrega" / "Entrega_Actividad_2.pdf"
REPO = "https://github.com/AndresRamirez0/actividad-2-busqueda-transmilenio"
VIDEO = "ENLACE PENDIENTE DESPUES DE GRABAR EL VIDEO"

regular = Path(r"C:\Windows\Fonts\aptos.ttf")
bold = Path(r"C:\Windows\Fonts\aptos-bold.ttf")
if regular.exists() and bold.exists():
    pdfmetrics.registerFont(TTFont("Aptos", str(regular)))
    pdfmetrics.registerFont(TTFont("Aptos-Bold", str(bold)))
    REG, BOLD = "Aptos", "Aptos-Bold"
else:
    REG, BOLD = "Helvetica", "Helvetica-Bold"

NAVY = colors.HexColor("#17365D")
BLUE = colors.HexColor("#2F75B5")
PALE = colors.HexColor("#EAF2F8")
GRAY = colors.HexColor("#666666")
W, H = A4
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Institution", fontName=BOLD, fontSize=15, leading=20,
                          alignment=TA_CENTER, textColor=NAVY))
styles.add(ParagraphStyle(name="CoverTitle", fontName=BOLD, fontSize=20, leading=26,
                          alignment=TA_CENTER, spaceAfter=8))
styles.add(ParagraphStyle(name="Cover", fontName=REG, fontSize=12, leading=18,
                          alignment=TA_CENTER))
styles.add(ParagraphStyle(name="H1x", fontName=BOLD, fontSize=15, leading=19,
                          spaceBefore=10, spaceAfter=7, keepWithNext=True))
styles.add(ParagraphStyle(name="H2x", fontName=BOLD, fontSize=12, leading=16,
                          spaceBefore=8, spaceAfter=5, keepWithNext=True))
styles.add(ParagraphStyle(name="Bodyx", fontName=REG, fontSize=10.5, leading=16,
                          alignment=TA_JUSTIFY, spaceAfter=8))
styles.add(ParagraphStyle(name="Smallx", fontName=REG, fontSize=9, leading=13, spaceAfter=4))
styles.add(ParagraphStyle(name="Linkx", fontName=BOLD, fontSize=10.5, leading=16,
                          textColor=BLUE, spaceAfter=8))


def p(text, style="Bodyx"):
    return Paragraph(text, styles[style])


def footer(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        canvas.setStrokeColor(colors.HexColor("#D9E2F3"))
        canvas.line(2.2*cm, H-1.45*cm, W-2.2*cm, H-1.45*cm)
        canvas.setFont(REG, 8)
        canvas.setFillColor(GRAY)
        canvas.drawString(2.2*cm, H-1.15*cm, "Actividad 2 - Búsqueda y sistemas basados en reglas")
        canvas.drawRightString(W-2.2*cm, 1.15*cm, f"Página {doc.page}")
    canvas.restoreState()


def document(path, title):
    path.parent.mkdir(parents=True, exist_ok=True)
    frame = Frame(2.2*cm, 1.7*cm, W-4.4*cm, H-3.5*cm, id="main")
    doc = BaseDocTemplate(str(path), pagesize=A4, title=title,
        author="Nelson Andrés Ramírez Gutiérrez")
    doc.addPageTemplates([PageTemplate(id="page", frames=[frame], onPage=footer)])
    return doc


def cover(subtitle):
    return [Spacer(1, 1.35*cm), p("Corporación Universitaria Iberoamericana", "Institution"),
        p("Programa de Desarrollo de Software", "Cover"), Spacer(1, 1.7*cm),
        p("Actividad 2", "Cover"), p("Búsqueda y sistemas basados en reglas", "CoverTitle"),
        p(subtitle, "Cover"), Spacer(1, 1.7*cm), p("Presentado por", "Cover"),
        p("Nelson Andrés Ramírez Gutiérrez", "Cover"), Spacer(1, 1.1*cm),
        p("Curso: Inteligencia artificial", "Cover"), p("Docente: Sandra Bautista", "Cover"),
        p("Código del curso: 24082026_C1_202634", "Cover"), Spacer(1, 1.3*cm),
        p("Bogotá, Colombia", "Cover"), p("2026", "Cover"), PageBreak()]


def table(rows, widths):
    t = Table([[p(str(c), "Smallx") for c in row] for row in rows], colWidths=widths,
              repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,0), NAVY),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white), ("FONTNAME", (0,0), (-1,0), BOLD),
        ("GRID", (0,0), (-1,-1), .4, colors.HexColor("#CCCCCC")),
        ("VALIGN", (0,0), (-1,-1), "TOP"), ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, PALE]),
        ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5)]))
    return t


report = cover("Sistema inteligente para la búsqueda de rutas en TransMilenio")
report += [p("Introducción", "H1x"), p("Los sistemas basados en reglas representan conocimiento mediante hechos y condiciones que permiten inferir acciones. En este proyecto se combinan dichas reglas con un grafo y el algoritmo A* para recomendar una ruta entre dos estaciones de un modelo simplificado de TransMilenio. El caso facilita observar cómo la representación del conocimiento condiciona una búsqueda y cómo el sistema responde ante cierres o entradas inválidas."),
    p("El modelo tiene fines académicos. Sus costos y posiciones son estimaciones didácticas y no deben utilizarse para planear viajes reales."),
    p("Planteamiento del problema", "H1x"), p("¿Cómo construir en Python un sistema inteligente que utilice reglas lógicas y búsqueda heurística para obtener una ruta válida y de costo mínimo entre dos estaciones?"),
    p("Objetivo general", "H1x"), p("Desarrollar un sistema en Python que represente una red de transporte mediante una base de conocimiento y aplique reglas lógicas y A* para seleccionar una ruta entre un origen y un destino."),
    p("Objetivos específicos", "H2x"), p("1. Modelar estaciones, conexiones y costos como un grafo. 2. Definir reglas para validar consultas y movimientos. 3. Implementar A* y compararlo con Dijkstra. 4. Evaluar rutas normales, cierres y errores de entrada."), PageBreak(),
    p("Marco conceptual", "H1x"), p("La representación del conocimiento organiza los hechos que un programa necesita para razonar. En un sistema basado en reglas, las condiciones se evalúan sobre esos hechos para habilitar o impedir conclusiones y acciones (Benítez, 2014). En este proyecto los hechos son estaciones, troncales, tipos, posiciones y conexiones; las reglas determinan la validez de cada movimiento."),
    p("Una red de transporte puede representarse como un grafo ponderado. Los vértices corresponden a estaciones, las aristas a conexiones y los pesos al costo estimado. La búsqueda A* asigna a cada estado la evaluación f(n) = g(n) + h(n), donde g(n) es el costo acumulado y h(n) estima el costo restante. Si la heurística no sobreestima, A* conserva la optimalidad (Russell & Norvig, 2021)."),
    p("Metodología y arquitectura", "H1x"), table([["Módulo", "Responsabilidad"], ["base_conocimiento.py", "25 estaciones, 26 conexiones, costos y posiciones."], ["reglas.py", "Cinco reglas de validación e inferencia."], ["busqueda.py", "A*, Dijkstra y reconstrucción de rutas."], ["main.py", "Menú y presentación de resultados."], ["test_sistema.py", "Siete pruebas automatizadas."]], [5*cm, 10.5*cm]),
    p("Base de conocimiento y reglas", "H1x"), p("R1: una estación es utilizable si existe y no está cerrada. R2: se puede viajar entre dos estaciones habilitadas si existe una conexión. R3: una estación declarada como transbordo permite cambiar de troncal. R4: una consulta exige estaciones existentes, abiertas y diferentes. R5: una ruta es válida si todos sus movimientos consecutivos cumplen R2."), PageBreak(),
    p("Algoritmos", "H1x"), p("A* mantiene una frontera priorizada por el costo acumulado más la heurística. La heurística emplea la distancia euclidiana entre posiciones didácticas. El programa conserva el mejor costo conocido y el predecesor de cada nodo; al alcanzar el destino reconstruye la secuencia completa. Dijkstra usa la misma estructura sin heurística y actúa como oráculo de comparación."),
    p("Resultados de las pruebas", "H1x"), table([["Caso", "Condición", "Resultado"], ["1", "Portal Norte a Calle 100", "Ruta válida; 22 minutos; 8 nodos explorados."], ["2", "Portal Norte a Portal El Dorado", "A* y Dijkstra: mismo costo de 81 minutos."], ["3", "Calle 76 cerrada", "Ruta alternativa Heroes-Calle 72; 44 minutos."], ["4", "Calle 26 cerrada", "No existe ruta al Portal El Dorado."], ["5", "Origen inexistente", "Mensaje de error controlado."], ["6", "Origen igual al destino", "Consulta rechazada."], ["7", "Regla de transbordo", "Calle 26: verdadero; Marly: falso."]], [1.2*cm, 6*cm, 8.3*cm]),
    p("La ejecución de <font name='Courier'>python -m unittest discover -s tests -v</font> produjo siete pruebas correctas en Python. La comparación del caso extenso confirmó que A* y Dijkstra alcanzan el mismo costo. El cierre de Calle 76 activó una alternativa, mientras que el cierre de Calle 26 separó el destino del resto del grafo."),
    p("Limitaciones", "H1x"), p("El modelo no incluye horarios, congestión, frecuencia, sentidos operativos ni todos los servicios. Las coordenadas no son geográficas y los costos no son oficiales. Estas decisiones mantienen un alcance reproducible y permiten concentrarse en reglas y búsqueda."),
    p("Conclusiones", "H1x"), p("La integración de hechos, reglas y A* permitió obtener rutas explicables y reaccionar ante restricciones. Las reglas impiden que el algoritmo utilice estados inválidos; la heurística orienta la exploración; y Dijkstra ofrece una referencia independiente del costo mínimo. Las pruebas muestran que separar conocimiento, inferencia, búsqueda e interfaz mejora la verificabilidad del sistema."), PageBreak(),
    p("Referencias", "H1x"),
    p("Benítez, R. (2014). <i>Inteligencia artificial avanzada</i>. Editorial UOC. Capítulos 2, 3 y 9.", "Smallx"),
    p("Python Software Foundation. (2026). <i>Python 3 documentation</i>. https://docs.python.org/3/", "Smallx"),
    p("Russell, S. J., &amp; Norvig, P. (2021). <i>Artificial intelligence: A modern approach</i> (4th ed.). Pearson.", "Smallx"),
    p("TransMilenio S. A. (2026). <i>Sistema TransMilenio</i>. https://www.transmilenio.gov.co/", "Smallx"),
    p("Repositorio", "H1x"), p(f'<link href="{REPO}">{REPO}</link>', "Linkx")]
document(REPORT, "Informe de pruebas - Actividad 2").build(report)

delivery = cover("Documento de entrega")
delivery += [p("Descripción", "H1x"), p("Sistema académico desarrollado en Python que combina una base de conocimiento, cinco reglas lógicas, el algoritmo A* y pruebas comparativas con Dijkstra para recomendar rutas en una red simplificada de TransMilenio."),
    p("Código fuente e instrucciones", "H1x"), p(f'<link href="{REPO}">{REPO}</link>', "Linkx"),
    p("Informe de pruebas", "H1x"), p(f'<link href="{REPO}/blob/main/docs/Informe_Pruebas_Actividad_2.pdf">{REPO}/blob/main/docs/Informe_Pruebas_Actividad_2.pdf</link>', "Linkx"),
    p("Video explicativo", "H1x"), p(VIDEO, "Linkx"),
    p("Observación", "H1x"), p("Entrega individual. El repositorio es público para permitir la revisión. La invitación formal como colaboradora se enviará cuando se disponga del usuario o correo de GitHub de la docente. Antes de entregar, se debe reemplazar el texto pendiente por el enlace público o no listado del video."),
    p("Fecha límite", "H1x"), p("27 de septiembre de 2026, antes de las 23:59 (hora de Bogotá).")]
document(DELIVERY, "Entrega - Actividad 2").build(delivery)
print(REPORT)
print(DELIVERY)

