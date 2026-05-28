# PARCH — Contexto completo del proyecto para Claude

> Este archivo contiene toda la información acordada en la sesión de planificación inicial.
> Al leerlo tenés el contexto completo para continuar el desarrollo sin repetir decisiones ya tomadas.

---

## Qué es PARCH

**PARCH** = Sistema Personal Autónomo de Respuesta e Control Holístico

Es un sistema operativo personal con identidad visual completamente propia, construido sobre Linux pero sin que el usuario lo vea jamás. Al encender la computadora aparece únicamente la interfaz de PARCH: su logo, su animación, su diseño. Debajo corre Ubuntu Server, pero es invisible.

La inspiración es **JARVIS de Iron Man**: un sistema que rodea al usuario, responde preguntas, controla el cuarto físico, se maneja con voz y gestos, y está disponible desde el celular en cualquier parte del mundo.

**PARCH no es una IA.** Es el cuerpo. Claude API es el cerebro. Toda inteligencia viene de Claude — PARCH solo sabe cuándo y cómo preguntarle.

---

## Autor

- Nombre: Francisco Puchala
- Email: franpuchala8@gmail.com
- GitHub: FranciscoPuchala
- Nivel técnico: principiante motivado — explicar conceptos con claridad, sin dar por sentado conocimiento previo

---

## Decisiones arquitectónicas — todas confirmadas, no re-consultar

| Decisión | Valor acordado |
|---|---|
| OS base | Ubuntu Server 24.04 LTS (oculto al usuario) |
| Boot | GRUB2 custom → Plymouth custom → Electron fullscreen |
| IA principal | Claude API siempre. PARCH nunca decide solo |
| Búsqueda en internet | SOLO si el usuario lo pide explícitamente. Abre ventana de Google real. |
| Lenguaje backend | Python |
| Lenguaje frontend | JavaScript / TypeScript (Electron + React Native) |
| Compositor | Hyprland (Wayland) |
| Interfaz | Electron + React |
| 3D en interfaz | Three.js |
| Módulos 3D | Sistema de plugins. Cada módulo es archivo independiente |
| Modelado 3D | Blender integrado, lanzado desde PARCH. Control gestual via MediaPipe |
| App celular | React Native (Android primero, iOS después via Expo EAS) |
| Mirror de pantalla | WebRTC |
| Nube propia | Nextcloud self-hosted en el Mini PC |
| VPN | WireGuard |
| Encriptación disco | LUKS2 |
| Backup | Restic |
| Wake word | Porcupine (100% offline) |
| Voz → texto | Whisper Small (local, sin internet) |
| Texto → voz | Piper TTS (local) |
| Visión | MediaPipe + OpenCV + DeepFace |
| IoT cuarto | MQTT (Mini PC ↔ Raspberry Pi ↔ Arduino) |
| Base de datos | PostgreSQL |
| API interna | FastAPI (REST) |
| Nombre del sistema | PARCH |

---

## Hardware — decisiones finales

### Mini PC (cerebro, siempre encendido)
**MINISFORUM UM790 Pro** — ~$370-400 USD

| Especificación | Valor |
|---|---|
| CPU | AMD Ryzen 9 7940HS (8 núcleos, boost 4.0GHz) |
| RAM | 32 GB DDR5 |
| SSD | 1 TB NVMe |
| GPU integrada | AMD Radeon 780M RDNA3 (12 CUs, ~4.4 TFLOPS) |
| WiFi | WiFi 6E |
| Bluetooth | 5.2 |
| Consumo | ~35W en uso |
| OS a instalar | Ubuntu Server 24.04 LTS |

**Por qué NO el Beelink SER5 MAX (opción original):**
El SER5 MAX tiene Vega 8 (~1.5 TFLOPS). Corriendo Blender + MediaPipe a 60fps simultáneamente, la GPU se satura. La 780M es 3x más potente y maneja ambos sin problemas. La diferencia son ~$80 que son necesarios.

### Raspberry Pi 5 (hub del cuarto)
- Modelo: Raspberry Pi 5 8GB RAM — ~$80-100 USD
- Rol: SOLO controlar el cuarto físico (Arduino, sensores, luces)
- NO corre PARCH. Recibe comandos del Mini PC via WiFi (MQTT)

### Arduino
- Ya existe. Conectado al Raspberry Pi por USB
- Controla: relays de luces, sensores PIR, cerraduras, actuadores

### Cámara
- **Logitech C922** (o C920s) — ~$70-80 USD — DEBE ser 60fps
- Una webcam de 30fps hace que los gestos se vean desincronizados e inutilizables
- Conectada al Mini PC por USB

### UPS
- UPS básico ~$40-50 USD
- Protege contra cortes de luz que pueden corromper la base de datos

### PC de desarrollo (del usuario, NO parte de PARCH)
- Windows 11, RTX 3050
- Acá se programa todo, git push → Mini PC recibe y recarga módulos
- La RTX 3050 sirve para probar localmente partes pesadas antes de enviar al Mini PC

---

## Workflow de desarrollo

```
PC Windows (programás acá)
├── VS Code con extensión Remote SSH
├── Git
└── Python + Node.js instalados

          ↓ git push / SSH

Mini PC PARCH Linux (corre el sistema)
├── git pull automático
└── PARCH recarga módulos en caliente (sin reiniciar todo)
```

Los módulos están diseñados para recargarse en caliente. Un cambio en el módulo de voz no requiere reiniciar la interfaz.

---

## Arquitectura de carpetas (a crear en Fase 1)

```
parch/
├── core/
│   ├── orchestrator.py       ← cerebro: decide qué hacer con cada input
│   ├── claude_client.py      ← wrapper de la API de Claude
│   └── config.py
├── modules/
│   ├── voice/
│   │   ├── wake_word.py      ← Porcupine, siempre escuchando offline
│   │   ├── transcriber.py    ← Whisper Small
│   │   └── tts.py            ← Piper TTS
│   ├── vision/
│   │   ├── face_auth.py      ← MediaPipe + DeepFace, login facial
│   │   ├── gesture.py        ← MediaPipe Hands, gestos de control
│   │   └── presence.py       ← YOLOv8, detección de presencia
│   ├── blender_hands/
│   │   ├── hand_tracker.py   ← MediaPipe 60fps
│   │   ├── gesture_engine.py ← interpreta gestos
│   │   ├── blender_bridge.py ← habla con Blender via Python API (bpy)
│   │   └── calibration.py
│   ├── room/
│   │   └── mqtt_controller.py← comandos al Raspberry Pi
│   └── web_search/
│       └── google_launcher.py← abre ventana de Google cuando el usuario lo pide
├── api/
│   └── main.py               ← FastAPI, API REST interna
├── ui/
│   ├── electron/             ← interfaz visual principal
│   └── mobile/               ← React Native app
└── infra/
    ├── nextcloud/            ← configuración Nextcloud
    └── wireguard/            ← configuración VPN
```

---

## Los 10 módulos del sistema

### Módulo 1 — Boot personalizado
- GRUB2: logo PARCH, 0.5 segundos visible
- Plymouth: animación de carga custom (3-5 seg)
- Hyprland: compositor, nunca visible al usuario
- Electron: ocupa toda la pantalla al terminar Plymouth
- Resultado: encendés y ves solo PARCH

### Módulo 2 — Orquestador de IA (el corazón)
- PARCH recibe input (voz o texto)
- Analiza el tipo de pedido
- Si es pregunta general → Claude API → respuesta
- Si pide buscar en internet → abre ventana Google real → resultado a Claude → respuesta
- Si es acción del sistema → ejecuta localmente
- Si es comando del cuarto → MQTT a Raspberry Pi
- **PARCH nunca busca en internet por iniciativa propia**

### Módulo 3 — Voz
- Siempre escuchando: Porcupine detecta "Hey PARCH" (offline)
- Al activar: Whisper Small transcribe (local, privado)
- Respuesta: Piper TTS habla (local)
- Micrófono Bluetooth soportado via BlueZ nativo de Linux

### Módulo 4 — Visión
- Login: MediaPipe + DeepFace reconoce la cara → desbloquea
- Presencia: si el usuario se aleja, PARCH puede bloquearse
- Gestos mano: MediaPipe Hands, 21 puntos por mano a 60fps
- Gestos: índice = cursor, pinza = click, pinza+mover = arrastrar, dos manos = escalar

### Módulo 5 — App del celular
- React Native (Android primero, iOS después)
- Chat remoto con PARCH desde cualquier parte del mundo
- Mirror de pantalla en tiempo real (WebRTC) — como Chromecast
- Desbloqueo remoto con frase de seguridad
- Conexión siempre via VPN WireGuard

### Módulo 6 — Cuarto físico
- Raspberry Pi 5 recibe comandos MQTT del Mini PC
- Raspberry Pi envía órdenes al Arduino por USB
- Arduino controla relays (luces), sensores, cerraduras
- Protocolo: paho-mqtt

### Módulo 7 — Nube propia
- Nextcloud corriendo en el Mini PC
- Accesible desde el celular y desde fuera via VPN
- Guarda: proyectos 3D de Blender, conversaciones con PARCH, archivos personales
- Encriptación en reposo: LUKS2

### Módulo 8 — Seguridad
- Login físico: reconocimiento facial
- Acceso remoto: VPN WireGuard (criptografía ECC, inmune a fuerza bruta)
- Desbloqueo remoto: frase de seguridad en app del celular
- Disco: LUKS2 full-disk encryption

### Módulo 9 — Módulos 3D y plugins
- Sistema de plugins donde cada módulo es una carpeta independiente
- Módulos 3D usan Three.js, se construyen como páginas web
- Se instalan sin tocar el core de PARCH
- Ejemplos: reloj 3D, panel del cuarto, visualizador de música

### Módulo 10 — Control gestual en Blender
- Blender instalado en el Mini PC, lanzable por voz ("Hey PARCH, abrí Blender")
- MediaPipe Hands a 60fps lee la cámara
- gesture_engine.py interpreta: pinza=agarrar, pinza+mover=trasladar, girar muñeca=rotar, dos manos=escalar
- blender_bridge.py traduce gestos a comandos Blender via Python API (bpy)
- calibration.py: el usuario calibra su espacio de trabajo una vez
- Los proyectos se guardan automáticamente en Nextcloud
- **Requiere Radeon 780M o superior — no funciona bien con Vega 8**

---

## Fases de desarrollo (7 fases)

| Fase | Contenido | Duración estimada |
|---|---|---|
| 1 | Boot custom + Claude API (texto) + interfaz básica | 2-3 meses |
| 2 | Voz (Whisper+Porcupine+TTS) + Visión (facial+gestos) | 2-3 meses |
| 3 | App celular (React Native) + mirror + VPN WireGuard | 2 meses |
| 4 | Cuarto físico: Raspberry Pi + Arduino + MQTT | 1-2 meses |
| 5 | Nube (Nextcloud) + Seguridad (LUKS2) + Backup | 1-2 meses |
| 6 | Pulido: módulos 3D Three.js + sistema de plugins | Ongoing |
| 7 | Blender + control gestual (módulo 10 completo) | 2-3 meses |

**Regla del proyecto: completar cada fase antes de avanzar a la siguiente.**

---

## Análisis de riesgos — ya identificados y resueltos

| Severidad | Riesgo | Solución |
|---|---|---|
| CRÍTICO | 500GB SSD se llena con proyectos Blender | Pedir UM790 Pro con 1TB SSD |
| CRÍTICO | Vega 8 no aguanta Blender + MediaPipe | Usar UM790 Pro con Radeon 780M |
| IMPORTANTE | Cámara 30fps = gestos laggy | Logitech C922, 60fps obligatorio |
| IMPORTANTE | App iOS requiere Mac para compilar | Empezar Android + PWA. iOS después via Expo EAS |
| IMPORTANTE | Sin internet = PARCH sin cerebro | Ollama local (Llama 3.1 8B) como fallback offline |
| MEDIO | Whisper grande es lento sin GPU dedicada | Usar Whisper Small, responde en ~0.8seg |
| MENOR | Corte de luz corrompe base de datos | UPS básico ~$40 |
| MENOR | Costos API Claude impredecibles | Plan Claude Pro ($20/mes fijo) |

---

## Stack tecnológico completo

### Python (backend)
```
anthropic          # Claude API
openai-whisper     # transcripción de voz local
pvporcupine        # wake word offline
piper-tts          # síntesis de voz local
mediapipe          # visión: cara, manos, gestos
opencv-python      # procesamiento de imagen
deepface           # reconocimiento facial
fastapi            # API REST interna
uvicorn            # servidor ASGI
sqlalchemy         # ORM para PostgreSQL
paho-mqtt          # comunicación con Raspberry Pi
bpy                # Python API de Blender (módulo 10)
ollama             # modelos IA locales (fallback offline)
```

### JavaScript / TypeScript (frontend)
```
electron           # interfaz desktop
react              # UI de la interfaz
three.js           # módulos 3D
framer-motion      # animaciones
react-native       # app del celular
expo               # toolchain React Native
webrtc             # mirror de pantalla
socket.io-client   # comunicación en tiempo real
```

### Infraestructura Linux
```
Ubuntu Server 24.04 LTS   # OS base
GRUB2                     # bootloader custom
Plymouth                  # animación de carga custom
Hyprland                  # compositor Wayland
Nextcloud                 # nube self-hosted
WireGuard                 # VPN
LUKS2                     # encriptación de disco
Restic                    # backup
PostgreSQL                # base de datos
MQTT (Mosquitto)          # protocolo IoT
Blender                   # modelado 3D (módulo 10)
```

---

## Reglas importantes del proyecto

1. **PARCH nunca busca en internet por su cuenta.** Solo cuando el usuario lo pide explícitamente. Cuando busca, abre una ventana real de Google.

2. **Claude es el único cerebro.** PARCH no toma decisiones inteligentes solo. Todo pasa por Claude API. El modelo local (Ollama) es solo fallback de emergencia cuando no hay internet.

3. **Cada módulo es independiente.** Se puede desarrollar, testear y recargar sin tocar el resto del sistema.

4. **La interfaz visual es 100% custom.** El usuario nunca ve Linux, terminales, ni nada que no sea PARCH.

5. **Perfección sobre velocidad.** Cada fase se termina completamente antes de avanzar. Sin atajos.

6. **Privacidad total.** Los datos del usuario nunca salen de su hardware. Nube propia, modelos de voz locales, sin telemetría.

7. **El hardware importa.** Cualquier feature nueva debe ser evaluada contra las especificaciones del Mini PC antes de prometerse.

---

## Estado actual del proyecto

- **Fase actual:** Planificación completada ✓
- **Próximo paso:** Comprar hardware + preparar entorno de desarrollo en Windows
- **Código escrito:** Ninguno todavía (solo planificación)
- **Documentación:** Reporte técnico v1.1 en `docs/PARCH_Reporte_Tecnico.pdf`
- **Repositorio:** Inicializado, listo para desarrollo

---

## Archivos en este repositorio

```
PARCH/
├── CLAUDE.md                        ← este archivo (contexto para Claude)
├── README.md                        ← descripción pública del proyecto
├── .gitignore
├── docs/
│   └── PARCH_Reporte_Tecnico.pdf   ← plan técnico completo v1.1
└── scripts/
    └── parch_report.py             ← script Python que genera el PDF
```

---

## Cómo continuar el desarrollo en futuras sesiones

Cuando abras Claude Code en este repositorio y quieras continuar:

1. Claude lee este CLAUDE.md automáticamente y tiene todo el contexto
2. No hace falta re-explicar las decisiones tomadas
3. Decile directamente en qué fase estás y qué querés implementar
4. Claude sabe el stack, la arquitectura, el hardware, las reglas y los riesgos

Ejemplo: *"Estoy en Fase 1, quiero implementar el boot personalizado con GRUB2"*
