from fpdf import FPDF
from fpdf.enums import XPos, YPos

FONTS = r"C:\Windows\Fonts"

class PARCHPDF(FPDF):
    def setup_fonts(self):
        self.add_font("Arial",  "",   FONTS + r"\arial.ttf")
        self.add_font("Arial",  "B",  FONTS + r"\arialbd.ttf")
        self.add_font("Arial",  "I",  FONTS + r"\ariali.ttf")
        self.add_font("Arial",  "BI", FONTS + r"\arialbi.ttf")
        self.add_font("Mono",   "",   FONTS + r"\cour.ttf")
        self.add_font("Mono",   "B",  FONTS + r"\courbd.ttf")

    def header(self):
        if self.page_no() > 1:
            self.set_font("Arial", "I", 8)
            self.set_text_color(120, 120, 120)
            self.cell(0, 8, "PARCH — Reporte Técnico Completo", align="L")
            self.cell(0, 8, f"Página {self.page_no()}", align="R",
                      new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_text_color(0, 0, 0)
            self.ln(2)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, "PARCH — Sistema Personal Autónomo de Respuesta e Control Holístico",
                  align="C")

    # ── PORTADA ────────────────────────────────────────────────────────────
    def cover_page(self):
        self.add_page()
        self.set_fill_color(10, 10, 20)
        self.rect(0, 0, 210, 297, "F")

        self.set_draw_color(80, 140, 255)
        self.set_line_width(1)
        self.line(20, 60, 190, 60)

        self.set_y(70)
        self.set_font("Arial", "B", 52)
        self.set_text_color(80, 140, 255)
        self.cell(0, 20, "PARCH", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.set_font("Arial", "", 13)
        self.set_text_color(180, 200, 255)
        self.cell(0, 10,
                  "Sistema Personal Autónomo de Respuesta e Control Holístico",
                  align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.ln(5)
        self.line(20, self.get_y(), 190, self.get_y())

        self.ln(15)
        self.set_font("Arial", "", 11)
        self.set_text_color(140, 160, 200)
        self.set_x(30)
        self.multi_cell(150, 7,
            "Sistema operativo personal con identidad visual propia, inteligencia artificial "
            "integrada via Claude API, control por voz, reconocimiento facial y gestual, "
            "aplicación móvil, integración con hardware físico y nube privada encriptada.",
            align="C")

        self.ln(20)
        badges = [
            ("JARVIS-STYLE AI",  80, 140, 255),
            ("LINUX BASE",       60, 180, 100),
            ("SELF-HOSTED",     200, 100,  60),
            ("OPEN SOURCE",     160,  80, 200),
        ]
        total_w = len(badges) * 42 + (len(badges) - 1) * 6
        start_x = (210 - total_w) / 2
        badge_y = self.get_y()
        for i, (label, r, g, b) in enumerate(badges):
            self.set_xy(start_x + i * 48, badge_y)
            self.set_fill_color(r, g, b)
            self.set_text_color(255, 255, 255)
            self.set_font("Arial", "B", 7)
            self.cell(42, 8, label, align="C", fill=True)

        self.set_y(220)
        meta = [
            ("Versión", "1.0 - Plan de Arquitectura"),
            ("Fecha",   "28 de mayo de 2026"),
            ("Estado",  "Planificación completada - listo para desarrollo"),
            ("Autor",   "franpuchala8@gmail.com"),
        ]
        for label, value in meta:
            self.set_x(50)
            self.set_font("Arial", "B", 10)
            self.set_text_color(80, 140, 255)
            self.cell(40, 8, label + ":", align="R")
            self.set_font("Arial", "", 10)
            self.set_text_color(180, 200, 255)
            self.cell(0, 8, value, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.set_y(260)
        self.set_draw_color(40, 60, 100)
        self.line(20, self.get_y(), 190, self.get_y())
        self.ln(5)
        self.set_font("Arial", "I", 9)
        self.set_text_color(60, 80, 120)
        self.cell(0, 8, "Documento confidencial - uso personal", align="C")

    # ── ÍNDICE ─────────────────────────────────────────────────────────────
    def toc_page(self):
        self.add_page()
        self.section_title("Índice de Contenidos")
        entries = [
            ("1.",      "Visión General del Proyecto",                  "3"),
            ("2.",      "Arquitectura General",                         "4"),
            ("3.",      "Hardware",                                     "5"),
            ("4.",      "Stack Tecnológico",                            "7"),
            ("5.",      "Módulos en Detalle",                           "8"),
            ("  5.1",   "Módulo 1 — Experiencia de Boot",               "8"),
            ("  5.2",   "Módulo 2 — Orquestador de IA (estilo Siri)",   "9"),
            ("  5.3",   "Módulo 3 — Voz",                               "10"),
            ("  5.4",   "Módulo 4 — Visión",                            "10"),
            ("  5.5",   "Módulo 5 — App del Celular",                   "11"),
            ("  5.6",   "Módulo 6 — Cuarto (Raspberry Pi + Arduino)",   "12"),
            ("  5.7",   "Módulo 7 — Nube Propia",                       "12"),
            ("  5.8",   "Módulo 8 — Seguridad",                         "13"),
            ("  5.9",   "Módulo 9 — Módulos 3D y Plugins",              "13"),
            ("  5.10",  "Módulo 10 — Control Gestual en Blender",       "14"),
            ("6.",      "Workflow de Desarrollo",                       "15"),
            ("7.",      "Fases de Desarrollo",                          "16"),
            ("8.",      "Análisis de Riesgos y Soluciones",             "19"),
            ("9.",      "Inversión Estimada (revisada)",                "21"),
            ("10.",     "Próximo Paso",                                  "22"),
        ]
        self.ln(4)
        for num, title, page in entries:
            is_sub = num.startswith("  ")
            sz = 9 if is_sub else 10
            self.set_font("Arial", "" if is_sub else "B", sz)
            self.set_text_color(60 if is_sub else 20, 60 if is_sub else 20, 60 if is_sub else 20)
            self.set_x(20)
            self.cell(15, 7, num)
            self.set_x(35)
            dot_count = max(0, int((145 - self.get_string_width(title) - 8) /
                                   max(self.get_string_width("."), 0.1)))
            dots = "." * dot_count
            self.cell(145, 7, title + "  " + dots, new_x=XPos.RIGHT, new_y=YPos.LAST)
            self.set_text_color(80, 140, 255)
            self.set_font("Arial", "B", sz)
            self.cell(10, 7, page, align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_text_color(0, 0, 0)

    # ── HELPERS ────────────────────────────────────────────────────────────
    def section_title(self, title, level=1):
        self.ln(4)
        if level == 1:
            self.set_fill_color(10, 30, 80)
            self.set_text_color(255, 255, 255)
            self.set_font("Arial", "B", 14)
            self.cell(0, 10, "  " + title, fill=True,
                      new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        else:
            self.set_text_color(30, 80, 180)
            self.set_font("Arial", "B", 12)
            self.ln(2)
            self.cell(0, 8, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_draw_color(100, 150, 255)
            self.set_line_width(0.3)
            self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.set_text_color(0, 0, 0)
        self.ln(3)

    def body_text(self, text, indent=0):
        self.set_font("Arial", "", 10)
        self.set_text_color(40, 40, 40)
        self.set_x(self.l_margin + indent)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def code_block(self, text):
        self.set_fill_color(240, 242, 248)
        self.set_draw_color(200, 210, 230)
        self.set_line_width(0.3)
        lines = text.strip().split("\n")
        h = len(lines) * 5.5 + 6
        self.rect(self.l_margin, self.get_y(), 170, h, "FD")
        self.set_y(self.get_y() + 3)
        self.set_font("Mono", "", 8)
        self.set_text_color(30, 50, 100)
        for line in lines:
            self.set_x(self.l_margin + 3)
            self.cell(0, 5.5, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(0, 0, 0)
        self.ln(4)

    def info_table(self, headers, rows, col_widths=None):
        n = len(headers)
        if col_widths is None:
            col_widths = [170 // n] * n
        self.set_fill_color(20, 50, 120)
        self.set_text_color(255, 255, 255)
        self.set_font("Arial", "B", 9)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 8, "  " + h, fill=True, border=1)
        self.ln()
        for ri, row in enumerate(rows):
            bg = (245, 248, 255) if ri % 2 == 0 else (255, 255, 255)
            self.set_fill_color(*bg)
            self.set_text_color(30, 30, 30)
            self.set_font("Arial", "", 9)
            y_start = self.get_y()
            x_start = self.l_margin
            max_h = 6
            for i, cell in enumerate(row):
                lines = self.multi_cell(col_widths[i], 6, "  " + str(cell),
                                        dry_run=True, output="LINES")
                max_h = max(max_h, len(lines) * 6)
            for i, cell in enumerate(row):
                self.set_xy(x_start + sum(col_widths[:i]), y_start)
                self.multi_cell(col_widths[i], 6, "  " + str(cell),
                                fill=True, border=1, max_line_height=6)
                drawn_h = (self.get_y() - y_start)
                if drawn_h < max_h:
                    self.set_xy(x_start + sum(col_widths[:i]), self.get_y())
                    self.cell(col_widths[i], max_h - drawn_h, "", fill=True, border=1)
            self.set_y(y_start + max_h)
        self.ln(5)

    def bullet(self, text, level=0):
        indent = 5 + level * 8
        char = "•" if level == 0 else "◦"
        self.set_font("Arial", "", 10)
        self.set_text_color(40, 40, 40)
        self.set_x(self.l_margin + indent)
        self.cell(6, 6, char)
        self.set_x(self.l_margin + indent + 6)
        self.multi_cell(0, 6, text)

    def highlight_box(self, title, text, color=(230, 240, 255)):
        self.set_fill_color(*color)
        self.set_draw_color(80, 140, 255)
        self.set_line_width(0.5)
        y0 = self.get_y()
        self.set_font("Arial", "B", 10)
        self.set_text_color(20, 60, 150)
        self.set_x(self.l_margin + 3)
        self.multi_cell(164, 6, title, fill=True)
        self.set_font("Arial", "", 9)
        self.set_text_color(40, 40, 80)
        self.set_x(self.l_margin + 3)
        self.multi_cell(164, 5.5, text, fill=True)
        self.rect(self.l_margin, y0, 170, self.get_y() - y0, "D")
        self.ln(4)


# ── CONTENIDO ───────────────────────────────────────────────────────────────
def build_pdf():
    pdf = PARCHPDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_margins(20, 20, 20)
    pdf.setup_fonts()

    # PORTADA
    pdf.cover_page()

    # ÍNDICE
    pdf.toc_page()

    # ── 1. VISIÓN GENERAL ─────────────────────────────────────────────────
    pdf.add_page()
    pdf.section_title("1. Visión General del Proyecto")
    pdf.body_text(
        "PARCH es un sistema operativo personal e inteligente con identidad visual propia, "
        "construido sobre Linux pero completamente invisible como tal. Al encender la computadora, "
        "el usuario ve únicamente la interfaz de PARCH: su logo, sus animaciones, su diseño. "
        "Debajo corre Linux como motor, pero jamás aparece ante el usuario."
    )
    pdf.body_text(
        "El núcleo del sistema es un orquestador que conecta al usuario con Claude (la IA de "
        "Anthropic) para responder preguntas, ejecutar tareas y controlar el entorno. PARCH no "
        "es una IA en sí mismo — es un sistema que sabe cuándo y cómo hablarle a Claude para "
        "obtener la mejor respuesta posible."
    )
    pdf.body_text(
        "El sistema se extiende al celular como control remoto y espejo de pantalla, al cuarto "
        "físico a través de Arduino y Raspberry Pi, y a una nube privada encriptada alojada en "
        "el propio hardware del usuario."
    )
    pdf.section_title("Principios de Diseño", level=2)
    principles = [
        ("Invisibilidad tecnológica",
         "El usuario nunca ve Linux, terminales ni configuraciones. Solo ve PARCH."),
        ("Claude como cerebro",
         "Toda inteligencia viene de Claude API. PARCH es el cuerpo, Claude el cerebro."),
        ("Privacidad total",
         "Los datos nunca salen de la casa del usuario. Nube propia, encriptada."),
        ("Modularidad",
         "Cada función es un módulo independiente que se puede agregar o quitar."),
        ("Control físico real",
         "PARCH interactúa con el mundo real via Arduino y Raspberry Pi."),
        ("Acceso global",
         "Desde cualquier parte del mundo el usuario puede hablar con PARCH via celular."),
    ]
    for ptitle, desc in principles:
        pdf.set_font("Arial", "B", 10)
        pdf.set_text_color(20, 60, 150)
        pdf.set_x(pdf.l_margin + 5)
        pdf.cell(6, 6, "•")
        pdf.set_x(pdf.l_margin + 11)
        pdf.cell(0, 6, ptitle + ":", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("Arial", "", 10)
        pdf.set_text_color(60, 60, 60)
        pdf.set_x(pdf.l_margin + 17)
        pdf.multi_cell(0, 6, desc)
        pdf.ln(1)

    # ── 2. ARQUITECTURA ───────────────────────────────────────────────────
    pdf.add_page()
    pdf.section_title("2. Arquitectura General")
    pdf.body_text(
        "PARCH se compone de cuatro nodos principales que se comunican entre sí: "
        "el Mini PC central (siempre encendido), el celular del usuario, el hub del cuarto "
        "(Raspberry Pi + Arduino), y la PC de desarrollo (Windows con RTX 3050)."
    )
    pdf.code_block(
"""MINI PC - PARCH (siempre encendido)
+----------------------------------------------------------+
|  Boot Layer          Orquestador Central                 |
|  Tu logo       -->   Recibe input -> decide accion       |
|  Tu animacion        -> habla con Claude API             |
|                                |                         |
|  Modulo Voz    Modulo Vision   Claude API                |
|  Whisper       MediaPipe       (cerebro)                 |
|                                                          |
|  Interfaz Visual  (Electron + Three.js)                  |
|  Nube Propia      (Nextcloud encriptada)                 |
+------------------------+---------------------------------+
                         | WiFi / VPN WireGuard
         +---------------+---------------+
         |               |               |
  Celular (app)    Raspberry Pi 5   PC Windows
  React Native     Hub del cuarto   (desarrollo)
  Mirror pantalla  + Arduino        RTX 3050
  Voz / texto      Luces/sensores   git push -> PARCH""")

    pdf.section_title("Flujo de datos principal", level=2)
    pdf.code_block(
"""Usuario habla: "Hey PARCH, que temperatura hace afuera?"
         |
Porcupine detecta wake word (OFFLINE)
         |
Whisper transcribe el audio (LOCAL)
         |
Orquestador PARCH recibe el texto
         |
Claude API procesa la pregunta
         |
Claude responde
         |
Piper TTS convierte respuesta a voz (LOCAL)
         |
PARCH habla al usuario""")

    # ── 3. HARDWARE ───────────────────────────────────────────────────────
    pdf.add_page()
    pdf.section_title("3. Hardware")

    pdf.section_title("3.1 Mini PC — Cerebro Principal", level=2)
    pdf.body_text(
        "El Mini PC es el corazón de PARCH. Corre las 24 horas los 7 días de la semana "
        "con bajo consumo eléctrico. IMPORTANTE: la recomendación fue revisada al incorporar "
        "Blender + control gestual al proyecto. Estos procesos requieren una GPU integrada "
        "significativamente más potente que la generación anterior."
    )
    pdf.highlight_box(
        "RECOMENDADO (revisado): MINISFORUM UM790 Pro — ~$370 USD",
        "AMD Ryzen 9 7940HS (8 nucleos, 4.0GHz boost)  |  32 GB DDR5  |  1 TB NVMe SSD\n"
        "GPU: Radeon 780M RDNA3 (12 CUs, ~4.4 TFLOPS)  |  WiFi 6E + Bluetooth 5.2\n"
        "Consumo: ~35W en uso  |  Compatible 100% con Linux  |  Silencioso",
        color=(220, 240, 220)
    )
    pdf.highlight_box(
        "Por que no el Beelink SER5 MAX original (~$290)?",
        "El SER5 MAX tiene GPU Vega 8 (~1.5 TFLOPS). Corriendo Blender + MediaPipe "
        "simultaneamente, la GPU se satura y los gestos se vuelven lentos e imprecisos. "
        "La Radeon 780M del UM790 Pro es 3x mas potente y maneja ambos sin problemas. "
        "La diferencia de $80 es necesaria para la experiencia que se busca.",
        color=(255, 240, 220)
    )
    pdf.section_title("Comparativa de Mini PCs — con rating para PARCH completo", level=2)
    pdf.info_table(
        ["Modelo", "GPU Integrada", "TFLOPS", "Para PARCH", "Precio"],
        [
            ["GMKtec NucBox G3",      "Intel UHD",       "~0.4",  "Solo funciones basicas", "~$140"],
            ["Beelink SER5 MAX",      "Vega 8 (RDNA1)",  "~1.5",  "Sin Blender: OK",        "~$300"],
            ["MINISFORUM UM790 Pro**","Radeon 780M(RDNA3)","~4.4","PARCH completo: SI",     "~$370"],
            ["Beelink GTR7 Pro",      "Radeon 780M",     "~4.4",  "PARCH completo: SI",     "~$460"],
            ["MINISFORUM HX200G",     "Radeon 890M",     "~5.3",  "PARCH completo: SI",     "~$550"],
        ],
        col_widths=[46, 42, 18, 42, 22]
    )
    pdf.body_text("**  Recomendado: mejor relacion precio/potencia para PARCH con Blender")

    pdf.section_title("3.2 Raspberry Pi 5 — Hub del Cuarto", level=2)
    pdf.body_text(
        "El Raspberry Pi NO corre PARCH. Su único trabajo es ser el intermediario entre "
        "el Mini PC y los dispositivos físicos del cuarto. Recibe órdenes del Mini PC y "
        "las ejecuta en el mundo físico."
    )
    pdf.info_table(
        ["Especificación", "Detalle"],
        [
            ["Modelo",           "Raspberry Pi 5 (8GB RAM)"],
            ["Rol en PARCH",     "Controlador del cuarto físico"],
            ["Conectado a",      "Arduino via USB / Mini PC via WiFi (MQTT)"],
            ["Precio aprox.",    "~$80-100 USD"],
        ],
        col_widths=[60, 110]
    )

    pdf.section_title("3.3 Diferencia clave: Raspberry Pi vs Mini PC", level=2)
    pdf.info_table(
        ["Característica", "Raspberry Pi 5", "Mini PC (x86)"],
        [
            ["Chip",                  "ARM (como celular)",    "x86 (como PC normal)"],
            ["RAM maxima",            "8 GB",                  "32+ GB"],
            ["Linux completo",        "Si, pero limitado",     "Si, sin problemas"],
            ["Modelos de IA",         "No puede",              "Si (los pequenos)"],
            ["Vision en tiempo real", "Limitado",              "Sin problemas"],
            ["Consumo de energia",    "5-15W",                 "15-65W"],
            ["Precio",                "~$80-100 USD",          "$130-500 USD"],
            ["Ideal para",            "Sensores, Arduino, IoT","Cerebro principal PARCH"],
        ],
        col_widths=[55, 57, 58]
    )

    pdf.section_title("3.4 Arduino y Cámara", level=2)
    pdf.bullet("Arduino: Ya lo tenés. Se conecta al Raspberry Pi por USB.")
    pdf.bullet("Camara: DEBE ser 60fps para control gestual fluido. Logitech C922 (~$75 USD).")
    pdf.bullet("Camara a 30fps: el gesto y la pantalla van desincronizados, la experiencia se siente torpe.")
    pdf.bullet("Microfono: Bluetooth, compatible nativo con Linux via BlueZ.")

    # ── 4. STACK TECNOLÓGICO ──────────────────────────────────────────────
    pdf.add_page()
    pdf.section_title("4. Stack Tecnológico")

    pdf.section_title("4.1 Sistema Operativo Base", level=2)
    pdf.info_table(
        ["Capa", "Tecnología", "Para qué"],
        [
            ["Base",              "Ubuntu Server 24.04 LTS",    "Linux invisible, base estable"],
            ["Bootloader",        "GRUB2 con tema custom",       "Primera pantalla: tu logo"],
            ["Animación de carga","Plymouth custom",             "Tu animación mientras carga"],
            ["Compositor",        "Hyprland (Wayland)",          "Gestor de ventanas moderno"],
            ["Interfaz principal","Electron (Node + Chromium)",  "La UI que ve el usuario"],
        ],
        col_widths=[38, 55, 77]
    )

    pdf.section_title("4.2 Backend — Python (el cerebro)", level=2)
    pdf.info_table(
        ["Módulo", "Librería / Herramienta"],
        [
            ["Claude API",              "anthropic SDK oficial"],
            ["Reconocimiento de voz",   "Whisper (OpenAI, corre local)"],
            ["Palabra de activación",   "Porcupine (offline, sin internet)"],
            ["Síntesis de voz",         "Piper TTS (local)"],
            ["Visión: cara/ojo/gestos", "MediaPipe + OpenCV"],
            ["Comunicación con RPi",    "MQTT protocol (paho-mqtt)"],
            ["API interna",             "FastAPI (REST)"],
            ["Base de datos",           "PostgreSQL"],
        ],
        col_widths=[70, 100]
    )

    pdf.section_title("4.3 Frontend — JavaScript/TypeScript (lo que se ve)", level=2)
    pdf.info_table(
        ["Módulo", "Tecnología"],
        [
            ["Interfaz principal",         "Electron + React"],
            ["Módulos 3D",                 "Three.js"],
            ["Animaciones",                "Framer Motion"],
            ["App del celular",            "React Native"],
            ["Mirror de pantalla",         "WebRTC"],
            ["Comunicación en tiempo real","WebSocket"],
        ],
        col_widths=[70, 100]
    )

    pdf.section_title("4.4 Infraestructura", level=2)
    pdf.info_table(
        ["Servicio", "Tecnología"],
        [
            ["Nube propia",             "Nextcloud (self-hosted)"],
            ["VPN remota",              "WireGuard"],
            ["Encriptación de disco",   "LUKS2"],
            ["Backup automático",       "Restic"],
            ["Sincronización de código","Git + SSH"],
        ],
        col_widths=[70, 100]
    )

    # ── 5. MÓDULOS ────────────────────────────────────────────────────────
    pdf.add_page()
    pdf.section_title("5. Módulos en Detalle")

    pdf.section_title("Módulo 1 — Experiencia de Boot", level=2)
    pdf.body_text(
        "Al encender el Mini PC, el usuario jamás ve una terminal, un menú de Linux "
        "ni nada que no sea PARCH. El flujo completo es:"
    )
    pdf.code_block(
"""Encendido
   |
GRUB (oculto, 0.5 seg) -> muestra tu logo
   |
Plymouth -> animacion de carga personalizada (3-5 seg)
   |
Hyprland inicia (invisible para el usuario)
   |
Electron lanza la interfaz de PARCH (pantalla completa)
   |
Reconocimiento facial -> desbloqueas con tu cara
   |
PARCH listo para usar""")

    pdf.section_title("Módulo 2 — Orquestador de IA (estilo Siri)", level=2)
    pdf.body_text(
        "PARCH no es inteligente por sí mismo. Su inteligencia viene 100% de Claude. "
        "El orquestador decide qué hacer con cada pedido del usuario:"
    )
    pdf.code_block(
"""Input del usuario (voz o texto)
        |
Orquestador analiza el tipo de pedido:
        |-- Pregunta general    -> Claude API -> muestra respuesta
        |-- "Busca en internet" -> abre ventana Google real
        |                         -> da resultado a Claude -> responde
        |-- "Apaga la luz"      -> comando a Raspberry Pi -> Arduino
        |-- "Abre el archivo X" -> accion en sistema de archivos
        +-- "Recuerda que..."   -> guarda en base de datos local""")

    pdf.highlight_box(
        "Regla de Internet",
        "PARCH NUNCA busca en internet por su cuenta. Solo busca si el usuario lo pide "
        "explicitamente ('busca', 'googlea', 'checkea en internet'). Cuando lo hace, "
        "abre una ventana real de Google — el usuario ve la busqueda.",
        color=(255, 240, 220)
    )

    pdf.add_page()
    pdf.section_title("Módulo 3 — Sistema de Voz", level=2)
    pdf.code_block(
"""Siempre escuchando (OFFLINE) -> detecta "Hey PARCH"
        |
Activa microfono activo
        |
Whisper transcribe lo que decis (LOCAL, privado)
        |
Texto va al Orquestador
        |
Claude API responde
        |
Piper TTS convierte respuesta a voz (LOCAL)
        |
PARCH te habla""")
    pdf.body_text(
        "El reconocimiento de la palabra de activación corre 100% offline. "
        "Nadie escucha nada hasta que pronunciás 'Hey PARCH'. "
        "El micrófono Bluetooth funciona igual que uno cableado, BlueZ lo gestiona de forma nativa."
    )

    pdf.section_title("Módulo 4 — Sistema de Visión", level=2)
    pdf.info_table(
        ["Función", "Tecnología", "Comportamiento"],
        [
            ["Login facial",       "MediaPipe + DeepFace", "Al encender, PARCH te reconoce y desbloquea"],
            ["Detección presencia","YOLOv8",               "Si te alejás, PARCH puede bloquearse solo"],
            ["Gestos con mano",    "MediaPipe Hands",      "Mano abierta = activar / puño = pausar"],
            ["Detección del ojo",  "OpenCV + dlib",        "Capa extra de seguridad configurable"],
        ],
        col_widths=[40, 45, 85]
    )

    pdf.section_title("Módulo 5 — App del Celular", level=2)
    for t, d in [
        ("1. Chat remoto",
         "Desde cualquier parte del mundo, escribís o hablás y PARCH responde via Claude. "
         "Las conversaciones se guardan en tu nube propia."),
        ("2. Mirror de pantalla (como Chromecast)",
         "Ves en tiempo real lo que está en la pantalla del Mini PC. Podés navegar "
         "la interfaz con el dedo desde el celular, como si fuera un touchpad remoto."),
        ("3. Desbloqueo remoto con frase de seguridad",
         "Si PARCH está bloqueado, la app te pide una frase secreta. Al confirmarla, "
         "PARCH se desbloquea. La conexión siempre va via VPN WireGuard."),
    ]:
        pdf.set_font("Arial", "B", 10)
        pdf.set_text_color(20, 60, 150)
        pdf.set_x(pdf.l_margin + 5)
        pdf.cell(0, 7, t, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("Arial", "", 10)
        pdf.set_text_color(50, 50, 50)
        pdf.set_x(pdf.l_margin + 12)
        pdf.multi_cell(0, 6, d)
        pdf.ln(2)

    pdf.add_page()
    pdf.section_title("Módulo 6 — Cuarto Físico (Raspberry Pi + Arduino)", level=2)
    pdf.code_block(
"""Vos: "Hey PARCH, apaga las luces del cuarto"
        |
PARCH Orquestador interpreta la accion
        |
Envia comando MQTT al Raspberry Pi 5
        |
Raspberry Pi envia señal al Arduino por USB
        |
Arduino activa el relay
        |
Luces apagadas""")
    pdf.body_text(
        "El Raspberry Pi puede manejar múltiples Arduinos, sensores de temperatura, "
        "humedad, movimiento y cualquier dispositivo que se agregue en el futuro. "
        "Es el 'mayordomo físico' de PARCH."
    )

    pdf.section_title("Módulo 7 — Nube Propia", level=2)
    pdf.info_table(
        ["Servicio", "Tecnología", "Descripción"],
        [
            ["Almacenamiento", "Nextcloud (self-hosted)", "Como Google Drive, pero en tu casa"],
            ["Base de datos",  "PostgreSQL",              "Conversaciones, logs, config de PARCH"],
            ["Backup auto",    "Restic",                  "Copias de seguridad incrementales"],
            ["Encriptación",   "LUKS2 + TLS",             "Disco encriptado + tráfico encriptado"],
        ],
        col_widths=[35, 55, 80]
    )

    pdf.section_title("Módulo 8 — Seguridad", level=2)
    pdf.info_table(
        ["Amenaza", "Protección"],
        [
            ["Alguien usa la PC físicamente",   "Reconocimiento facial obligatorio al inicio"],
            ["Intento de acceso por red",        "VPN WireGuard + firewall estricto"],
            ["Robo del Mini PC",                 "LUKS2 — disco encriptado, sin clave no se lee nada"],
            ["Acceso remoto no autorizado",      "Frase de seguridad en la app del celular"],
            ["Fuerza bruta a la VPN",            "WireGuard usa ECC — inmune a fuerza bruta"],
        ],
        col_widths=[80, 90]
    )

    pdf.section_title("Módulo 9 — Módulos 3D y Sistema de Plugins", level=2)
    pdf.body_text(
        "PARCH está diseñado para crecer. Cualquier nueva función se agrega como un módulo "
        "sin tocar el núcleo del sistema. Los módulos 3D usan Three.js y se construyen "
        "como páginas web independientes que PARCH muestra en su interfaz."
    )
    pdf.code_block(
"""PARCH Core (estable, no se toca)
+-- Sistema de Modulos
    |-- Modulo: Clima       (muestra el tiempo en 3D)
    |-- Modulo: Musica      (control de reproductores)
    |-- Modulo: Tareas      (lista de pendientes)
    |-- Modulo: Cuarto      (control del Arduino)
    +-- [cualquier modulo futuro]""")

    pdf.section_title("Módulo 10 — Control Gestual en Blender", level=2)
    pdf.body_text(
        "Este módulo conecta MediaPipe con Blender para que puedas modelar objetos 3D "
        "usando únicamente tus manos frente a la cámara, como Tony Stark con sus hologramas. "
        "PARCH actúa como traductor entre tus gestos y las acciones en Blender."
    )
    pdf.code_block(
"""Tu mano frente a la camara
        |
MediaPipe detecta 21 puntos de la mano en tiempo real
        |
PARCH interpreta el gesto
        |
PARCH envia el comando a Blender via Python API (bpy)
        |
El objeto 3D en Blender responde a tu movimiento""")

    pdf.info_table(
        ["Gesto", "Acción en Blender"],
        [
            ["Indice apuntando + mover",         "Mover cursor en el viewport 3D"],
            ["Pinza (pulgar+indice) en objeto",   "Seleccionar / agarrar objeto"],
            ["Pinza sostenida + mover mano",      "Mover el objeto en el espacio 3D"],
            ["Girar la muneca con pinza",         "Rotar el objeto"],
            ["Dos manos alejandose",              "Escalar objeto mas grande"],
            ["Dos manos acercandose",             "Escalar objeto mas pequeno"],
            ["Palma abierta + mover",             "Orbitar la camara del viewport"],
            ["Pellizco + scroll vertical",        "Zoom in / zoom out"],
            ["Swipe rapido horizontal",           "Eliminar objeto seleccionado"],
        ],
        col_widths=[85, 85]
    )
    pdf.body_text(
        "Estructura del modulo en el codigo de PARCH:"
    )
    pdf.code_block(
"""parch/modules/blender_hands/
    |-- hand_tracker.py     <- MediaPipe, lee la camara a 60fps
    |-- gesture_engine.py   <- interpreta que gesto es
    |-- blender_bridge.py   <- habla con Blender via Python API
    +-- calibration.py      <- calibras tu espacio de trabajo""")
    pdf.highlight_box(
        "Requerimiento de hardware para este modulo",
        "Esta feature requiere la GPU Radeon 780M (UM790 Pro) o superior. "
        "Con GPU Vega 8 (SER5 MAX), MediaPipe a 60fps + Blender viewport "
        "compiten por la GPU y el resultado es laggy e inutilizable.",
        color=(255, 235, 235)
    )

    # ── 6. WORKFLOW ───────────────────────────────────────────────────────
    pdf.add_page()
    pdf.section_title("6. Workflow de Desarrollo")
    pdf.body_text(
        "Todo el código se escribe en la PC Windows actual (con RTX 3050) y se despliega "
        "al Mini PC PARCH. No es necesario reiniciar el Mini PC en cada cambio: PARCH "
        "está diseñado para recargar módulos en caliente."
    )
    pdf.code_block(
"""Tu PC Windows (aca programas)
+-- VS Code con extension Remote SSH
+-- Git instalado
+-- Python + Node.js instalados localmente

            |
            |  git push / SSH directo
            v

Mini PC PARCH Linux (aca corre el sistema)
+-- Mismo codigo, corre en Linux
+-- git pull automatico al recibir cambios
+-- PARCH recarga el modulo modificado automaticamente""")

    pdf.section_title("VS Code Remote SSH", level=2)
    pdf.body_text(
        "Con la extensión Remote SSH de VS Code, podés programar en Windows pero "
        "el código se ejecuta en tiempo real en el Linux del Mini PC. "
        "Es como si estuvieras ahí: ves los archivos del Mini PC, los editás, "
        "y los cambios se aplican instantáneamente."
    )
    pdf.highlight_box(
        "RTX 3050 para pruebas locales",
        "Tu RTX 3050 en Windows puede usarse para probar partes del sistema que "
        "requieren GPU (vision, modelos de IA locales) antes de enviarlas al Mini PC. "
        "Esto acelera el desarrollo significativamente.",
        color=(220, 255, 220)
    )

    # ── 7. FASES ──────────────────────────────────────────────────────────
    pdf.add_page()
    pdf.section_title("7. Fases de Desarrollo")

    phases = [
        {
            "title": "Fase 1 — Fundación",
            "time":  "2-3 meses",
            "color": (20, 80, 160),
            "tasks": [
                "Mini PC configurado con Ubuntu Server 24.04 LTS",
                "GRUB con logo PARCH personalizado",
                "Animación Plymouth custom",
                "Electron app básica (pantalla con logo, campo de texto)",
                "Conexión con Claude API funcionando",
                "Primera conversación de texto con PARCH",
            ],
            "result": "Encendés el Mini PC, aparece tu logo, la interfaz de PARCH, escribís algo y PARCH (Claude) te responde.",
        },
        {
            "title": "Fase 2 — Voz y Visión",
            "time":  "2-3 meses",
            "color": (20, 120, 80),
            "tasks": [
                "Whisper integrado — PARCH entiende lo que decís",
                "Porcupine con wake word 'Hey PARCH'",
                "Piper TTS — PARCH te habla en voz",
                "Reconocimiento facial para login automático",
                "Detección básica de gestos con mano",
            ],
            "result": "Decís 'Hey PARCH', respondés con la voz, PARCH te contesta en voz.",
        },
        {
            "title": "Fase 3 — App del Celular",
            "time":  "2 meses",
            "color": (140, 60, 180),
            "tasks": [
                "App React Native básica (iOS + Android)",
                "Chat en tiempo real con PARCH",
                "Mirror de pantalla via WebRTC",
                "VPN WireGuard configurada y funcionando",
                "Desbloqueo remoto con frase de seguridad",
            ],
            "result": "Desde cualquier lugar del mundo, abrís la app y hablás con PARCH.",
        },
        {
            "title": "Fase 4 — Cuarto Físico",
            "time":  "1-2 meses",
            "color": (160, 100, 20),
            "tasks": [
                "Raspberry Pi 5 configurado y conectado",
                "Arduino conectado al RPi y respondiendo",
                "Control de luces por voz",
                "Sensores de presencia funcionando",
            ],
            "result": "'Hey PARCH, apagá las luces' — se apagan.",
        },
        {
            "title": "Fase 5 — Nube y Seguridad",
            "time":  "1-2 meses",
            "color": (180, 40, 60),
            "tasks": [
                "Nextcloud instalado y accesible desde el celular",
                "LUKS2 encriptación del disco del Mini PC",
                "Backup automático con Restic",
                "Sistema de seguridad completo integrado",
            ],
            "result": "Todos los datos guardados y encriptados en tu propia infraestructura.",
        },
        {
            "title": "Fase 6 — Pulido Continuo",
            "time":  "Ongoing",
            "color": (60, 60, 60),
            "tasks": [
                "Módulos 3D con Three.js",
                "Sistema de plugins/skills instalables",
                "Optimización de velocidad y memoria",
                "Refinamiento del diseño visual",
            ],
            "result": "PARCH evoluciona continuamente con nuevas funciones como plugins.",
        },
        {
            "title": "Fase 7 — Blender + Control Gestual 3D",
            "time":  "2-3 meses",
            "color": (20, 120, 140),
            "tasks": [
                "Blender instalado y lanzable desde PARCH con voz",
                "Módulo hand_tracker.py — MediaPipe a 60fps leyendo la cámara",
                "Módulo gesture_engine.py — reconoce pinza, agarre, swipe, escala",
                "Módulo blender_bridge.py — traduce gestos a comandos Blender via Python API",
                "Calibración del espacio de trabajo (distancia mano-cámara)",
                "Gestos básicos: seleccionar, mover, rotar, escalar, borrar",
                "Guardar proyectos 3D en Nextcloud desde Blender",
            ],
            "result": "Paras frente a la cámara, decís 'Hey PARCH abrí Blender', extendés la mano y modelás objetos 3D con gestos como Tony Stark.",
        },
    ]

    for ph in phases:
        r, g, b = ph["color"]
        pdf.set_fill_color(r, g, b)
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Arial", "B", 11)
        pdf.cell(0, 9, f"  {ph['title']}  ({ph['time']})",
                 fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_text_color(0, 0, 0)
        pdf.ln(1)
        for task in ph["tasks"]:
            pdf.set_font("Arial", "", 9)
            pdf.set_text_color(50, 50, 50)
            pdf.set_x(pdf.l_margin + 5)
            pdf.cell(6, 5.5, "[ ]")
            pdf.set_x(pdf.l_margin + 14)
            pdf.multi_cell(0, 5.5, task)
        pdf.set_fill_color(245, 248, 240)
        pdf.set_font("Arial", "I", 9)
        pdf.set_text_color(40, 100, 40)
        pdf.set_x(pdf.l_margin + 5)
        pdf.multi_cell(165, 5.5, "Resultado: " + ph["result"], fill=True)
        pdf.ln(4)

    # ── 8. ANÁLISIS DE RIESGOS ────────────────────────────────────────────
    pdf.add_page()
    pdf.section_title("8. Análisis de Riesgos y Soluciones")
    pdf.body_text(
        "Esta sección documenta todos los problemas potenciales identificados antes "
        "de realizar cualquier inversión. Cada riesgo tiene una solución concreta."
    )
    risks = [
        ("CRÍTICO", (200,50,50),
         "Almacenamiento insuficiente",
         "Un proyecto Blender mediano ocupa 200-500MB. El OS + PARCH + Nextcloud + "
         "PostgreSQL ya usan ~30GB. Con varios proyectos 3D y grabaciones de voz, "
         "500GB se llena en meses.",
         "Pedir el UM790 Pro con 1TB SSD (+$20) o agregar un SSD externo 2TB (~$60)."),
        ("CRITICO", (200,50,50),
         "GPU insuficiente para Blender + MediaPipe simultaneos",
         "Vega 8 (SER5 MAX) tiene ~1.5 TFLOPS. Blender viewport + MediaPipe 60fps "
         "compiten por la GPU. El resultado es lag en gestos e interfaz trabada.",
         "Usar MINISFORUM UM790 Pro con Radeon 780M (~4.4 TFLOPS). 3x mas potente."),
        ("IMPORTANTE", (200,130,30),
         "Camara 30fps — gestos laggy",
         "Webcams baratas corren a 30fps. Para control gestual fluido en Blender "
         "se necesitan 60fps minimo. A 30fps el gesto y la pantalla van desincronizados.",
         "Logitech C922 o C920s (~$70-80 USD). Soportan 60fps a 1080p."),
        ("IMPORTANTE", (200,130,30),
         "App iOS requiere Mac para compilar",
         "Para publicar la app en iPhone se necesita una Mac o servicio de compilacion pago. "
         "El usuario tiene Windows.",
         "Empezar con Android (gratis) + PWA para iOS. Agregar iOS nativo cuando el proyecto este maduro via Expo EAS Build."),
        ("IMPORTANTE", (200,130,30),
         "Sin internet = PARCH sin cerebro",
         "Claude API requiere conexion a internet. Si se corta, PARCH no puede responder.",
         "Instalar Ollama con modelo local (Llama 3.1 8B, ~5GB). PARCH cae al modelo "
         "local automaticamente cuando Claude no esta disponible."),
        ("MEDIO", (150,150,30),
         "Whisper lento sin GPU dedicada",
         "El modelo grande de Whisper tarda 3-5 segundos en procesar voz en CPU. "
         "Hace que PARCH se sienta lento.",
         "Usar Whisper Small: responde en ~0.8 seg, buena precision, balance perfecto "
         "para el hardware del UM790 Pro."),
        ("MENOR", (100,150,50),
         "Corte de luz apaga PARCH abruptamente",
         "Sin UPS, un corte de luz puede corromper la base de datos o archivos en escritura.",
         "UPS basico (~$40-50 USD) da 10-20 minutos — suficiente para apagado limpio."),
        ("MENOR", (100,150,50),
         "Costos API Claude impredecibles",
         "Si PARCH se usa intensivamente todo el dia, el costo por tokens puede superar $20/mes.",
         "Usar plan Claude Pro ($20/mes fijo). Mas predecible que pago por tokens."),
    ]
    for severity, color, title, problem, solution in risks:
        r, g, b = color
        pdf.set_fill_color(r, g, b)
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Arial", "B", 9)
        pdf.cell(22, 7, f" {severity}", fill=True, border=0)
        pdf.set_fill_color(245, 245, 245)
        pdf.set_text_color(20, 20, 20)
        pdf.set_font("Arial", "B", 10)
        pdf.cell(0, 7, f"  {title}", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("Arial", "", 9)
        pdf.set_text_color(80, 30, 30)
        pdf.set_x(pdf.l_margin + 5)
        pdf.multi_cell(165, 5.5, "Problema: " + problem)
        pdf.set_text_color(20, 80, 20)
        pdf.set_x(pdf.l_margin + 5)
        pdf.multi_cell(165, 5.5, "Solucion: " + solution)
        pdf.ln(3)

    # ── 9. INVERSIÓN ──────────────────────────────────────────────────────
    pdf.add_page()
    pdf.section_title("9. Inversión Estimada (Revisada)")

    pdf.section_title("Hardware (pago único) — Lista revisada", level=2)
    pdf.info_table(
        ["Ítem", "Detalle", "Precio aprox. (USD)"],
        [
            ["MINISFORUM UM790 Pro", "Ryzen 9 7940HS, 32GB RAM, 1TB SSD, Radeon 780M", "$370-400"],
            ["Raspberry Pi 5 (8GB)", "Hub del cuarto fisico",                            "$80-100"],
            ["Logitech C922 (60fps)", "Camara 60fps para gestos fluidos",               "$70-80"],
            ["MicroSD 64GB",         "Almacenamiento del Raspberry Pi",                 "$12-15"],
            ["UPS basico",           "Proteccion contra cortes de luz",                 "$40-50"],
            ["TOTAL",                "",                                                 "~$572-645"],
        ],
        col_widths=[50, 88, 32]
    )
    pdf.highlight_box(
        "Comparativa: plan original vs plan revisado",
        "Plan original (sin Blender): ~$407-475 USD\n"
        "Plan revisado (con Blender + gestos): ~$572-645 USD\n"
        "Diferencia: ~$165 USD — necesarios para que Blender + gestos funcionen correctamente.",
        color=(235, 245, 255)
    )

    pdf.section_title("Costos recurrentes (mensuales)", level=2)
    pdf.info_table(
        ["Servicio", "Descripción", "Costo mensual"],
        [
            ["Claude API",      "Plan Pro fijo (recomendado para uso intensivo)", "$20 USD"],
            ["Electricidad",    "Mini PC 35W promedio x 24h x 30 dias",           "~$3-5 USD"],
            ["TOTAL mensual",   "",                                                "~$23-25 USD"],
        ],
        col_widths=[40, 100, 30]
    )

    # ── 10. PRÓXIMO PASO ──────────────────────────────────────────────────
    pdf.section_title("10. Próximo Paso")
    pdf.body_text("El plan está completo y revisado. Los pasos inmediatos para arrancar son:")
    for t, d in [
        ("Paso 1 — Comprar hardware revisado",
         "MINISFORUM UM790 Pro (~$370-400 USD) + Raspberry Pi 5 + Logitech C922 + UPS. "
         "NO comprar el Beelink SER5 MAX si se quiere Blender + gestos."),
        ("Paso 2 — Preparar entorno de desarrollo (ya mismo, sin esperar hardware)",
         "Instalar en la PC Windows: Python 3.11+, Node.js 20+, VS Code con Remote SSH, "
         "Git, y hacer el primer 'Hola PARCH' que llame a la API de Claude."),
        ("Paso 3 — Configurar el Mini PC cuando llegue",
         "Instalar Ubuntu Server 24.04, configurar SSH, boot personalizado con logo PARCH "
         "y desplegar el core del sistema."),
        ("Paso 4 — Desarrollo fase por fase (7 fases)",
         "Seguir las fases en orden: Fundacion, Voz+Vision, Celular, Cuarto, Nube, "
         "Pulido, Blender+Gestos. Completar cada una antes de avanzar. Sin apuros."),
    ]:
        pdf.set_font("Arial", "B", 10)
        pdf.set_text_color(20, 60, 150)
        pdf.set_x(pdf.l_margin + 3)
        pdf.cell(0, 7, t, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("Arial", "", 10)
        pdf.set_text_color(50, 50, 50)
        pdf.set_x(pdf.l_margin + 10)
        pdf.multi_cell(0, 6, d)
        pdf.ln(3)

    # ── PÁGINA FINAL ──────────────────────────────────────────────────────
    pdf.add_page()
    pdf.set_fill_color(10, 10, 20)
    pdf.rect(0, 0, 210, 297, "F")
    pdf.set_y(110)
    pdf.set_font("Arial", "B", 36)
    pdf.set_text_color(80, 140, 255)
    pdf.cell(0, 15, "PARCH", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(5)
    pdf.set_draw_color(80, 140, 255)
    pdf.set_line_width(0.5)
    pdf.line(60, pdf.get_y(), 150, pdf.get_y())
    pdf.ln(8)
    pdf.set_font("Arial", "", 11)
    pdf.set_text_color(140, 170, 220)
    pdf.cell(0, 8, "Sistema Personal Autónomo de Respuesta e Control Holístico",
             align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(15)
    pdf.set_font("Arial", "I", 10)
    pdf.set_text_color(80, 100, 140)
    pdf.cell(0, 8, "franpuchala8@gmail.com",    align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 8, "Version 1.1 — Mayo 2026  |  Incluye Blender + Gestos + Analisis de Riesgos",   align="C")

    out = r"C:\Users\franp\Escritorio\PARCH_Reporte_Tecnico.pdf"
    pdf.output(out)
    print(f"PDF generado correctamente: {out}")


if __name__ == "__main__":
    build_pdf()
