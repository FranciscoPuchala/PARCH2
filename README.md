# PARCH
### Sistema Personal Autónomo de Respuesta e Control Holístico

Sistema operativo personal con identidad visual propia, inteligencia artificial integrada via Claude API, control por voz, reconocimiento facial y gestual, aplicación móvil, integración con hardware físico (Arduino + Raspberry Pi), modelado 3D con Blender controlado por gestos, y nube privada encriptada.

---

## Concepto

PARCH es un JARVIS personal. Al encender la computadora, el usuario ve únicamente la interfaz de PARCH — su logo, sus animaciones, su diseño. Linux corre por debajo pero jamás es visible.

La inteligencia viene de Claude API (Anthropic). PARCH no piensa por sí mismo — sabe cuándo y cómo hablarle a Claude para obtener la mejor respuesta posible.

---

## Características principales

- **Boot personalizado** — Tu logo, tu animación, cero señales de Linux
- **IA via Claude** — Siempre pregunta a Claude. Solo busca en internet si se lo pedís
- **Control por voz** — Wake word offline "Hey PARCH" + Whisper para transcripción local
- **Reconocimiento facial** — Login automático con tu cara
- **Control gestual** — Mover la interfaz y objetos 3D con las manos
- **Blender integrado** — Modelado 3D controlado con gestos (estilo Iron Man)
- **App del celular** — Mirror de pantalla, chat remoto, desbloqueo por frase
- **Cuarto inteligente** — Arduino + Raspberry Pi para luces, sensores, puertas
- **Nube propia** — Nextcloud self-hosted, encriptada, solo tuya
- **VPN WireGuard** — Acceso seguro desde cualquier parte del mundo

---

## Hardware

| Componente | Modelo | Rol |
|---|---|---|
| Mini PC (cerebro) | MINISFORUM UM790 Pro | PARCH corre aquí 24/7 |
| Raspberry Pi 5 | 8GB RAM | Hub del cuarto físico |
| Arduino | Ya existente | Sensores y actuadores |
| Cámara | Logitech C922 (60fps) | Visión, gestos, login facial |

---

## Stack tecnológico

**Backend (Python):** Claude API · Whisper · Porcupine · Piper TTS · MediaPipe · FastAPI · PostgreSQL · MQTT

**Frontend (JavaScript):** Electron + React · Three.js · React Native · WebRTC

**Infraestructura:** Ubuntu Server 24.04 · Nextcloud · WireGuard · LUKS2 · Restic

---

## Fases de desarrollo

| Fase | Contenido | Estado |
|---|---|---|
| Fase 1 | Fundación: boot custom + Claude API básico | Pendiente |
| Fase 2 | Voz + Visión: Whisper + gestos + login facial | Pendiente |
| Fase 3 | App del celular: React Native + mirror + VPN | Pendiente |
| Fase 4 | Cuarto: Raspberry Pi + Arduino | Pendiente |
| Fase 5 | Nube y Seguridad: Nextcloud + LUKS2 | Pendiente |
| Fase 6 | Pulido: módulos 3D + plugins | Pendiente |
| Fase 7 | Blender + Control Gestual 3D | Pendiente |

---

## Documentación

- [Reporte Técnico Completo v1.1](docs/PARCH_Reporte_Tecnico.pdf) — Plan de arquitectura completo con análisis de riesgos
- [Script generador del reporte](scripts/parch_report.py) — Genera el PDF desde Python

---

## Autor

Francisco Puchala · franpuchala8@gmail.com
